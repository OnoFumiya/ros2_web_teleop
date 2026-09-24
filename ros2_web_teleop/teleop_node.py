import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient

import os
# import time
import threading
from subprocess import Popen, DEVNULL

from .websocket_server import WebSocketServer
from . import network_address_manager

from ament_index_python.packages import get_package_share_directory

import numpy as np

from cv_bridge import CvBridge

from std_msgs.msg import String
from geometry_msgs.msg import Twist, TwistStamped
from geometry_msgs.msg import Vector3
from sensor_msgs.msg import Image


class VelocityPublisher(Node):
    def __init__(self):
        super().__init__('web_teleop_manager')

        self.bridge = CvBridge()

        # # Declare Parameters
        self.declare_parameter("topic_name", "cmd_vel")
        self.declare_parameter("use_stamped", False)
        self.declare_parameter("websocket_port", 8080)
        self.declare_parameter("http_port", 8000)
        self.declare_parameter("control_rate", 20)
        self.declare_parameter("max_linear_velocity", 0.20)
        self.declare_parameter("max_angular_velocity", 0.75)
        self.declare_parameter("min_linear_velocity", 0.02)
        self.declare_parameter("min_angular_velocity", 0.1)
        self.declare_parameter("ui_bringup", False)

        self.topic_name = self.get_parameter("topic_name").get_parameter_value().string_value
        self.use_stamped = self.get_parameter("use_stamped").get_parameter_value().bool_value
        self.websocket_port = self.get_parameter("websocket_port").get_parameter_value().integer_value
        self.http_port = self.get_parameter("http_port").get_parameter_value().integer_value
        self.control_rate = self.get_parameter("control_rate").get_parameter_value().integer_value
        self.max_linear_velocity = self.get_parameter("max_linear_velocity").get_parameter_value().double_value
        self.max_angular_velocity = self.get_parameter("max_angular_velocity").get_parameter_value().double_value
        self.min_linear_velocity = self.get_parameter("min_linear_velocity").get_parameter_value().double_value
        self.min_angular_velocity = self.get_parameter("min_angular_velocity").get_parameter_value().double_value
        self.ui_bringup = self.get_parameter("ui_bringup").get_parameter_value().bool_value

        self.web_server = WebSocketServer("0.0.0.0", self.websocket_port)

        self.publish_qrcode_image()

        self.websocket_thread = threading.Thread(
            target=self.web_server.run,
            daemon=True
        )

        self.websocket_thread.start()

        # Publisherの作成
        if self.use_stamped:
            self.publisher = self.create_publisher(TwistStamped, self.topic_name, 10)
        else:
            self.publisher = self.create_publisher(Twist, self.topic_name, 10)

        self.velocity = TwistStamped() if self.use_stamped else Twist()

        self.stack_vel = Twist(linear=Vector3(z=-1.0), angular=Vector3(x=-1.0, y=-1.0))

        self.timer = self.create_timer(1.0 / self.control_rate, self.control_callback)


    def publish_qrcode_image(self):

        qos_policy = rclpy.qos.QoSProfile(
            reliability=rclpy.qos.ReliabilityPolicy.RELIABLE,
            history=rclpy.qos.HistoryPolicy.KEEP_LAST,
            durability=rclpy.qos.DurabilityPolicy.TRANSIENT_LOCAL,
            depth=1
        )

        self.url_link_pub = self.create_publisher(String, "web_teleop_url_link", qos_policy)
        self.url_qr_pub = self.create_publisher(Image, "web_teleop_url_qrcode", qos_policy)

        url = "http://" + str(network_address_manager.get_ipaddress()) + ":" + str(self.http_port)
        qrcode_file = os.path.join(get_package_share_directory("ros2_web_teleop"), "img", "qrcode.png")

        print("\033[34mGUI URL: " + str(url) + "\033[0m", flush=True)

        img = network_address_manager.create_qrcode(url, qrcode_file)
        cv_img = np.array(img).astype(np.uint8) * 255
        ros_img = self.bridge.cv2_to_imgmsg(cv_img, encoding="mono8")

        # Publish URL String and QRcode Image
        self.url_link_pub.publish(String(data=url))
        self.url_qr_pub.publish(ros_img)

        if (self.get_parameter("ui_bringup").get_parameter_value().bool_value):
            Popen(["xdg-open", url], stderr=DEVNULL) # bringup the engine


    def control_callback(self):
        # GUIからのデータを取得
        data = self.web_server.data

        if (np.abs(data["y"] * self.max_linear_velocity) < self.min_linear_velocity):
            vel = Twist(angular=Vector3(z=float(-data["x"] * self.max_angular_velocity)))
        else:
            pararel = data["y"] / np.abs(data["y"])
            vel = Twist(linear=Vector3(x=float(data["y"] * self.max_linear_velocity)), angular=Vector3(z=float(-data["x"] * pararel * self.max_angular_velocity)))

        if self.use_stamped:
            self.velocity.header.stamp = self.get_clock().now().to_msg()
            self.velocity.twist = vel
        else:
            self.velocity = vel

        if (self.stack_vel != vel):
            self.publisher.publish(self.velocity)
            self.stack_vel = vel


def main():
    rclpy.init()
    node = VelocityPublisher()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

# =========================

if __name__ == "__main__":
    main()
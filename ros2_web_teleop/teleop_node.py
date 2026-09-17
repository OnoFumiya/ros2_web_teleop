import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient

import os
# import copy
# import time
import threading
from subprocess import Popen

from .websocket_server import WebSocketServer

from ament_index_python.packages import get_package_share_directory
# import yaml

# import numpy as np

# from cv_bridge import CvBridge

from std_msgs.msg import String
from geometry_msgs.msg import Twist, TwistStamped
from geometry_msgs.msg import Vector3
from sensor_msgs.msg import Image

# from .functions import create_ros_msg
# from .functions import ros2_communications_control
# from .functions import network_address_manager
# from .functions import create_html_and_javascript

# from flask import Flask
# from flask import request
# from flask import jsonify
# from flask import send_from_directory

# from flask_cors import CORS

# app = Flask(__name__, static_folder="static")

# CORS(app)


class VelocityPublisher(Node):
    def __init__(self):
        super().__init__('web_teleop_manager')

        # self.app = app
        # self.bridge = CvBridge()

        # default_config_file = os.path.join(get_package_share_directory("blockly_ros2"), "config", "block_structure.yaml")

        # # Declare Parameters
        self.declare_parameter("port", 8080)
        self.declare_parameter("ui_bringup", False)
        self.declare_parameter("control_rate", 20)
        self.declare_parameter("topic_name", "cmd_vel")
        self.declare_parameter("use_stamped", False)
        self.declare_parameter("max_linear_velocity", 0.20)
        self.declare_parameter("max_angular_velocity", 0.75)

        self.port = self.get_parameter("port").get_parameter_value().integer_value
        self.ui_bringup = self.get_parameter("ui_bringup").get_parameter_value().bool_value
        self.control_rate = self.get_parameter("control_rate").get_parameter_value().integer_value
        self.topic_name = self.get_parameter("topic_name").get_parameter_value().string_value
        self.use_stamped = self.get_parameter("use_stamped").get_parameter_value().bool_value
        self.max_linear_velocity = self.get_parameter("max_linear_velocity").get_parameter_value().double_value
        self.max_angular_velocity = self.get_parameter("max_angular_velocity").get_parameter_value().double_value

        self.web_server = WebSocketServer("0.0.0.0", self.port)

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

        self.timer = self.create_timer(1.0 / self.control_rate, self.control_callback)


    def control_callback(self):
        # GUIからのデータを取得
        data = self.web_server.data
        # print(f"\033[34mCurrent data: {data}\033[0m", flush=True)

        vel = Twist(linear=Vector3(x=float(data["y"])), angular=Vector3(z=float(-data["x"])))
        vel.linear.x = vel.linear.x * self.max_linear_velocity
        vel.angular.z = vel.angular.z * self.max_angular_velocity

        if self.use_stamped:
            self.velocity.header.stamp = self.get_clock().now().to_msg()
            self.velocity.twist = vel
        else:
            self.velocity = vel

        self.publisher.publish(self.velocity)


def main():
    rclpy.init()
    node = VelocityPublisher()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

# =========================

if __name__ == "__main__":
    main()
import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from launch.conditions import IfCondition


def generate_launch_description():

    pkg_share = get_package_share_directory("ros2_web_teleop")

    namespace_arg = DeclareLaunchArgument(
        "web_teleop_namespace",
        default_value="",
        description="Namespace for the nodes"
    )

    topic_name_arg = DeclareLaunchArgument(
        "web_teleop_topic_name",
        default_value="/nekomimi_bot/cmd_vel",
        description="Topic name for the teleoperation commands."
    )

    use_stamped_arg = DeclareLaunchArgument(
        "web_teleop_use_stamped",
        default_value="False",
        description="Whether to use stamped messages. (True: geometry_msgs/TwistStamped, False: geometry_msgs/Twist)"
    )

    port_arg = DeclareLaunchArgument(
        "web_teleop_port",
        default_value="8080",
        description="port number for network."
    )

    ui_bringup_arg = DeclareLaunchArgument(
        "web_teleop_ui_bringup",
        default_value="True",
        description="turn on the default engine for UI window (Blockly site)"
    )

    qrcode_view_arg = DeclareLaunchArgument(
        "web_teleop_qrcode_view",
        default_value="True",
        description="turn on the RQT Image View for QRcode.",
    )

    display_server = ExecuteProcess(
        cmd=["python3", "-m", "http.server", "8000"],
        cwd=os.path.join(pkg_share, "web"),
        output="screen",
    )

    ros2_manager_node = Node(
        package="ros2_web_teleop",
        executable="teleop_node",
        name="web_teleop_manager",
        namespace=LaunchConfiguration('web_teleop_namespace'),
        output="screen",
        parameters=[
            {
                "topic_name": LaunchConfiguration("web_teleop_topic_name"),
                "use_stamped": LaunchConfiguration("web_teleop_use_stamped"),
                "port": LaunchConfiguration("web_teleop_port"),
                "ui_bringup": LaunchConfiguration("web_teleop_ui_bringup"),
            }
        ]
    )

    # rqt_view_node = Node(
    #     package="rqt_image_view",
    #     executable="rqt_image_view",
    #     name="qrcode_viewer",
    #     arguments=["/web_teleop_qrcode"],
    #     condition=IfCondition(LaunchConfiguration("web_teleop_qrcode_view")),
    # )

    return LaunchDescription([
        namespace_arg,
        topic_name_arg,
        use_stamped_arg,
        port_arg,
        ui_bringup_arg,
        qrcode_view_arg,
        display_server,
        ros2_manager_node,
        # rqt_view_node,
    ])

<a name="readme-top"></a>

[EN](README.md) | [JA](README_ja.md)

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![License][license-shield]][license-url]

# ROS2 Web Teleop

A ROS 2 web-based teleoperation package for controlling robots from a smartphone via a virtual joystick and WebSocket.

<!-- Table of Contents -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#introduction">Introduction</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#launch-and-usage">Launch and Usage</a></li>
      <li><a href="#parameter-settings">Parameters Setting</a></li>
    <li><a href="#milestone">Milestone</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>




<!-- Repository overview -->
## Introduction

This repository provides a ROS 2-compatible, web-based teleoperation package that allows users to intuitively control a robot from a smartphone or mobile device via WebSockets. 

It features an on-screen virtual joystick, offering a smooth and responsive control interface right inside the web browser.

Key Features & Customization:
Flexible Message Type Support: Supports dynamically publishing to either geometry_msgs/msg/Twist or geometry_msgs/msg/TwistStamped to fit your specific robot setup.
Configurable Topic Names: Easily customize the target topic name for velocity commands.
Custom Port Configuration: Enables setting custom WebSocket ports to prevent conflicts with other running services or nodes on the same network.


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- Getting Started -->
## Getting Started

This section describes how to set up this repository.


<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Prerequisites

First, prepare the following environment before proceeding to the installation steps.

| System  | Version |
| ------------- | ------------- |
| Ubuntu | 26.04 (Resolute Raccoon) |
| ROS    | Lyrical Luth |
| Python | 3.14 |

<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Installation
1. First, navigate to the `src` folder of your ROS 2 workspace.
```sh
$ cd ~/colcon_ws/src
```
2. Clone the ROS package `ros2_web_teleop` into the `src` folder.
```sh
$ git clone -b lyrical-devel https://github.com/OnoFumiya/ros2_web_teleop.git
```
3. Navigate into the cloned repository folder.
```sh
$ cd ros2_web_teleop
```
4. Install the required dependencies.
```sh
$ bash install.sh
```
5. Build the package.
```sh
$ cd ~/colcon_ws/
$ colcon build --symlink-install
$ source ~/colcon_ws/install/setup.sh
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Launch and Usage -->
## Launch and Usage
Once the package has been successfully built, you can verify its operation using the following steps:

If you need to configure detailed settings such as port numbers or topic names, refer to [this page](#parameter-settings) for instructions.

Additionally, when using a remote-controlled device, ensure it is connected to the same network (such as the same Wi-Fi network) as the server.

※A network connection is required because the system uses the network’s hostname for lookup.

```sh
$ ros2 launch ros2_web_teleop teleop_ros_server.launch.py
```

If you launch the application with the default settings, a QR code with a UI and the website linked to that QR code will be displayed.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


# Parameter Settings

The parameters in the Launch file and their settings are shown below.

| Parameter Name  | Meaning | Type | Default Value |
| ------------- | ------------- | ------------- | ------------- |
| `web_teleop_namespace` | This node's namespace. This namespace is appended to rqt images and topic names. | String | ""(empty string) |
| `web_teleop_topic_name` | The topic name published from this node | String | "cmd_vel" |
| `web_teleop_use_stamped` | Whether to publish TwistStamped or Twist types (True for TwistStamped). | Bool | False |
| `web_teleop_websocket_port` | Internal port number for exchanging joystick values with the Node. Must be a value that does not conflict with others within the global IP address range. (Recommended to change if the default does not work) | Int | 7777 |
| `web_teleop_http_port` | Port number for displaying the joystick. Must be a value that does not conflict with other ports on the global IP address, including the `web_teleop_websocket_port` mentioned above. (Recommended to change if the default does not work) | Int | 7000 |
| `control_rate` | Number of times to publish per second. [Hz] | Int | 20 |
| `max_linear_velocity` | Absolute value of the maximum linear velocity based on the joystick's forward and backward tilt. [m/s] | Double | 0.3 |
| `max_angular_velocity` | Absolute value of the maximum angular velocity resulting from the joystick's left-right tilt. [rad/s] | Double | 1.0 |
| `min_linear_velocity` | Absolute value of the linear velocity at or below which values are ignored when the tilt is small. [m/s] | Double | 0.05 |
| `min_angular_velocity` | Absolute value of the angular velocity at or below which values are ignored when the tilt is small. [rad/s] | Double | 0.1 |
| `web_teleop_ui_bringup` | Whether to display the site where operations can be performed. | Bool | True |
| `web_teleop_qrcode_view` | Whether to display a QR code for the URL that allows navigation to the site where operations can be performed. ※ | Bool | True |

> [!NOTE]
> ※Even if you set “Do not display QR code” (False), the QR code image and its URL will each be published to the topic once as Transient Local (QoS).
> They are published to `web_teleop_url_qrcode` (sensor_msgs/Image) and `web_teleop_url_link` (std_msgs/String), respectively. Note that since the namespace is applied, the namespace will be appended when configuring the namespace.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Milestones

- [ ] Stop allowing immediate speed input and add processing such as publishing the current speed and target speed using a smooth transition.

Please check the [Issue page][issues-url] for current bugs and feature requests.


## Acknowledgments
[ROS2 Lyrical](http://wiki.ros.org/lyrical)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/OnoFumiya/ros2_web_teleop.svg?style=for-the-badge
[contributors-url]: https://github.com/OnoFumiya/ros2_web_teleop/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/OnoFumiya/ros2_web_teleop.svg?style=for-the-badge
[forks-url]: https://github.com/OnoFumiya/ros2_web_teleop/network/members
[stars-shield]: https://img.shields.io/github/stars/OnoFumiya/ros2_web_teleop.svg?style=for-the-badge
[stars-url]: https://github.com/OnoFumiya/ros2_web_teleop/stargazers
[issues-shield]: https://img.shields.io/github/issues/OnoFumiya/ros2_web_teleop.svg?style=for-the-badge
[issues-url]: https://github.com/OnoFumiya/ros2_web_teleop/issues
[license-shield]: https://img.shields.io/github/license/OnoFumiya/ros2_web_teleop.svg?style=for-the-badge
[license-url]: LICENSE
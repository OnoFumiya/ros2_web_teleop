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
      <li><a href="#parameters-setting">Parameters Setting</a></li>
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



<p align="right">(<a href="#readme-top">back to top</a>)</p>


# Parameters Setting

Parameters Setting...


<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Milestones

- [ ] 
- [ ] 
- [ ] 

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

```
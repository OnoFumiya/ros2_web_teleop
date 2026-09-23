<a name="readme-top"></a>

[英語](README.md) | [日本語](README_ja.md)

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![License][license-shield]][license-url]

# ROS2 Web Teleop

仮想ジョイスティックとWebSocketを介して、スマートフォンからロボットを制御するための、ROS 2 対応のWebベース遠隔操作パッケージ。


<!-- Table of Contents -->
<details>
  <summary>目次</summary>
  <ol>
    <li>
      <a href="#概要">概要</a>
    </li>
    <li>
      <a href="#はじめに">はじめに</a>
      <ul>
        <li><a href="#前提条件">前提条件</a></li>
        <li><a href="#インストール">インストール</a></li>
      </ul>
    </li>
    <li><a href="#起動と使用方法">起動と使用方法</a></li>
      <li><a href="#パラメータ設定">パラメータ設定</a></li>
    <li><a href="#マイルストーン">マイルストーン</a></li>
    <li><a href="#参考文献">参考文献</a></li>
  </ol>
</details>




<!-- Repository overview -->
## 概要

本リポジトリは、スマートフォンなどのモバイル端末から WebSocket 通信を介してロボットを直感的に操作できる、ROS 2 対応の Web ベース遠隔操作（Teleop）パッケージです。

ブラウザ上に表示される仮想ジョイスティックにより、スムーズな操縦インターフェースを提供します。

主な特徴と調整機能:
柔軟なメッセージ型対応: 用途やロボット構成に合わせて、geometry_msgs/msg/Twist および geometry_msgs/msg/TwistStamped のいずれかを動的に選択して Publish 可能です。
トピック名自由設定: パブリッシュ先となる速度指令トピック名を簡単にカスタマイズできます。
ポート番号設定: WebSocket 通信用のポート番号を変更できるため、他のネットワークサービスやノードとのポート競合を未然に防ぎます。


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- Getting Started -->
## はじめに

このリポジトリの設定方法について説明します。


<p align="right">(<a href="#readme-top">back to top</a>)</p>

### 前提条件

まず、インストール手順に進む前に、以下の環境を整えておいてください。

| System  | Version |
| ------------- | ------------- |
| Ubuntu | 26.04 (Resolute Raccoon) |
| ROS    | Lyrical Luth |
| Python | 3.14 |

<p align="right">(<a href="#readme-top">back to top</a>)</p>


### インストール
1. `src`フォルダへ移動
```sh
$ cd ~/colcon_ws/src
```
2. 本リポジトリを`src`直下にclone
```sh
$ git clone -b lyrical-devel https://github.com/OnoFumiya/ros2_web_teleop.git
```
3. 本リポジトリへ移動
```sh
$ cd ros2_web_teleop
```
4. 必要なライブラリをインストール
```sh
$ bash install.sh
```
5. パッケージをビルド
```sh
$ cd ~/colcon_ws/
$ colcon build --symlink-install
$ source ~/colcon_ws/install/setup.sh
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Launch and Usage -->
## 起動と使用方法
パッケージのビルドが正常に完了したら、以下の手順で動作を確認できます。



<p align="right">(<a href="#readme-top">back to top</a>)</p>

# パラメータ設定

パラメータ設定...

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## マイルストーン

[ ] 
[ ] 
[ ] 

Please check the [Issue page][issues-url] for current bugs and feature requests.


## 参考文献
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
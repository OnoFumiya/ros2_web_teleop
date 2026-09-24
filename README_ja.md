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

ポート番号の設定やTopic名など詳細に設定する必要がある場合は[こちら](#パラメータ設定)を参考に設定する。

また、遠隔操作のデバイスを使用する場合、IPアドレスが同一となるネットワーク(同一Wi-Fi等)に設定する。

※ネットワークのhostnameを検索する使用のため、ネットワークは必須となる。

```sh
$ ros2 launch ros2_web_teleop teleop_ros_server.launch.py
```

デフォルトの設定のまま起動した場合、UIのあるQRコードとそのQRコード先のサイトが表示される。

<p align="right">(<a href="#readme-top">back to top</a>)</p>

# パラメータ設定

Launchファイル上のパラメータとその設定は以下に示す。

| パラメータ名  | 意味 | 型 |デフォルト値 |
| ------------- | ------------- | ------------- | ------------- |
| `web_teleop_namespace` | このノードのNameSpace. rqtのImageやTopic NameにもこのNameSpaceが付加される. | String | ""(空文字) |
| `web_teleop_topic_name` | このノードからPublishするTopic名 | String | "cmd_vel" |
| `web_teleop_use_stamped` | PublishするのはTwistStamped型またはTwist型か（TrueでTwistStamped）. | Bool | False |
| `web_teleop_websocket_port` | Joystickの値をNodeとやり取りするための内部Port番号. Global IP アドレス内で他と競合しない値にする必要がある. (Defaultのままでうまく行かなかった場合に変えることを推奨) | Int | 7777 |
| `web_teleop_http_port` | Joystickが表示されるためのPort番号. Global IP アドレス内で上記の`web_teleop_websocket_port`を含め、他と競合しない値にする必要がある. (Defaultのままでうまく行かなかった場合に変えることを推奨) | Int | 7000 |
| `control_rate` | 1秒間に何度Publishするか. [Hz] | Int | 20 |
| `max_linear_velocity` | Joystickの前後方向の傾きによる最高並進速度の絶対値. [m/s] | Double | 0.3 |
| `max_angular_velocity` | Joystickの左右方向の傾きによる最高角速度の絶対値. [rad/s] | Double | 1.0 |
| `min_linear_velocity` | 傾きが小さいときにある速度以下を無視する並進速度の絶対値. [m/s] | Double | 0.05 |
| `min_angular_velocity` | 傾きが小さいときにある速度以下を無視する角速度の絶対値. [rad/s] | Double | 0.1 |
| `web_teleop_ui_bringup` | 操作ができるサイトを表示するかどうか.  | Bool | True |
| `web_teleop_qrcode_view` | 操作ができるサイトへ移動することができるURLのQRコードを表示するか. ※ | Bool | True |

> [!NOTE]
> ※QRコードを表示しない(False)とした場合でも、QRコードの画像とそのURLは、それぞれTransient Local(QoS)として、トピックに1回ずつ公開されます。
> 公開先は、それぞれ`web_teleop_url_qrcode`(sensor_msgs/Image)および`web_teleop_url_link`(std_msgs/String)です。なおNameSpaceが適応されるため、NameSpace設定時はNameSpaceが付加される点に注意。

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## マイルストーン

- [ ] 速度の即時入力をやめ現在速度と目標速度をならしでPublishするなどの処理を追加する

現在のバグや機能要望については、[こちら][issues-url]をご確認ください。


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
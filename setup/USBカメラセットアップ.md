# USBカメラセットアップ

## デバイスの確認
~~~
$lsusb
~~~
~~~
Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
Bus 001 Device 007: ID 1c4f:0002 SiGma Micro Keyboard TRACER Gamma Ivory
Bus 001 Device 008: ID 046d:0825 Logitech, Inc. Webcam C270
Bus 001 Device 005: ID 192f:0416 Avago Technologies, Pte. ADNS-5700 Optical Mouse Controller (3-button)
Bus 001 Device 004: ID 0451:2046 Texas Instruments, Inc. TUSB2046 Hub
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
~~~

Logitech, Inc. Webcam C270
が認識されている。

デスクトップからCheeseアプリを開くが、
No device foundとなって認識されない


##　認識させる
https://qiita.com/akira-sasaki/items/7465f6cfd6ab5977f1c9

- GStreamerのv4l2srcのインストール
~~~
$ sudo apt install v4l-utils
デバイス一覧取得
$ v4l2-ctl --list-device
デバイス情報取得
$ v4l2-ctl -d /dev/video0 --list-formats-ext
~~~
結果が帰ってくればOK

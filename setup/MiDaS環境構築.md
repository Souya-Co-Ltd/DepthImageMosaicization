# MiDaS環境構築

## Software
* Jetpack 5.0.1
* Python 3.8.10
* torch 1.13.0a0+340c4120.nv22.6
* torchvision 0.13.1
* CV2 4.5.1(GSTREAMER support)

# Setup
## Clone project
```console
$ git clone https://github.com/Souya-Co-Ltd/DepthImageMosaicization.git
```

## Install and upgrade pip3
```console
$ sudo apt-get -y update
$ sudo apt-get install -y python3-pip
$ pip install -U pip testresources setuptools==49.6.0
```

## Build CV2
```console
$ sudo apt install -y libtbb-dev
$ pip install -U numpy --no-cache-dir --no-binary numpy
$ wget https://github.com/opencv/opencv/archive/4.5.1.zip
$ unzip 4.5.1.zip
$ rm 4.5.1.zip
$ mv opencv-4.5.1 OpenCV
$ cd OpenCV
$ wget https://github.com/opencv/opencv_contrib/archive/4.5.1.zip
$ unzip 4.5.1.zip
$ rm 4.5.1.zip
$ mkdir build
$ cd build
$ cmake \
    -D CMAKE_BUILD_TYPE=Release \
    -D OPENCV_ENABLE_NONFREE=ON \
    -D OPENCV_EXTRA_MODULES_PATH=../opencv_contrib-4.5.1/modules/ \
    -D OPENCV_DNN_CUDA=ON \
    -D OPENCV_GENERATE_PKGCONFIG=ON \
    -D BUILD_DOCS=OFF \
    -D BUILD_EXAMPLES=OFF \
    -D BUILD_JASPER=OFF \
    -D BUILD_OPENEXR=OFF \
    -D BUILD_PERF_TESTS=OFF \
    -D BUILD_TESTS=OFF \
    -D BUILD_opencv_apps=OFF \
    -D BUILD_opencv_ml=OFF \
    -D ENABLE_FAST_MATH=ON \
    -D WITH_EIGEN=ON \
    -D WITH_V4L=ON \
    -D WITH_FFMPEG=ON \
    -D WITH_TBB=ON \
    -D WITH_OPENMP=ON \
    -D WITH_CUDA=ON \
    -D WITH_NVCUVID=OFF \
    -D BUILD_opencv_cudacodec=OFF \
    -D WITH_CUDNN=ON \
    -D WITH_CUBLAS=ON \
    -D CUDA_FAST_MATH=ON \
    -D WITH_CUFFT=ON \
    -D build_opencv_python3=ON \
    -D build_opencv_python2=OFF \
    -D WITH_PYTHON=ON \
    -D INSTALL_PYTHON_EXAMPLES=OFF \
    -D PYTHON_DEFAULT_EXECUTABLE=/usr/bin/python3 \
    -D PYTHON3_EXECUTABLE=/usr/bin/python3 \
    ..
$ make all -j4
$ make install
```

## pytorchインストール
timmを入れると依存関係でインストールされるが、GPUを使う為先にインストールする
https://docs.nvidia.com/deeplearning/frameworks/install-pytorch-jetson-platform/index.html
上記サイトを参考にする。

Jetpack 5.0.1　の場合　export TORCH_INSTALLは以下を指定する。
~~~
export TORCH_INSTALL=https://developer.download.nvidia.com/compute/redist/jp/v50/pytorch/torch-1.13.0a0+340c4120.nv22.06-cp38-cp38-linux_aarch64.whl
~~~

## timmインストール
~~~
$ pip3 install timm
~~~

インストールは以上

## 実行
~~~
export LD_PRELOAD=/home/souya/.local/lib/python3.8/site-packages/torch/lib/libgomp-d22c30c5.so.1:/usr/lib/aarch64-linux-gnu/libgomp.so.1:/lib/aarch64-linux-gnu/libGLdispatch.so.0
cd [DepthImageMosaicization path]
cd src
python3 main.py
~~~

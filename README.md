# ME369P-Group-11

## Program Capabilities:
1. Open camera and record video
2. Real-time facial recognition between stored photo and camera
3. a) If a stranger is detected it will alarm and email a picture to the homeowner
   b) If homeowner is detected, unlock the door
## Syetem Structure:
Note: Since we don't have a real door, we will use green LED turned on as unlocking the door and red LED on as alarming.

When there's no one touching the sensor, the touch sensor is always running to wait for a touch
Once touch sensed, camera begins to work and detect whether you are the houseowner(s) for 30 secs
if detected:
   if the houseowners:
      unlock the door(greed LED on for 5 secs)
   if strangers: 
      red LED on
      send a photo of the stranger to houseowners' e-mail
else:                                                      #No face detected within 30 secs
   camera stop running                                     #To save energy and increase running speed
## 1. Test the camera whether it works
   $vcgencmd get_camera
   #if supported = 1 detected = 1: camera connected successfully
   $raspistill -o image.jpg
   #Take a photo named "image.jpg" and saved in "/pi/home"

## 2. Install dlib, opencv, facial_recognition, numpy
   ---------- install necessary libs for dlib, opencv ----------- 
   $sudo apt-get update
   $sudo apt-get install build-essential \
    cmake \
    gfortran \
    git \
    wget \
    curl \
    graphicsmagick \
    libgraphicsmagick1-dev \
    libatlas-dev \
    libavcodec-dev \
    libavformat-dev \
    libboost-all-dev \
    libgtk2.0-dev \
    libjpeg-dev \
    liblapack-dev \
    libswscale-dev \
    pkg-config \
    python3-dev \
    python3-numpy \
    python3-pip \
    zip
   ----------- install lib for raspberry camera ----------- 
   $sudo apt-get install python3-picamera
   $sudo pip3 install --upgrade picamera[array]
   ----------- install dlib ----------- 
   $mkdir -p dlib
   $git clone -b 'v19.6' --single-branch https://github.com/davisking/dlib.git dlib/
   $cd ./dlib
   $sudo python3 setup.py install --compiler-flags "-mfpu=neon"
   ----------install numpy----------- 
   $sudo pip3 install numpy
   ----------install opencv----------- 
Install necessary libs for opencv
   $sudo apt-get install build-essential git cmake pkg-config -y
   $sudo apt-get install libjpeg8-dev -y
   $sudo apt-get install libtiff5-dev -y
   $sudo apt-get install libjasper-dev -y
   $sudo apt-get install libpng12-dev -y
   $sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev -y
   $sudo apt-get install libgtk2.0-dev -y
   $sudo apt-get install libatlas-base-dev gfortran -y

Download opencv
   $cd /home/pi/Downloads
   $wget https://github.com/Itseez/opencv/archive/3.4.0.zip
   $wget https://github.com/Itseez/opencv_contrib/archive/3.4.0.zip

Unzip 
   $cd /home/pi/Downloads
   $unzip opencv-3.4.0.zip
   $unzip opencv_contrib-3.4.0.zip

Compile
   $cd /home/pi/Downloads/opencv-3.4.0
   $mkdir build
   $cd build
   $cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D INSTALL_C_EXAMPLES=ON -D INSTALL_PYTHON_EXAMPLES=ON -D OPENCV_EXTRA_MODULES_PATH=/home/pi/Downloads/opencv_contrib-3.4.0/modules -D BUILD_EXAMPLES=ON -D WITH_LIBV4L=ON PYTHON3_EXECUTABLE=/usr/bin/python3.5 PYTHON_INCLUDE_DIR=/usr/include/python3.5 PYTHON_LIBRARY=/usr/lib/arm-linux-gnueabihf/libpython3.5m.so PYTHON3_NUMPY_INCLUDE_DIRS=/home/pi/.local/lib/python3.5/site-packages/numpy/core/include ..
   $cd /home/pi/Downloads/opencv-3.4.0/build
   $make

---------------------- 
Note: Before installing dlib & opencv, we need to increase swap file size to 1024 and expand filesystem first.

## 3. Run the example code on github(facial_recognition)
## 4. Add touch sensor, LED and connect wires

## Referece 
https://github.com/ageitgey/face_recognition/ for face_recognition github
https://pypi.org/project/face_recognition/ for discription for the functions of facial_recognition libraries
https://www.pyimagesearch.com/2017/05/01/install-dlib-raspberry-pi/ for installation for dlib
https://www.pyimagesearch.com/2018/09/26/install-opencv-4-on-your-raspberry-pi/ for opencv installation

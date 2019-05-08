# ME369P-Group-11

See https://github.com/ageitgey/face_recognition/
See https://pypi.org/project/face_recognition/    discription for the functions of facial_recognition libraries
https://www.pyimagesearch.com/2017/05/01/install-dlib-raspberry-pi/   installation for dlib

1. Test the camera whether it works
$vcgencmd get_camera
if supported = 1 detected = 1: camera connected successfully

Use the following code to take a photo named "image.jpg" and saved in "/pi/home"
$raspistill -o image.jpg

2. Install dlib, opencv, facial_recognition, numpy
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

https://www.pyimagesearch.com/2017/05/01/install-dlib-raspberry-pi/

----------install numpy----------- 
$sudo pip3 install numpy

----------install opencv----------- 
#Install necessary libs for opencv
   $sudo apt-get install build-essential git cmake pkg-config -y
   $sudo apt-get install libjpeg8-dev -y
   $sudo apt-get install libtiff5-dev -y
   $sudo apt-get install libjasper-dev -y
   $sudo apt-get install libpng12-dev -y
   $sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev -y
   $sudo apt-get install libgtk2.0-dev -y
   $sudo apt-get install libatlas-base-dev gfortran -y

#Download opencv
   $cd /home/pi/Downloads
   $wget https://github.com/Itseez/opencv/archive/3.4.0.zip
   $wget https://github.com/Itseez/opencv_contrib/archive/3.4.0.zip

#Unzip 
   $cd /home/pi/Downloads
   $unzip opencv-3.4.0.zip
   $unzip opencv_contrib-3.4.0.zip

#Compile
   $cd /home/pi/Downloads/opencv-3.4.0
   $mkdir build
   $cd build
   $cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D INSTALL_C_EXAMPLES=ON -D INSTALL_PYTHON_EXAMPLES=ON -D OPENCV_EXTRA_MODULES_PATH=/home/pi/Downloads/opencv_contrib-3.4.0/modules -D BUILD_EXAMPLES=ON -D WITH_LIBV4L=ON PYTHON3_EXECUTABLE=/usr/bin/python3.5 PYTHON_INCLUDE_DIR=/usr/include/python3.5 PYTHON_LIBRARY=/usr/lib/arm-linux-gnueabihf/libpython3.5m.so PYTHON3_NUMPY_INCLUDE_DIRS=/home/pi/.local/lib/python3.5/site-packages/numpy/core/include ..
   $cd /home/pi/Downloads/opencv-3.4.0/build
   $make
   
---------------------- 
Note: Before installing dlib & opencv, we need to increase swap file size to 1024 and expand filesystem first.

Referece: 
https://www.jianshu.com/p/56929416b4a1
https://www.pyimagesearch.com/2017/05/01/install-dlib-raspberry-pi/
https://blog.csdn.net/imdyf/article/details/81262488

3. Run the example code on github(facial_recognition)
4. Add touch sensor, LED and connect wires

Program Capabilities:
1.*Not finished yet but hopefully use distance sensor to detect if coming or leaving
2. Open camera and record video
3. Real-time facial recognition between stored photo and camera
4. a)If a stranger is detected it will email a picture to the homeowner
   b) If homeowner is detected unlock the door for 2 seconds
   
Syetem Structure:
Once touch sensed, camera begins to work and detect whether you are the houseowner(s) for 30 secs
if detected:
   if the houseowners:
      unlock the door(greed LED on for 5 secs)
   if strangers: 
      red LED on
      send a photo of the stranger to houseowners' e-mail
else: 
   camera closed and another LED on to indicate that no face detected

(Since we don't have an actual door here, we will use LED_ON as openning the door)

Problem:
1. Our camera can only deteced 2D picture, so people can use houseowner's photo to unlock the door...
2. Camera's viedo/picture sent to raspberry pi has a delay around 2 secs (but tiny delay for recognition)
3. It takes 10-20 secs to open the camera
4. We need around 2 minites to analyze and learn the two photos stored after we run the code.(initializing time are a bit long)
5. Sometimes it recognize other people as the houseowner: need to change some parameters to let it be more accurate: OK, now I think it just cannot recognize Asians well...

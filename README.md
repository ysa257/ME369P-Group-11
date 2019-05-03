# ME369P-Group-11

See https://github.com/ageitgey/face_recognition/
See https://pypi.org/project/face_recognition/    discription for the functions of facial_recognition libraries

1. Test the camera whether it works
2. Download dlib, opencv, facial_recognition, numpy...libs
3. Run the example code on github(facial_recognition)
4. Add motion sensor, led, buzzer...

Program Capabilities:
1.*Not finished yet but hopefully use distance sensor to detect if coming or leaving
2. Open camera and record video
3. Real-time facial recognition between stored photo and camera
4. a)If a stranger is detected it will email a picture to the homeowner
   b) If homeowner is detected unlock the door for 2 seconds
   
Syetem Structure:
once motion detected/touch sensed/infrad sensed, camera begins to work and detect whether you are the houseowner(s) for 10 secs
if detected:
   if yes:
      open the door(LED on for 2 secs)
   if not: 
      Buzzer alarming/send live viedos to the labtop(using ssh)
else: 
   camera closed and another LED on to indicate that no face detected

(Since we don't have an actual door here, we will use LED_ON as openning the door)

Problem:
1. Our camera can only deteced 2D picture, so people can use houseowner's photo to unlock the door...
2. Camera's viedo/picture sent to raspberry pi has a delay around 2 secs (but tiny delay for recognition)
3. It takes 10-20 secs to open the camera
4. We need around 2 minites to analyze and learn the two photos stored after we run the code.(initializing time are a bit long)
5. Sometimes it recognize other people as the houseowner: need to change some parameters to let it be more accurate: OK, now I think it just cannot recognize Asians well...

# ME369P-Group-11

See https://github.com/ageitgey/face_recognition/
See https://pypi.org/project/face_recognition/    discription for the functions of facial_recognition libraries

1. Test the camera whether it works
2. Download dlib, opencv, facial_recognition, numpy...libs
3. Run the example code on github(facial_recognition)
4. Add motion sensor, led, buzzer...

Syetem Structure:
once motion detected/touch sensed/infrad sensed, camera begins to work and detect whether you are the houseowner(s)
if not: Buzzer alarming/send live viedos to the labtop(using ssh)
else: Unlock the door (Since we don't have an actual door here, we will use LED_ON as openning the door)

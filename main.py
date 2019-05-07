import face_recognition
import cv2
import numpy as np
import gpiozero
import time
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders

#set up LEDs and sensor
#green is homeowner and red is not homewowner
green = gpiozero.LED(17) 
red = gpiozero.LED(21)
touch_sensor = gpiozero.Button(19)

#touch sensor function
def sensor_is_touched():
    if touch_sensor.is_pressed: return False
    else: return True
    
#function to determine if homeowner    
def match_control_led(list_of_matches):
    for i in range(len(list_of_matches)):
        if list_of_matches[i] == False:
            flag = 0
        else:
            flag = 1
            break
    if flag:
        red.off()
        green.on()
        time.sleep(1)
        green.off()
        return 1
    else:
        return 0
    
#function for sending an email
def send_an_email(picture):
    to_add = 'kmrussell98@gmail.com'
    from_add = 'kmrussell98@gmail.com'
    subject='Home Security Warning'

    #set-up the email basics 
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = from_add
    msg['To'] = to_add
    msg.preamble = 'test'
    
    #add the picture to an email
    part=MIMEBase('application', 'octet-stream')
    part.set_payload(open(picture, 'rb').read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="person_detected.jpg"') #File name and format name
    msg.attach(part)
    
    #try sending the email
    try:
        s=smtplib.SMTP('smtp.gmail.com', 587) #protocol
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(user = 'kmrussell98@gmail.com', password= '*********') 
        s.sendmail(from_add, to_add, msg.as_string())
    except SMTPException as error:
        print('Error')


# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)
# Load a sample picture and learn how to recognize it.
zjc_image = face_recognition.load_image_file("zjc2.jpg")
zjc_face_encoding = face_recognition.face_encodings(zjc_image)[0]

# Load a second sample picture and learn how to recognize it.
kmr_image = face_recognition.load_image_file("kmr3.jpg")
kmr_face_encoding = face_recognition.face_encodings(kmr_image)[0]

# Create arrays of known face encodings and their names
known_face_encodings = [
    zjc_face_encoding,
    kmr_face_encoding
]
known_face_names = [
    "Joe",
    "Kayla"
]

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    print("No one touch me")
    owner_detected = 0
    if sensor_is_touched():
        count=0 #initialize for sending emails
        print("Someone Outside")
        video_capture = cv2.VideoCapture(0)   # Without this line, the camera with not able to open for the second time.
        
        
        #setup for saving the video
        #fourcc = cv2.VideoWriter_fourcc(*'XVID')
        #out=cv2.VideoWriter('output.avi', fourcc, 20, (640,480))
        
        #If touched, camera open and run for 30 secs, if not keep running to detect whether touched
        first_time = time.time() 
        while True:
            if time.time() - first_time >30:
                print("No houseowner was detected during 30 secs")
                break
            # Grab a single frame of video
            ret, frame = video_capture.read()
            # add frame to the video
            #out.write(frame)
#            if frame.all() == None:
#                print("Error: No frame")
#                break
                
            # Resize frame of video to 1/4 size for faster face recognition processing
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

            # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
            rgb_small_frame = small_frame[:, :, ::-1]

            # Only process every other frame of video to save time
            if process_this_frame:
                # Find all the faces and face encodings in the current frame of video
                face_locations = face_recognition.face_locations(rgb_small_frame)
                face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

                face_names = []
                for face_encoding in face_encodings:
                    # See if the face is a match for the known face(s)
                    matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance = 0.52)
                    #match is a list of [True, True] if detect Obama and Biden
                    #print(matches[0])
                        
                    name = "Unknown"
                        

                    # # If a match was found in known_face_encodings, just use the first one.
                    # if True in matches:
                    #     first_match_index = matches.index(True)
                    #     name = known_face_names[first_match_index]

                    # Or instead, use the known face with the smallest distance to the new face
                    face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                    best_match_index = np.argmin(face_distances)
                    if matches[best_match_index]:
                        name = known_face_names[best_match_index]

                    face_names.append(name)
                    
                    if name=='Unknown' and count==0:
                        cv2.imwrite('intruder.jpg', frame)
                        send_an_email('intruder.jpg')
                        count=+1
                        
                    
#                    print(matches) 
                    owner_detected = match_control_led(matches)
                    
            process_this_frame = not process_this_frame


            # Display the results
            for (top, right, bottom, left), name in zip(face_locations, face_names):
                # Scale back up face locations since the frame we detected in was scaled to 1/4 size
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4

                # Draw a box around the face
                cv2.rectangle(frame, (left, top), (right, bottom), (226, 204, 249), 2)

                # Draw a label with a name below the face
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (226, 204, 249), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

            # Display the resulting image
            cv2.imshow('Video', frame)

            # Hit 'q' on the keyboard to quit!
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            if owner_detected:
                print("Welcome Back Home!!!!!!!!!!!!!!!!!!!!")
                break
            else:
                red.on()

        # Release handle to the webcam
        video_capture.release()
        cv2.destroyAllWindows()
       
    else: continue

import os
import cv2 as cv
import numpy as np
import mediapipe as mp
import math
import serial
from datetime import datetime
from Modules import Manipulator


#ser=serial.Serial('com7',9600)



mp_face_mesh = mp.solutions.face_mesh
flag = True
NOSE_LANDMARK = 1
dest_x, dest_y, dest_y2 = 90, 45, 135
dest = "90,45,135"
cap = cv.VideoCapture(0)

check = True

blue = (255, 0, 0)
green= (0, 255, 0)
red= (0, 0, 255)
white= (255, 255, 255)


font =  cv.FONT_HERSHEY_SIMPLEX

manipulator = Manipulator()


def convert(x, max, min, dest_max, dest_min):
    converted_x = dest_min + (x-min) * ((dest_max-dest_min) / (max - min))
    return converted_x



with mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
) as face_mesh:
    while True:
        check = True
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv.flip(frame, 1)
        rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        img_h, img_w = frame.shape[:2]

        results = face_mesh.process(rgb_frame)
        mask = np.zeros((img_h, img_w), dtype=np.uint8)



        if results.multi_face_landmarks:
            mesh_points=np.array([np.multiply([p.x, p.y], [img_w, img_h]).astype(int)
            for p in results.multi_face_landmarks[0].landmark])
           
            x, y = mesh_points[1]
            left_nose_x, left_nose_y = mesh_points[331]
            right_nose_x, right_nose_y = mesh_points[102]

            x = x - img_w/2
            y = -y + img_h/2

            left_nose_x = left_nose_x - img_w/2
            left_nose_y = -left_nose_y + img_h/2
            right_nose_x = right_nose_x - img_w/2
            right_nose_y = -right_nose_y + img_h/2

                             

            if(x>50 and left_nose_x > 50 and right_nose_x > 50):
                dest_x=dest_x+1
                check = False

            if(x<-50 and left_nose_x < -50 and right_nose_x < -50):
                dest_x=dest_x-1
                check = False

            if(y>50 and left_nose_y > 50 and right_nose_y > 50):
                dest_y=dest_y+1
                check = False

            if(y<-50 and left_nose_y < -50 and right_nose_y < -50):
                dest_y=dest_y-1
                check = False

            dest = str(int(dest_x)) +" " + str(int(dest_y)) +" "+ str(int(dest_y2))
            # print(dest)

            #ser.write(dest.encode('utf-8'))                        


        key = cv.waitKey(1)
       
        if key == ord('p'):
            timeformat = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            filename = timeformat+".png"
            manipulator.remove_bg(frame, os.path.join(os.getcwd(),r'Images',r'NoBack',filename))
        if key == ord('o'):
            timeformat = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            filename = timeformat+".png"
            originpath = os.path.join(os.getcwd(),r'Images',r'Origin',filename)
            cv.imwrite(originpath, frame)
        if key == ord('i'):
            timeformat = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            filename = timeformat+".png"
            manipulator.remove_bg(frame, os.path.join(os.getcwd(),r'Images',r'Chroma',filename),True)

        if check:
            frame = cv.rectangle(frame,(270,290),(370,190),(0,255,0),3)

        else:
            frame = cv.rectangle(frame,(270,290),(370,190),(0,0,255),3)

        if key == ord('q'):
            break

       

        cv.imshow('img', frame)
       
       



cap.release()

cv.destroyAllWindows()
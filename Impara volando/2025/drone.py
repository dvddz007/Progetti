from djitellopy import tello
import cv2
import time
from keyboard import is_pressed
from face_detect import getArea

import os
def connectTello(tellonum):
    ssid = "TELLO-"+tellonum
    return os.system(f'''cmd /c "netsh wlan connect name={ssid}"''')

def initDrone():
    drone = tello.Tello()
    drone.connect()
    print("BATTERY: ", drone.get_battery())
    if drone.get_battery()<10:
        print("BATTERY TOO LOW!!!")
        exit(-1)
    return drone


def sendRcControl(drone, control = [0,0,0,0]):
    return drone.send_rc_control(control[0], control[1], control[2], control[3])


def camera():
    img = drone.get_frame_read().frame
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    cv2.putText(img, f"Battery: {drone.get_battery()}%", (690, 100), cv2.QT_FONT_NORMAL, 1, (50, 240, 255), 2)
    return img


def Controls(d, speed: int, oldControl = [0, 0, 0, 0]):
    control=[0,0,0,0]
    on = False

    if is_pressed("A"): control[0] = -speed
    elif is_pressed("D"): control[0] = speed
    if is_pressed("S"): control[1] = -speed
    elif is_pressed("W"): control[1] = speed

    if is_pressed("DOWN ARROW"): control[2] = -speed
    elif is_pressed("UP ARROW"): control[2] = speed
    if is_pressed("LEFT ARROW"): control[3] = -speed
    elif is_pressed("RIGHT ARROW"): control[3] = speed
    
    if is_pressed("Z") and not d.is_flying: d.takeoff()
    if is_pressed("X") and d.is_flying: d.land()
    
#######
#camera non funziona
#####

    if is_pressed("q"):
        if on:
            drone.stream_on()
            camera()
            on = False
        elif not on:
            drone.streamoff()
            cv2.destroyWindow("Output")
            on = True

    if control != oldControl: 
        print(control)
        sendRcControl(d, control)

    return control


##face = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#connectTello("F0B1D2")
##faceTracking = False
drone = initDrone()
drone.streamon()
print("OK")
#cap = cv2.VideoCapture(0)
control = [0,0,0,0]
while not is_pressed("ESC"):
    control = Controls(drone, 100, control)
    

    img = drone.get_frame_read().frame
    #_, img = cap.read()
    #img = cv2.resize(img, (WIDTH,HEIGHT)) 
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    ##area = getArea(face, img)
    # if area != None:
    ##if area is not None:
        ##if area < 20_000: control[1] = 50
        ##if area > 90_000: control[1] = -50
    #print(control)
    #sendRcControl(drone, control)
    #img, info = findFace(img)
    ##cv2.imshow("Face Capture",img)
    ##cv2.waitKey(1)
    
drone.send_rc_control(0,0,0,0)
drone.land()

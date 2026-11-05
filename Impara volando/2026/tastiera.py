from djitellopy import tello
from time import sleep
import cv2
from keyboard import is_pressed


POTENZA = 50
CONTROLS = [0, 0, 0, 0]


def main() -> int:
    drone = tello.Tello()
    drone.connect()
    print(f"Battery = {drone.get_battery()}")

    drone.streamon()
    while True:
        imgBGR = drone.get_frame_read().frame
        imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)
        cv2.imshow("CAMERA", imgRGB)
        cv2.waitKey(1)

        if is_pressed("Z"):
            print("TAKE OFF")
            drone.takeoff()

        if is_pressed("x"):
            print("LAND")
            drone.land()

        if is_pressed("space"):
            print("STOP DRONE")
            CONTROLS = [0, 0, 0, 0]

        while is_pressed("w"):
            print("AVANTI")
            CONTROLS[1] += POTENZA
        
        while is_pressed("a"):
            print("SINISTRA")
            CONTROLS[0] -= POTENZA
        
        while is_pressed("s"):
            print("INDIETRO")
            CONTROLS[1] -= POTENZA
        
        while is_pressed("d"):
            print("DESTRA")
            CONTROLS[0] += POTENZA
        
        drone.send_rc_control(CONTROLS)

    return 0


if __name__ == "__main__":
    main()


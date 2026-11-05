from djitellopy import tello
from time import sleep
import cv2


def main() -> int:
    drone = tello.Tello()
    drone.connect()
    print(f"Battery = {drone.get_battery()}")

    drone.streamon()
    while True:
        imgBGR = drone.get_frame_read().frame #  restituisce l'immagine in BGR catturata dal drone
        imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB) #  converte l'immagine in RGB
        cv2.imshow("CAMERA", imgRGB) #  crea una finestra. imshow(nome_finestra, immagine_da_mostrare)
        cv2.waitKey(1) #  pausa di 1 secondo per frame
        
    return 0


if __name__ == "__main__":
    main()

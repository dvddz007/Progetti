from djitellopy import tello
from time import sleep


PAUSA = 3
POTENZA = 50


def main() -> int:
    drone = tello.Tello()
    drone.connect()
    print(f"Battery = {drone.get_battery()}")

    drone.takeoff()

    sleep(PAUSA)
    drone.send_rc_control(0, 0, 0, POTENZA)
    sleep(PAUSA)

    drone.land()
    
    return 0


if __name__ == "__main__":
    main()

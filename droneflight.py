from djitellopy import tello
from time import sleep

drone = tello.Tello()
# Drone will take off and move up to proper altitude
drone.takeoff()
drone.move_up(90)
# Drone will move forward 800cm in two calls then sleep
drone.move_forward(400)
drone.move_forward(400)
sleep(.5)
# Drone will turn to the left and continue forward to the landing zone in 500cm
drone.rotate_counter_clockwise(90)
drone.move_forward(500)
sleep(.5)
# Drone will land
drone.land()

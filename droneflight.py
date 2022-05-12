from djitellopy import tello
from time import sleep

drone = tello.Tello()
drone.connect()

# Drone will take off and move up to proper altitude (170cm)
drone.takeoff()
drone.move_up(90)
# Drone will move forward 800cm in two calls then sleep
drone.move_forward(400)
drone.move_forward(400)
sleep(.5)
# Drone will turn to the left 90 degrees and continue forward to the landing zone in 500cm
drone.rotate_counter_clockwise(90)
drone.move_forward(500)
sleep(.5)
# Drone will land in the landing zone
drone.land()

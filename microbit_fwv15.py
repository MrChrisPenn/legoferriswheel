from microbit import *


def stop():
    pin8.write_analog(1023)
    pin12.write_analog(1023)
    display.scroll("stp")

def forward(speed):
    pin8.write_analog(speed)
    pin12.write_digital(0)
    display.scroll(speed)

    
speed = 100
while True:
    if button_b.was_pressed():
        #speed = speed + 20
        forward(300)
        sleep(1000)
        forward(190)
        #if speed == 300:
         #   speed = 0
    if button_a.was_pressed():
        stop()

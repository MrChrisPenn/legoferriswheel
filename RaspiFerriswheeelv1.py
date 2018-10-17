# CamJam EduKit 3 - Robotics
# Worksheet 3 - Motor Test Code

import time  # Import the Time library
from gpiozero import CamJamKitRobot  # Import the GPIO Zero Library CamJam library

from guizero import App, PushButton

Speed = 0

from guizero import App, Text, Combo
from time import sleep

def move_forward(selected_value):
        Speed = float(selected_value)
        print(Speed)
        robot.forward(0.3)
        sleep(1)
        robot.forward(Speed)

def move_backward(selected_value):
        Speed = float(selected_value)
        print(Speed)
        robot.backward(0.3)
        sleep(1)
        robot.backward(Speed)
        
def you_chose_forward(selected_value):
    if selected_value == "0.15":
        move_forward(selected_value)
    elif selected_value == "0.16":
        move_forward(selected_value)

    elif selected_value == "0.17":
        move_forward(selected_value) 
    elif selected_value == "0.18":
        move_forward(selected_value)
        

    elif selected_value == "0.19":
        move_forward(selected_value)

def you_chose_backward(selected_value):
    if selected_value == "0.15":
        move_backward(selected_value)

    elif selected_value == "0.16":
        move_backward(selected_value)
    elif selected_value == "0.17":
        move_backward(selected_value)
    elif selected_value == "0.18":
        move_backward(selected_value)
    elif selected_value == "0.19":
        move_backward(selected_value)
    

robot = CamJamKitRobot()

def Stop():
    robot.stop()
    
app = App()

instructions = Text(app, text="Choose a forward speed")
combo = Combo(app, options=[0.15,0.16,0.17,0.18,0.19], command=you_chose_forward)
combo.width = 60
combo.height = 5
result = Text(app)


instructions = Text(app, text="Choose a backward speed")
combo = Combo(app, options=[0.15,0.16,0.17,0.18,0.19], command=you_chose_backward)
combo.width = 60
combo.height = 5
result = Text(app)


Stop_button = PushButton(app, command=Stop, text="Stop")
Stop_button.width = 20
Stop_button.height = 10


app.display()


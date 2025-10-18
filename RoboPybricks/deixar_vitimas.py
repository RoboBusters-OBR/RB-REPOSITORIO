from config import hub, left_Motor, right_Motor, Drive, UltrassonicoF, timer, Garra, my_colors, sensor_CorD, sensor_CorE, Color
from movimentos_bases import guinada, mover
from pybricks.tools import wait

def fita_prata():
    if sensor_CorD.reflection() > 80 or sensor_CorE.reflection() > 80:
        Drive.straight(50)
        guinada("E", 175, 80)
        hub.ble.broadcast(2)
        wait(600)
        right_Motor.dc(100)
        left_Motor.dc(100)
        wait(200)
        right_Motor.dc(-100)
        left_Motor.dc(-100)
        wait(200)
        right_Motor.dc(100)
        left_Motor.dc(100)
        wait(200)
        right_Motor.dc(-100)
        left_Motor.dc(-100)
        wait(200)
        right_Motor.dc(100)
        left_Motor.dc(100)
        wait(200)
        right_Motor.dc(-100)
        left_Motor.dc(-100)
        wait(200)
        Drive.brake()
        hub.ble.broadcast(5)
        wait(600)
        rint("lxfgsjhd")
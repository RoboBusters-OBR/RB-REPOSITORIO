#resgate_de_vitimas
from config import (
    Garra, Drive, timer, left_Motor, right_Motor,
    sensor_CorD, sensor_CorE, UltrassonicoF, hub, Color 
)
from movimentos_bases import guinada, mover
from pybricks.tools import wait, run_task, multitask
import obstaculos_trajeto
import movimentos_bases
import config

async def move_gripper():
    await Garra.run_angle(1000, 180)
    await Garra.run_angle(1000, -180)

async def sobe_gripper():
    await Garra.run_angle(1000, 180)   

async def main():
    await multitask(Drive.straight(-60), move_gripper())

async def resg():
    await multitask(Drive.straight(-20), move_gripper())    

async def sobe():
    await multitask(Drive.straight(-60), sobe_gripper())        

def identifica_sala():
    from seguimento_de_linha import seguir_Linha, FitaRED, curvabrusca, verifica_verde
    from obstaculos_trajeto import Obstaculo, separar_dados
    if sensor_CorD.reflection() > 80 or sensor_CorE.reflection() > 80  :
        left_Motor.dc(-80)
        right_Motor.dc(-80)
        wait(600)
        Drive.brake()
        Garra.dc(-100)
        wait(1000)
        hub.ble.broadcast("AREA_DE_RESGATE")
        wait(600)
        left_Motor.dc(80)
        right_Motor.dc(80)
        wait(800)
        print("coco babacu")
        fazer_resgate()

def fazer_resgate():
    from seguimento_de_linha import seguir_Linha, verifica_verde, curvabrusca, FitaRED
    from obstaculos_trajeto import rampa,separar_dados,Obstaculo
    parede = 0
    hub.imu.reset_heading(0)
    while True:
        print(UltrassonicoF.distance())
        left_Motor.dc(93)
        right_Motor.dc(90)
        parede = 0
        if UltrassonicoF.distance() < 120 and UltrassonicoF.distance() > 100 :
            timer.reset()
            while True :
                left_Motor.dc(90)
                right_Motor.dc(87)
                if (UltrassonicoF.distance() < 120):
                    parede += 1

                if timer.time()>700 or sensor_CorD.reflection() < 18 and sensor_CorE.reflection() < 18 or hub.imu.heading() < -19 or sensor_CorD.reflection() > 90 and sensor_CorE.reflection() > 90:
                    parede = 0 
                    break
                if (UltrassonicoF.distance() < 120 and hub.imu.heading() > -11 and hub.imu.heading() <11 and parede > 555):
                    break

                if UltrassonicoF.distance() > 140 :
                    parede = 0 
        if (UltrassonicoF.distance() < 120 and hub.imu.heading() > -11 and hub.imu.heading() < 11 and parede > 550  ):
            break 
    if UltrassonicoF.distance() < 120 and hub.imu.heading() > -11 and hub.imu.heading() < 11 and parede > 550 :
        Drive.straight(-100)
        Garra.dc(100)
        wait(1000)
        Drive.straight(-400)
        guinada("E",90,100)
        left_Motor.dc(-100)
        right_Motor.dc(-100)
        wait(400)
        left_Motor.dc(100)
        right_Motor.dc(100)
        wait(600)
        left_Motor.dc(-100)
        right_Motor.dc(-100)
        wait(600)
        Garra.dc(-100)
        wait(1000)
        left_Motor.dc(100)
        right_Motor.dc(100)
        wait(3000)
        Drive.straight(-150)
        Garra.dc(100)
        wait(1000)
        left_Motor.dc(-100)
        right_Motor.dc(-100)
        wait(3000)
        Drive.straight(50)
        guinada("D",90,100)
        Drive.straight(150)
        guinada("E",90,100)
        left_Motor.dc(-100)
        right_Motor.dc(-100)
        wait(400)
        left_Motor.dc(100)
        right_Motor.dc(100)
        wait(600)
        left_Motor.dc(-100)
        right_Motor.dc(-100)
        wait(600)
        Garra.dc(-100)
        wait(1000)
        left_Motor.dc(100)
        right_Motor.dc(100)
        wait(3000)
        Drive.straight(-150)
        Garra.dc(100)
        wait(1000)
        left_Motor.dc(-100)
        right_Motor.dc(-100)
        wait(3000)
        Drive.straight(50)
        guinada("D",90,100)
        Drive.straight(150)
        guinada("E",90,100)
        left_Motor.dc(-100)
        right_Motor.dc(-100)
        wait(400)
        left_Motor.dc(100)
        right_Motor.dc(100)
        wait(600)
        left_Motor.dc(-100)
        right_Motor.dc(-100)
        wait(600)
        Garra.dc(-100)
        wait(1000)
        left_Motor.dc(100)
        right_Motor.dc(100)
        wait(3000)
        Drive.straight(-150)
        Garra.dc(100)
        wait(1000)
        left_Motor.dc(-100)
        right_Motor.dc(-100)
        wait(3000)
        Drive.straight(50)
        guinada("D",90,100)
        Drive.straight(150)
        guinada("E",90,100)
        left_Motor.dc(-100)
        right_Motor.dc(-100)
        wait(400)
        left_Motor.dc(100)
        right_Motor.dc(100)
        wait(600)
        left_Motor.dc(-100)
        right_Motor.dc(-100)
        wait(600)
        Garra.dc(-100)
        wait(1000)
        left_Motor.dc(100)
        right_Motor.dc(100)
        wait(3000)
        Drive.straight(-150)
        Garra.dc(100)
        wait(1000)
        left_Motor.dc(-100)
        right_Motor.dc(-100)
        wait(3000)
        Drive.straight(50)
        guinada("D",90,100)
        Drive.straight(150)
        guinada("E",90,100)
        left_Motor.dc(-100)
        right_Motor.dc(-100)
        wait(400)
        left_Motor.dc(100)
        right_Motor.dc(100)
        wait(600)
        left_Motor.dc(-100)
        right_Motor.dc(-100)
        wait(600)
        Garra.dc(-100)
        wait(1000)
        left_Motor.dc(100)
        right_Motor.dc(100)
        wait(3000)
        Drive.straight(-150)
        Garra.dc(100)
        wait(1000)
        left_Motor.dc(-100)
        right_Motor.dc(-100)
        wait(3000)
        Drive.straight(50)
        guinada("D",90,100)
        Drive.straight(80)
        guinada("E",90,100)
        left_Motor.dc(-100)
        right_Motor.dc(-100)
        wait(400)
        left_Motor.dc(100)
        right_Motor.dc(100)
        wait(600)
        left_Motor.dc(-100)
        right_Motor.dc(-100)
        wait(600)
        Garra.dc(-100)
        wait(1000)
        left_Motor.dc(100)
        right_Motor.dc(100)
        wait(3000)
        Drive.straight(-150)
        Garra.dc(100)
        wait(1000)
        left_Motor.dc(-100)
        right_Motor.dc(-100)
        wait(3000)
        Drive.straight(50)
        guinada("E",85,100)
        while True: 
            left_Motor.dc(100)
            right_Motor.dc(100)
            if sensor_CorD.reflection() > 80 or sensor_CorE.reflection() > 80  :
                left_Motor.dc(100)
                right_Motor.dc(100)
                wait(500)
                guinada("E", 52, 90)
                while True:
                    mover(80)
                    if sensor_CorE.reflection() < 28:
                        break
                while True:
                    seguir_Linha(5, 80)#5, 8
                    verifica_verde()
                    curvabrusca()
                    Obstaculo()
                    rampa()
        
        
        
        
    
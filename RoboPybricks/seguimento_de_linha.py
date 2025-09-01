#seguimento_de_linha

from config import sensor_CorE, sensor_CorD, left_Motor, right_Motor, Drive, timer, Color
from movimentos_bases import mover, guinada
from pybricks.tools import wait
from config import hub 
from obstaculos_trajeto import Obstaculo


def seguir_Linha(KP, velocidade_base):
    erro = (sensor_CorE.reflection()) - (sensor_CorD.reflection()+2) 

    correcao = erro * KP
    esquerda_power = velocidade_base + correcao 
    direita_power = velocidade_base - correcao 

    left_Motor.dc(esquerda_power)
    right_Motor.dc(direita_power)
       
def verifica_verde():
    if sensor_CorE.color() == Color.GREEN or sensor_CorD.color() == Color.GREEN:
        timer.reset()
        while timer.time() < 150 :
            seguir_Linha(1,40)
        Drive.brake()
        if sensor_CorE.color() == Color.GREEN and sensor_CorD.color() == Color.GREEN:
            timer.reset()
            while True:
                if (sensor_CorE.reflection() < 15 or sensor_CorE.reflection() > 25) and sensor_CorE.color() == Color.SILVER:
                    Drive.brake()
                    break
                left_Motor.dc(-70)
                right_Motor.dc(-70)
            wait(200)
            if sensor_CorD.reflection() < 15:
                hub.speaker.beep(500,100)
                left_Motor.dc(100)
                right_Motor.dc(100)
                wait(200)
                Drive.brake()
                while True:
                    mover(100)
                    if sensor_CorE.reflection() < 25:
                        Drive.stop()
                        break   
            elif sensor_CorE.reflection() > 25:
                hub.speaker.beep(500,100)
                left_Motor.dc(90) 
                right_Motor.dc(90) 
                wait(450)
                guinada('E', 200, 100)
                while True:
                    mover(100)
                    if sensor_CorE.reflection() < 20:
                        Drive.stop()
                        break
                Drive.straight(-15)
        if sensor_CorE.color() == Color.GREEN and sensor_CorD.color() != Color.GREEN:
            timer.reset()
            timer.reset()
            while True:
                if (sensor_CorE.reflection() < 15 or sensor_CorE.reflection() > 25) and sensor_CorE.color() != Color.GREEN :
                    Drive.brake()
                    break
                left_Motor.dc(-70)
                right_Motor.dc(-70)
            wait(200)
            if sensor_CorD.reflection() < 15:
                hub.speaker.beep(500,100)
                left_Motor.dc(100)
                right_Motor.dc(100)
                wait(200)
                Drive.brake()
                while True:
                    mover(100)
                    if sensor_CorE.reflection() < 25:
                        Drive.stop()
                        break   
            elif sensor_CorE.reflection() > 25:
                hub.speaker.beep(500,100)
                left_Motor.dc(90) 
                right_Motor.dc(90) 
                wait(450)
                guinada('E', 95, 100)
                while True:
                    mover(100)
                    if sensor_CorE.reflection() < 20:
                        Drive.stop()
                        break
        if sensor_CorD.color() == Color.GREEN and sensor_CorE.color() != Color.GREEN :
            timer.reset()
            timer.reset()
            while True:
                if (sensor_CorD.reflection() < 15 or sensor_CorD.reflection() > 25) and sensor_CorD.color() != Color.GREEN:
                    Drive.brake()
                    break
                left_Motor.dc(-70)
                right_Motor.dc(-70)
            wait(200)
            if sensor_CorD.reflection() < 15:
                hub.speaker.beep(500,100)
                left_Motor.dc(100)
                right_Motor.dc(100)
                wait(200)
                Drive.brake()
                while True:
                    mover(-100)
                    if sensor_CorD.reflection() < 28:
                        Drive.stop()
                        break   
            elif sensor_CorD.reflection() > 25:
                hub.speaker.beep(500,100)
                left_Motor.dc(90) 
                right_Motor.dc(90) 
                wait(450)
                guinada('D', 95, 100)
                while True:
                    mover(-100)
                    if sensor_CorD.reflection() < 28:
                        Drive.stop()
                        break 

def curvabrusca():
    Drive.settings(straight_acceleration=1000)
    if (sensor_CorE.reflection() >= 0 and sensor_CorE.reflection() <= 22) and (sensor_CorD.reflection() >= 20) and sensor_CorD.reflection() <= 45 and (sensor_CorE.color()!= Color.GREEN and sensor_CorD.color()!= Color.GREEN) and hub.imu.tilt()[1] > -9 and hub.imu.tilt()[1] < 9 and hub.imu.tilt()[0] < -1:
        guinada('D', 10, 100)
        Drive.straight(40) 
        Drive.brake()  
        timer.reset()
        hub.imu.reset_heading(0) 
        while True:
            mover(-100)
            if (abs(hub.imu.heading()) >= 99) or (sensor_CorD.reflection() >= 9 and sensor_CorD.reflection() <= 20 )and sensor_CorD.color() != Color.GREEN and sensor_CorE.color() != Color.GREEN:
                Drive.brake()
                break
        if sensor_CorD.reflection() >= 0 and sensor_CorD.reflection() <= 20:
            while True :
                    mover(100)
                    if (sensor_CorE.reflection() >= 30 and sensor_CorD.reflection() >= 30):
                        Drive.brake()
                        break
        
        elif  (hub.imu.heading()> 98) and (sensor_CorD.reflection() >= 40 and sensor_CorE.reflection() >= 40) and sensor_CorD.color() != Color.GREEN and sensor_CorE.color() != Color.GREEN :
            while True :
                mover(100)
                if (sensor_CorE.reflection() >= 9 and sensor_CorE.reflection() <= 20):
                    while True :
                        mover(-100)
                        if (sensor_CorE.reflection() >= 30 and sensor_CorD.reflection() >= 30):
                            Drive.brake()
                            break
                    break
                
    if (sensor_CorD.reflection() >= 0 and sensor_CorD.reflection() <= 22) and (sensor_CorE.reflection() >= 20 and sensor_CorE.reflection() <= 45) and (sensor_CorD.color()!= Color.GREEN and sensor_CorE.color()!= Color.GREEN) and hub.imu.tilt()[1] > -9 and hub.imu.tilt()[1] < 9   :
        guinada('E', 10, 100)
        Drive.straight(40) 
        Drive.brake()  
        timer.reset()
        hub.imu.reset_heading(0) 
        while True:
            mover(100)
            if (abs(hub.imu.heading()) >= 99) or (sensor_CorE.reflection() >= 9 and sensor_CorE.reflection() <= 20) and sensor_CorD.color() != Color.GREEN and sensor_CorE.color() != Color.GREEN:
                Drive.brake()
                break
        if sensor_CorD.reflection() >= 0 and sensor_CorD.reflection() <= 20:
            while True :
                mover(100)
                if (sensor_CorE.reflection() >= 30 and sensor_CorD.reflection() >= 30):
                    Drive.brake()
                    break
        
        elif  (abs(hub.imu.heading())> 98) and (sensor_CorD.reflection() >= 40 and sensor_CorE.reflection() >= 40) and sensor_CorD.color() != Color.GREEN and sensor_CorE.color() != Color.GREEN :
            while True :
                mover(100)
                if (sensor_CorE.reflection() >= 9 and sensor_CorE.reflection() <= 20):
                    while True :
                        mover(-100)
                        if (sensor_CorE.reflection() >= 30 and sensor_CorD.reflection() >= 30):
                            Drive.brake()
                            break
                    break
            
def FitaRED():
    if sensor_CorD.color() == Color.RED or sensor_CorD.color() == Color.RED:
        hub.ble.broadcast(2)
        Drive.stop()
        wait(1000000)

def curvalombada():
    
    if (sensor_CorE.reflection() >= 5 and sensor_CorE.reflection() <= 10) and (sensor_CorD.reflection() >= 17 and sensor_CorD.reflection() <= 43) and (sensor_CorE.color()!= Color.GREEN and sensor_CorD.color()!= Color.GREEN) and hub.imu.tilt()[1] > -9 and hub.imu.tilt()[1] < 9:
        left_Motor.dc(100) 
        right_Motor.dc(100) 
        wait(190) 
        guinada('D', 2, 70)
        Drive.brake() 
        timer.reset() 
        hub.imu.reset_heading(0) 

        while True:
            mover(-80)
            if (abs(hub.imu.heading())> 95) or (sensor_CorD.reflection() >= 9 and sensor_CorD.reflection() <= 20)and sensor_CorD.color() != Color.GREEN and sensor_CorE.color() != Color.GREEN:
                Drive.brake()
                break
        if sensor_CorD.reflection() >= 0 and sensor_CorD.reflection() <= 20:
            guinada('D',5,60)
            Drive.brake()
    
        elif  (abs(hub.imu.heading())> 90) and (sensor_CorD.reflection() >= 40 and sensor_CorE.reflection() >= 40) and sensor_CorD.color() != Color.GREEN and sensor_CorE.color() != Color.GREEN :
            hub.imu.reset_heading(0) 
            while True :
                mover(80)
                if (sensor_CorE.reflection() >= 9 and sensor_CorE.reflection() <= 17):
                    guinada('E',5,65)
                    break
                
    if (sensor_CorD.reflection() >= 5 and sensor_CorD.reflection() <= 10) and (sensor_CorE.reflection() >= 17 and sensor_CorE.reflection() <= 43) and (sensor_CorD.color()!= Color.GREEN and sensor_CorE.color()!= Color.GREEN) and hub.imu.tilt()[1] > -9 and hub.imu.tilt()[1] < 9   :
        left_Motor.dc(100) 
        right_Motor.dc(100) 
        wait(190) 
        Drive.brake() 

        guinada('E', 2, 70)
        Drive.brake()  
        timer.reset()
        hub.imu.reset_heading(0) 
        
        while True:
            mover(80)
            if (abs(hub.imu.heading())> 95) or (sensor_CorE.reflection() >= 9 and sensor_CorE.reflection() <= 20) and sensor_CorD.color() != Color.GREEN and sensor_CorE.color() != Color.GREEN:
                Drive.brake()
                break
            
        if sensor_CorE.reflection() >= 9 and sensor_CorE.reflection() <= 20 :
            Drive.brake()
            
        elif  (abs(hub.imu.heading())> 90) and (sensor_CorD.reflection() >= 40 and sensor_CorE.reflection() >= 40) :
            timer.reset()
            while True :
                mover(-80)
                if (sensor_CorD.reflection() >= 9 and sensor_CorD.reflection() <= 20) and sensor_CorD.color() != Color.GREEN and sensor_CorE.color() != Color.GREEN:               
                    guinada('D',5,60)

                    break
   
#seguimento_de_linha

from config import sensor_CorE, sensor_CorD, left_Motor, right_Motor, Drive, timer, Color
from movimentos_bases import mover, guinada
from pybricks.tools import wait
from config import hub 
def seguir_Linha(KP, velocidade_base):
    erro = (sensor_CorE.reflection()+ 4) - sensor_CorD.reflection() 

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
                if (sensor_CorE.reflection() < 15 or sensor_CorE.reflection() > 25) and sensor_CorE.color() != Color.GREEN :
                    Drive.brake()
                    break
                left_Motor.dc(-70)
                right_Motor.dc(-70)
            wait(200)
            if sensor_CorD.reflection() < 15:
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
    if (sensor_CorE.reflection() >= 5 and sensor_CorE.reflection() <= 22) and (sensor_CorD.reflection() >= 20 and sensor_CorD.reflection() <= 43) and (sensor_CorE.color()!= Color.GREEN and sensor_CorD.color()!= Color.GREEN) and hub.imu.tilt()[1] > -9 and hub.imu.tilt()[1] < 9:
        left_Motor.dc(100) 
        right_Motor.dc(100) 
        wait(190) 
        guinada('D', 25, 100)
        Drive.brake()
        Drive.stop()  
        timer.reset() 
        while True:
            mover(-100)
            if (timer.time() >= 1100) or (sensor_CorD.reflection() >= 9 and sensor_CorD.reflection() <= 17)and sensor_CorD.color() != Color.GREEN and sensor_CorE.color() != Color.GREEN:
                Drive.brake()
                if timer.time() >= 0 and timer.time() <= 300 and sensor_CorD.reflection() >= 9 and sensor_CorD.reflection() <= 15:
                    timer.reset()
                    #guinada('D',2,100)
                    while timer.time() < 190:
                        seguir_Linha(3.9, 69)#3.9, 79 # CURVA  > 5 < 19 AND > 20 < 42
                        FitaRED()
                        Obstaculo()
                break
        if sensor_CorD.reflection() >= 0 and sensor_CorD.reflection() <= 17:
            guinada('D',5,100)
            Drive.straight(-35)
            Drive.brake()
            wait(20)
            timer.reset()
            while timer.time() < 210:
                seguir_Linha(4.2, 70)#3.9, 79 # CURVA  > 5 < 19 AND > 20 < 42
                FitaRED()
                Obstaculo()
                verifica_verde()
            Drive.brake()
            Drive.brake()
            wait(10)
           
            Drive.stop()
            timer.reset()
    
        elif  (timer.time() >= 1100) and (sensor_CorD.reflection() >= 40 and sensor_CorE.reflection() >= 40) and sensor_CorD.color() != Color.GREEN and sensor_CorE.color() != Color.GREEN :
            while True :
                mover(100)
                if (sensor_CorE.reflection() >= 9 and sensor_CorE.reflection() <= 17):
                    guinada('E',5,100)
                    '''left_Motor.dc(-100)
                    right_Motor.dc(-100)
                    wait(200)'''
                    Drive.straight(-35)
                    Drive.brake()
                    wait(20)
                    timer.reset()
                    while timer.time() < 190:
                        seguir_Linha(5, 90)#3.9, 79 # CURVA  > 5 < 19 AND > 20 < 42
                        FitaRED()
                        Obstaculo()
                        verifica_verde()
                    Drive.brake()
                    Drive.brake()
                    wait(10)
                    break
                
    if (sensor_CorD.reflection() >= 5 and sensor_CorD.reflection() <= 22) and (sensor_CorE.reflection() >= 20 and sensor_CorE.reflection() <= 43) and (sensor_CorD.color()!= Color.GREEN and sensor_CorE.color()!= Color.GREEN) and hub.imu.tilt()[1] > -9 and hub.imu.tilt()[1] < 9   :
        left_Motor.dc(100) 
        right_Motor.dc(100) 
        wait(190) 
        Drive.brake() 
        '''if sensor_CorD.reflection() < 30 and sensor_CorE.reflection() < 30 :
            timer.reset()
            while timer.time() < 190:
                seguir_Linha(4.2, 70)#3.9, 79 # CURVA  > 5 < 19 AND > 20 < 42
                FitaRED()
                Obstaculo()
            return 0'''

        guinada('E', 25, 100)
        Drive.brake()  
        timer.reset() 
        while True:
            mover(100)
            if (timer.time() >= 1100) or (sensor_CorE.reflection() >= 9 and sensor_CorE.reflection() <= 17) and sensor_CorD.color() != Color.GREEN and sensor_CorE.color() != Color.GREEN:
                Drive.brake()
                if timer.time() >= 0 and timer.time() <= 300 and sensor_CorE.reflection() >= 9 and sensor_CorE.reflection() <= 17:
                    timer.reset()
                    #guinada('E',2,100)
                    while timer.time() < 190:
                        seguir_Linha(4.2, 70)#3.9, 79 # CURVA  > 5 < 19 AND > 20 < 42
                        FitaRED()
                        Obstaculo()
                break
        if sensor_CorE.reflection() >= 0 and sensor_CorE.reflection() <= 17:
            guinada('E',5,100)
            '''left_Motor.dc(-100)
            right_Motor.dc(-100)
            wait(200)'''
            Drive.straight(-35)
            Drive.brake()
            wait(20)
            timer.reset()
            while timer.time() < 210:
                seguir_Linha(4.2, 70)#3.9, 79 # CURVA  > 5 < 19 AND > 20 < 42
                verifica_verde()
                FitaRED()
                Obstaculo()

            Drive.brake()
            wait(10)
            
            Drive.stop()
            timer.reset()
        elif  (timer.time() >= 1100) and (sensor_CorD.reflection() >= 40 and sensor_CorE.reflection() >= 40) :
            while True :
                mover(-100)
                if (sensor_CorD.reflection() >= 9 and sensor_CorD.reflection() <= 15) and sensor_CorD.color() != Color.GREEN and sensor_CorE.color() != Color.GREEN:               
                    guinada('D',5,100)
                    '''left_Motor.dc(-100)
                    right_Motor.dc(-100)
                    wait(200)'''
                    Drive.straight(-35)
                    Drive.brake()
                    wait(20)
                    timer.reset()
                    while timer.time() < 210:
                        seguir_Linha(4.2, 70)#3.9, 79 # CURVA  > 5 < 19 AND > 20 < 42
                        verifica_verde()
                        FitaRED()
                        Obstaculo()
                    break
                    Drive.brake()
                    Drive.brake()
                    wait(10)
                    '''timer.reset()
                    while timer.time() < 300:
                        seguir_Linha(3.9, 69)#3.9, 79 # CURVA  > 5 < 19 AND > 20 < 42
                        verifica_verde()
                        FitaRED()
                        Obstaculo()'''
                    
                    break
            
def FitaRED():
    if sensor_CorD.color() == Color.RED or sensor_CorD.color() == Color.RED:
        Drive.stop()
        rint("jhzda")
        wait(1000000)

#seguimento_de_linha

from config import sensor_CorE, sensor_CorD, left_Motor, right_Motor, Drive, timer, Color
from movimentos_bases import mover, guinada
from pybricks.tools import wait
from config import hub 
from resgate_de_vitimas import identifica_sala
from obstaculos_trajeto import Obstaculo, rampa, separar_dados
import obstaculos_trajeto
import movimentos_bases
import config



def seguir_Linha(KP, velocidade_base):
    erro = (sensor_CorE.reflection()) - (sensor_CorD.reflection())
    if abs(erro) > 0 and abs(erro) < 2 or abs(erro) >0 and abs(erro)<3 or abs(erro) >0 and abs(erro)<4 or abs(erro) >0 and abs(erro)<5 :
        erro = 0
    correcao = erro * KP
    esquerda_power = velocidade_base + correcao 
    direita_power = velocidade_base - correcao 

    left_Motor.dc(esquerda_power)
    right_Motor.dc(direita_power)
       
def verifica_verde():
    if sensor_CorE.color() == Color.GREEN or sensor_CorD.color() == Color.GREEN:
        timer.reset()
        while timer.time() < 100 :
            seguir_Linha(1,40)
        Drive.brake()
    
        if sensor_CorE.color() == Color.GREEN and sensor_CorD.color() == Color.GREEN:
            timer.reset()
            while True:
                if (sensor_CorE.reflection() < 15 or sensor_CorE.reflection() > 40) and sensor_CorE.color() != Color.GREEN and (sensor_CorE.reflection() < 15 or sensor_CorE.reflection() > 40) and sensor_CorE.color() != Color.GREEN:
                    Drive.brake()
                    break
                left_Motor.dc(-50)
                right_Motor.dc(-50)
            wait(200)
            if sensor_CorD.reflection() < 15:
                hub.speaker.beep(500,100)
                left_Motor.dc(100)
                right_Motor.dc(100)
                wait(200)
                Drive.brake()
                while True:
                    mover(100)
                    if sensor_CorE.reflection() < 40:
                        Drive.stop()
                        break   
            elif sensor_CorE.reflection() > 40:
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

        '''elif  sensor_CorE.color() == Color.GREEN or sensor_CorD.color() == Color.GREEN :
            if sensor_CorE.color() == Color.GREEN :
                guinada("D",2,90)
            if sensor_CorD.color() == Color.GREEN:
                guinada("E",2,90)'''
        
        if sensor_CorE.color() == Color.GREEN and sensor_CorD.color() != Color.GREEN:
            Drive.brake()
            timer.reset()
            timer.reset()
            
            
            while True:
                if (sensor_CorE.reflection() < 15 and sensor_CorE.reflection() > 5 and sensor_CorE.color() != Color.GREEN  or sensor_CorE.reflection() > 40 and sensor_CorE.color() != Color.GREEN ) :
                    Drive.brake()

                    break
                left_Motor.dc(-50)
                right_Motor.dc(-50)
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
            elif sensor_CorE.reflection() > 40:
                hub.speaker.beep(500,100)
                left_Motor.dc(90) 
                right_Motor.dc(90) 
                wait(550)
                guinada('E', 95, 80)
                while True:
                    mover(80)
                    if sensor_CorE.reflection() < 20:
                        Drive.straight(-20)
                        Drive.brake()
                        wait(100)
                        
                        break
        if sensor_CorD.color() == Color.GREEN and sensor_CorE.color() != Color.GREEN :
            Drive.brake()
            hub.speaker.beep(500,100)
            
            timer.reset()

            while True:
                if (sensor_CorD.reflection() < 15 and sensor_CorD.reflection() > 5 and sensor_CorD.color() != Color.GREEN  or sensor_CorD.reflection() > 40 and sensor_CorD.color() != Color.GREEN ) :
                    Drive.brake()
                    break
                left_Motor.dc(-50)
                right_Motor.dc(-50)
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
                        Drive.brake()
            
                        break   
            elif sensor_CorD.reflection() > 40:
                hub.speaker.beep(500,100)
                left_Motor.dc(90) 
                right_Motor.dc(90) 
                wait(550)
                guinada('D', 95, 80)
                while True:
                    mover(-80)
                    if sensor_CorD.reflection() < 28:
                        Drive.straight(-20)
                        Drive.brake()
                        wait(100)
                        break 

def curvabrusca():
    Drive.settings(straight_acceleration=1000)
    """if (sensor_CorD.reflection() <= 20 and sensor_CorE.reflection() <= 20) :
        left_Motor.dc(80)
        right_Motor.dc(80)
        wait(300)"""
    
    if (sensor_CorE.reflection() >= 0 and sensor_CorE.reflection() <= 22) and (sensor_CorD.reflection() >= 0 and sensor_CorD.reflection() <= 40 )and (sensor_CorE.color()!= Color.GREEN and sensor_CorD.color()!= Color.GREEN) and hub.imu.tilt()[0] > -1 and hub.imu.tilt()[0] < 2 and (sensor_CorE.color()!= Color.RED and sensor_CorD.color()!= Color.RED):
        wait(50)
        if sensor_CorD.color()== Color.GREEN or sensor_CorE.color()== Color.GREEN:
            return 0
        guinada('D', 10, 100)
        Drive.straight(45) 
        """if (sensor_CorD.reflection() <= 40 or sensor_CorE.reflection() <= 40) :
            return 0"""
        Drive.brake()  
        timer.reset()
        hub.imu.reset_heading(0) 
        while True:
            mover(-100)
            if (abs(hub.imu.heading()) >= 115) or (sensor_CorD.reflection() >= 0 and sensor_CorD.reflection() <= 25 )and sensor_CorD.color() != Color.GREEN and sensor_CorE.color() != Color.GREEN:
                Drive.brake()
                print(sensor_CorD.reflection())
                break
        if sensor_CorD.reflection() >= 0 and sensor_CorD.reflection() <= 27:
            print("vi linha")
            Drive.brake()
            return 0
        
        elif sensor_CorD.reflection() >= 35 : #(abs(hub.imu.heading()> 80)) and (sensor_CorD.reflection() >= 40 and sensor_CorE.reflection() >= 40) and sensor_CorD.color() != Color.GREEN and sensor_CorE.color() != Color.GREEN 
            print(" nao vi linha")
            hub.imu.reset_heading(0)
            guinada("D",7,70)
            Drive.straight(-25)
            while True :
                mover(100)
                if (sensor_CorD.reflection() >= 9 and sensor_CorD.reflection() <= 20) :
                    Drive.brake()
                    guinada("D",2,80)
                    break
            
               
                
    if (sensor_CorD.reflection() >= 0 and sensor_CorD.reflection() <= 22) and (sensor_CorE.reflection() >= 20 and sensor_CorE.reflection() <= 40) and (sensor_CorD.color()!= Color.GREEN and sensor_CorE.color()!= Color.GREEN) and hub.imu.tilt()[0] > -1 and hub.imu.tilt()[0] < 2 and (sensor_CorE.color()!= Color.RED and sensor_CorD.color()!= Color.RED) :
        wait(50)
        if sensor_CorD.color()== Color.GREEN or sensor_CorE.color()== Color.GREEN:
            return 0
        guinada('E', 10, 100)
        Drive.straight(45) 
        """if (sensor_CorD.reflection() <= 40 or sensor_CorE.reflection() <= 40) :
            return 0"""
        Drive.brake()  
        timer.reset()
        hub.imu.reset_heading(0) 
        while True:
            mover(100)
            if (abs(hub.imu.heading()) >= 115) or (sensor_CorE.reflection() >= 0 and sensor_CorE.reflection() <= 25) and sensor_CorD.color() != Color.GREEN and sensor_CorE.color() != Color.GREEN:
                Drive.brake()
                print(sensor_CorE.reflection())
                break
        if sensor_CorD.reflection() >= 0 and sensor_CorD.reflection() <= 27:
            print("vi linha direita")
            return 0
        
        
        elif  sensor_CorE.reflection() >= 35:
            guinada("E",7,70)
            Drive.straight(-25)
            print(" nao vi linha")
            hub.imu.reset_heading(0)
            while True :
                mover(-100)
                if (sensor_CorE.reflection() >= 9 and sensor_CorE.reflection() <= 20) :
                    guinada("D",2,80)
                    Drive.brake()
                    break
                
            
def FitaRED():
    if sensor_CorD.color() == Color.RED or sensor_CorD.color() == Color.RED:
        hub.ble.broadcast(2)
        Drive.stop()
        wait(1000000)

def curvalombada():
    
    if (sensor_CorE.reflection() >= 5 and sensor_CorE.reflection() <= 10) and (sensor_CorD.reflection() >= 17 and sensor_CorD.reflection() <= 43) and (sensor_CorE.color()!= Color.GREEN and sensor_CorD.color()!= Color.GREEN) and hub.imu.tilt()[1] > -9 and hub.imu.tilt()[1] < 9: 
        guinada('D', 10, 70)
        Drive.straight(40)
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
        guinada('E', 10, 70)
        Drive.straight(40)
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

def seguir_Linha2(KP, velocidade_base):
    # Calcula o erro da linha
    erro = sensor_CorE.reflection() - (sensor_CorD.reflection() + 2)

    # Correção proporcional
    correcao = erro * KP

    # Limita a correção aos ângulos do IMU (-15 a 15)
    correcao = max(-15, min(15, correcao))

    # Calcula potência final dos motores
    esquerda_power = velocidade_base + correcao
    direita_power = velocidade_base - correcao

    # Limita potência para não passar do máximo do motor
    esquerda_power = max(0, min(velocidade_base, esquerda_power))
    direita_power = max(0, min(velocidade_base, direita_power))

    # Envia para os motores
    left_Motor.dc(esquerda_power)
    right_Motor.dc(direita_power)

def mapp(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def identificanada():
    timer.reset()
    preto = 0
    if sensor_CorD.reflection() > 55 and sensor_CorE.reflection()> 55  :
        preto = 0
        while True:
            seguir_Linha(5, 80)#5, 80
            curvabrusca()
            verifica_verde()
            FitaRED()
            Obstaculo()
            rampa()
            identifica_sala()
            if preto >= 1:
                break
            if sensor_CorD.reflection() <53 or sensor_CorE.reflection()<53 :
                preto += 1
                break
            print(preto)
            if preto == 0 and timer.time()>750  :
                while True :
                    left_Motor.dc(-70)
                    right_Motor.dc(-70)
                    if sensor_CorD.reflection()< 49 or  sensor_CorE.reflection()< 49 :
                        timer.reset()
                        while not timer.time()>2100 or sensor_CorD.reflection()< 40 or  sensor_CorE.reflection()< 40:
                            seguir_Linha(5,45)
                            verifica_verde()
                            FitaRED()
                            Obstaculo()
                            rampa()
                            identifica_sala()
                            if sensor_CorD.reflection()< 40 or  sensor_CorE.reflection()< 40:
                                return 0
                        """Drive.straight(20)
                        while not sensor_CorD.reflection()< 30:
                            mover(-80)
                        Drive.straight(-20)
                        break
                    if sensor_CorE.reflection()< 35:
                        Drive.straight(20)
                        while not sensor_CorE.reflection()< 30:
                            mover(80)
                        Drive.straight(-20)
                        break"""
                
                '''while True:
                    #guinada("D", 35, 100)
                    timer.reset()
                    achado = 0
                    while True :

                        if achado == 1:
                            return 0
                        mover(-80)
                        if sensor_CorD.reflection()< 25 or sensor_CorE.reflection()< 25 or timer.time()>1100:
                            if sensor_CorD.reflection()< 28 or sensor_CorE.reflection()< 28 :
                                Drive.brake()
                                achado += 1
                                return 0

                            elif sensor_CorD.reflection()> 20 and sensor_CorE.reflection()> 20 and timer.time()>1000   : 
                                timer.reset()
                                Drive.straight(20)
                                while True :
                            
                                    mover(80)
                                    if sensor_CorD.reflection()< 25 or sensor_CorE.reflection()< 25 or timer.time()>1500:
                                        break
                                
                                if sensor_CorD.reflection()< 28 or sensor_CorE.reflection()< 28 :
                                    Drive.brake()
                                    achado += 1
                                    return 0
                                else:
                                    timer.reset()
                                    Drive.straight(20)
                                    
                            break
                                
                                    
                        if achado == 1:
                            return 0'''

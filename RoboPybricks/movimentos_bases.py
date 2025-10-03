# -*- coding: utf-8 -*-
#movimentos_bases
from config import left_Motor, right_Motor, Drive, hub, Axis
from pybricks.tools import wait
def mover(GIRO):
    left_Motor.dc(GIRO)
    right_Motor.dc(-GIRO)

def guinada(LADO, GRAUS, VELOCIDADE):  
    hub.imu.reset_heading(0)
    if LADO == 'D':
        while True:
            mover(VELOCIDADE)
            if hub.imu.heading() >= GRAUS:
                Drive.brake()
                break
    else:
        while True:
            mover(-VELOCIDADE)
            if hub.imu.heading() <= -GRAUS:
                Drive.brake()
                break

"""def girar_absoluto(velocidade):

   Gira o robô até um ângulo absoluto 'destino' usando IMU.
    - direita = negativo
    - esquerda = positivo
    Compensa qualquer erro automaticamente.
    
    while True:
        

        if hub.imu.rotation(Axis.Z, calibrated=True) <=2 and hub.imu.rotation(Axis.Z, calibrated=True) >=-2:
            Drive.brake()
            break  # chegou no destino

        if hub.imu.rotation(Axis.Z, calibrated=True) <=0:         # precisa girar para direita
            left_Motor.dc(-velocidade)
            right_Motor.dc(velocidade)
        elif  hub.imu.rotation(Axis.Z, calibrated=True) >=0:
            left_Motor.dc(velocidade)
            right_Motor.dc(-velocidade)


    left_Motor.stop()
    right_Motor.stop()"""
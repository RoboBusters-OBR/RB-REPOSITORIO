#movimentos_bases
from config import left_Motor, right_Motor, Drive

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

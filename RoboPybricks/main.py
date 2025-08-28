

from config import sensor_CorE, sensor_CorD, Garra,  left_Motor, right_Motor,sensor_CorD, sensor_CorE,UltrassonicoF, Color
from seguimento_de_linha import seguir_Linha, verifica_verde, curvabrusca, FitaRED
from resgate_de_vitimas import identifica_sala
from obstaculos_trajeto import  Obstaculo, rampa, separar_dados
from pybricks.tools import wait
from pybricks.pupdevices import Motor

Garra.dc(100)
wait(1500)
while True:
    
    print(UltrassonicoF.distance(), separar_dados("I"))
    '''if sensor_CorD.color() == Color.SILVER and sensor_CorE.color() == Color.SILVER and sensor_CorD.reflection() >= 36 and sensor_CorD.reflection() <= 42 and sensor_CorE.reflection() >= 36 and sensor_CorE.reflection() <=42  :
        Drive.brake()
        wait(2000)   '''
    identifica_sala()
    seguir_Linha(5, 80)#5, 80
    curvabrusca()
    verifica_verde()
    FitaRED()
    Obstaculo()
    rampa()

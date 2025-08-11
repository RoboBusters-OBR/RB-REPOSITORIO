

from config import sensor_CorE, sensor_CorD, Garra
from seguimento_de_linha import seguir_Linha, verifica_verde, curvabrusca, FitaRED
from resgate_de_vitimas import identifica_sala
from obstaculos_trajeto import  Obstaculo, rampa
from pybricks.tools import wait
from pybricks.pupdevices import Motor

Garra.dc(100)
wait(1500)
while True:
    
    identifica_sala()
    seguir_Linha(5, 100)
    curvabrusca()
    verifica_verde()
    FitaRED()
    Obstaculo()
    rampa()

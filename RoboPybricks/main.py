
from config import sensor_CorE, sensor_CorD
from seguimento_de_linha import seguir_Linha, verifica_verde, curvabrusca, FitaRED
from resgate_de_vitimas import identifica_sala
from obstaculos_trajeto import  Obstaculo, rampa

cinza = 0

while True:
    if sensor_CorD.reflection() > 90:
        cinza = 1
    if sensor_CorE.reflection() > 90:
        cinza = 1

    identifica_sala()
    seguir_Linha(5, 80)
    curvabrusca()
    verifica_verde()
    FitaRED()
    Obstaculo()
    rampa()

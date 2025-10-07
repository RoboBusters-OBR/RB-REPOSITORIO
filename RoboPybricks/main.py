

from config import sensor_CorE, sensor_CorD, Garra,  left_Motor, right_Motor,sensor_CorD, sensor_CorE,UltrassonicoF, Color,timer,hub, Axis
from seguimento_de_linha import seguir_Linha, verifica_verde, curvabrusca, FitaRED,identificanada
from resgate_de_vitimas import identifica_sala
from obstaculos_trajeto import  Obstaculo, rampa, separar_dados
from pybricks.tools import wait
from pybricks.pupdevices import Motor

Garra.dc(100)
wait(1000)
Garra.stop()



while True:
  seguir_Linha(5, 80)#5, 80
  curvabrusca()
  verifica_verde()
  FitaRED()
  Obstaculo()
  rampa()
  identifica_sala()
  identificanada()
  print(sensor_CorD.reflection(),sensor_CorE.reflection())
  


    
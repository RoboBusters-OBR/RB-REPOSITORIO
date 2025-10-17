

from config import sensor_CorE, sensor_CorD, Garra,  left_Motor, right_Motor,sensor_CorD, sensor_CorE,UltrassonicoF, Color,timer,hub, Axis,Drive
from seguimento_de_linha import seguir_Linha, verifica_verde, curvabrusca, FitaRED,identificanada
from resgate_de_vitimas import identifica_sala
from obstaculos_trajeto import  Obstaculo, rampa, separar_dados
from pybricks.tools import wait
from pybricks.pupdevices import Motor
from pybricks.parameters import Stop
from movimentos_bases import guinada

Garra.run_target(500, 0,then = Stop.BRAKE,wait = False )
Drive.stop()
wait(1000)
while True :
  Drive.brake()
  if sensor_CorE.color() != Color.GREEN and sensor_CorD.color() != Color.GREEN :
    break
while True:
  seguir_Linha(5, 80)#5, 8
  verifica_verde()
  curvabrusca()
  FitaRED()
  Obstaculo()
  rampa()
  identifica_sala()
  #identificanada()
  print(sensor_CorE.reflection(),sensor_CorD.reflection())
  #print(hub.imu.tilt()[0])
  
# -*- coding: utf-8 -*-
# config.py
from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from pybricks.parameters import Axis
from pybricks.tools import multitask, run_task

# Inicializa o hub com canal de comunicação
hub = InventorHub(top_side=Axis.Z, front_side=Axis.Y, broadcast_channel=11, observe_channels=[41])

# Motores
Garra = Motor(Port.F)
left_Motor = Motor(Port.D, Direction.COUNTERCLOCKWISE)
right_Motor = Motor(Port.B)

# DriveBase (roda e eixo)
Drive = DriveBase(left_Motor, right_Motor, wheel_diameter=31, axle_track=140)

# Temporizador
timer = StopWatch()
timer.reset()

# Sensores de cor
sensor_CorE = ColorSensor(Port.A)
sensor_CorD = ColorSensor(Port.C)

# Sensores ultrassônicos
UltrassonicoF = UltrasonicSensor(Port.E)

# Definição de cores personalizadas
Color.BLACK = Color(h=220, s=34, v=20)#Drive.use_gyro(True)
Color.GREEN = Color(h=176, s=71, v=24)#176,71,24
Color.WHITE = Color(h=200, s=15, v=98)
Color.CINZA = Color(h=0, s=24, v=55)
Color.RED = Color(h=340, s=80, v=55)
Color.SILVER = Color(h=210, s=27, v=70)
# Lista de cores detectáveis
my_colors = (Color.GREEN, Color.RED, Color.WHITE, Color.BLACK, Color.CINZA,Color.SILVER)
sensor_CorD.detectable_colors(my_colors)
sensor_CorE.detectable_colors(my_colors)

# Inicialização de leitura de cor na superfície
sensor_CorE.color(surface=True)

# Variável auxiliar para contagem de cantos verdes
canto_verde = 0

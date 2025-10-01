from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from pybricks.parameters import Axis
from pybricks.tools import multitask, run_task

timer = StopWatch()
hub = InventorHub(top_side=Axis.Z, front_side=Axis.Y,broadcast_channel=2, observe_channels=[1])
CorD = ColorSensor(Port.A)
UltrassonicoL = UltrasonicSensor(Port.C)
cancelaE = Motor(Port.F)

Color.GREEN = Color(h=146, s=62, v=17)
Color.GRENL = Color(h=120, s=64, v=1)
Color.RED = Color(h=350, s=87, v=31)
Color.REDL = Color(h = 352, s=91, v=5)

my_colors1 = (Color.GREEN, Color.REDL, Color.GRENL, Color.RED)


CorD.detectable_colors(my_colors1)

cancelaE.run_target(700, 100)

while True:
    cancela = hub.ble.observe(1)
    if cancela == 3 : #Abrir verde
        cancelaE.run_target(700, 100)     
        cancela == 0 
    if cancela == 2 : #Abrir verde
        cancelaE.dc(100)
        wait(1000)
        cancelaE.dc(-100)
        cancela == 0   
    
    if hub.ble.observe(1) == 'AREA_DE_RESGATE' :
        cancelaE.run_target(700, 100)
        cancelaE.run_target(700, 70)   
        while True:

            tuplaultra = UltrassonicoL.distance()
            hub.ble.broadcast(tuplaultra)
            
            cancela = hub.ble.observe(1)
            cancelaE.dc(-100)
            if cancela == 2 : #Abrir verde
                cancelaE.dc(100)
                wait(1000)
                cancelaE.dc(-100)
                cancela == 0  
            if cancela == 5 : 
                cancelaE.dc(-100)     
                cancelaE.stop()
                cancela == 0 
            if cancela == 3 : 
                cancelaE.run_target(700, 100)     
                cancelaE.stop()
                cancela == 0 
            print("ultra")

            if hub.ble.observe(1) == "COR" :
                while True:
                    if hub.ble.observe(1) == "PARAR" :
                        break
                    tuplacor = str(CorD.color())
                    hub.ble.broadcast(tuplacor)
                    print("so cor")
                    print(tuplacor)
                    


    else:
        if cancela == 3 : #Abrir verde
            cancelaE.run_target(700, 100)     
            cancela == 0 

        if cancela == 2 : #Abrir verde
            cancelaE.dc(100)
            wait(1000)
            cancelaE.dc(-100)
            cancela == 0  
        print("SÓ DISTANCIA")

        tuplaultraa = UltrassonicoL.distance()

        print(tuplaultraa)
        hub.ble.broadcast(tuplaultraa)
       
    
    

 

 
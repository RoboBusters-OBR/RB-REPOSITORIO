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


Color.GREEN = Color(h=150, s=75, v=7)
Color.WHITE = Color(h=200, s=13, v=40)
Color.NADA = Color(h=210, s=27, v=9)
Color.RED = Color(h=352, s=87, v=30)
Color.NAO = Color(h = 0, s=86, v=3)

my_colors1 = (Color.GREEN, Color.RED, Color.WHITE, Color.NADA, Color.NAO )


CorD.detectable_colors(my_colors1)

cancelaE.run_target(700, 100)

while True:
    cancela = hub.ble.observe(1)
    if cancela == 3 : #Abrir verde
        cancelaE.run_target(700, 100)     
        cancelaE.stop()
        cancela == 0  
    
    if hub.ble.observe(1) == 'AREA_DE_RESGATE' :
        cancelaE.run_target(700, 100)
        cancelaE.run_target(700, 80)   
        while True:
            tuplaultra = UltrassonicoL.distance()
            hub.ble.broadcast(tuplaultra)

            cancela = hub.ble.observe(1)
            
            if cancela == 2 : #Abrir verde
                cancelaE.run_target(700, 180)
                wait(1000)
                cancelaE.run_target(700, 75)     
                cancelaE.stop()
                cancela == 0  
            if cancela == 0 : 
                cancelaE.run_target(700, 75)     
                cancelaE.stop()
                cancela == 0 
            if cancela == 3 : #Abrir verde
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
            cancelaE.stop()
            cancela == 0 
        print("SÓ DISTANCIA")
        #tuplacor = str(CorD.color())
        tuplaultra = UltrassonicoL.distance()

        #hub.ble.broadcast(tuplacor)
        hub.ble.broadcast(tuplaultra)

    
       
    
    

 

 
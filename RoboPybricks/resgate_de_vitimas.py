#resgate_de_vitimas
from config import (
    Garra, Drive, timer, left_Motor, right_Motor,
    sensor_CorD, sensor_CorE, UltrassonicoF, hub, Color 
)
from movimentos_bases import guinada, mover
from pybricks.tools import wait, run_task, multitask
import obstaculos_trajeto
import movimentos_bases
import config

async def move_gripper():
    await Garra.run_angle(1000, 180)
    await Garra.run_angle(1000, -180)

async def sobe_gripper():
    await Garra.run_angle(1000, 180)   

async def main():
    await multitask(Drive.straight(-60), move_gripper())

async def resg():
    await multitask(Drive.straight(-20), move_gripper())    

async def sobe():
    await multitask(Drive.straight(-60), sobe_gripper())        

def identifica_sala():
    from seguimento_de_linha import seguir_Linha, FitaRED, curvabrusca, verifica_verde
    from obstaculos_trajeto import Obstaculo, separar_dados
    if sensor_CorD.reflection() > 80 or sensor_CorE.reflection() > 80  :
        left_Motor.dc(80)
        right_Motor.dc(80)
        wait(600)
        hub.ble.broadcast("AREA_DE_RESGATE")
        print("coco babacu")
        fazer_resgate()

def fazer_resgate():
    from seguimento_de_linha import seguir_Linha, verifica_verde, curvabrusca, FitaRED
    from obstaculos_trajeto import rampa,separar_dados,Obstaculo
    Color.BLACK = Color(h=210, s=32, v=18)
    Color.GREEN = Color(h=176, s=71, v=24)
    Color.WHITE = Color(h=200, s=15, v=98)
    Color.CINZA = Color(h=0, s=24, v=55)
    Color.RED = Color(h=340, s=80, v=55)
    Color.SILVER = Color(h=210, s=27, v=70)

    # Lista de cores detectáveis
    my_colors = (Color.GREEN, Color.RED, Color.WHITE, Color.BLACK, Color.CINZA, Color.SILVER)
    sensor_CorD.detectable_colors(my_colors)
    sensor_CorE.detectable_colors(my_colors)
    timer.reset()
    Drive.straight(60)
    quant_meio = 0
    while True:
        if any(numero < 200 for numero in separar_dados('I')):
            print(separar_dados("I"))
            leitura_ultra = 50
        if any(numero > 200 for numero in separar_dados('I')):
            print(separar_dados("I"))

            leitura_ultra = 100
        if timer.time() > 1200:
            break
    if leitura_ultra == 50:  # verifica se esta encostado na parede
        Drive.straight(70)
        guinada("E", 90, 100)
        left_Motor.dc(-100)
        right_Motor.dc(-100)
        wait(1800)
        left_Motor.dc(70)
        right_Motor.dc(70)
        wait(400)
        Drive.brake
        guinada("D", 88, 90)
        Garra.dc(-90)
        wait(1500)
        quant_meio = 1
    elif leitura_ultra == 100:  # se nao esta encostado
        left_Motor.dc(80)
        right_Motor.dc(80)
        wait(300)
        Drive.brake()
        guinada("D", 89, 90)
        Drive.brake()
        Garra.dc(-90)
        wait(1200)
        Drive.straight(-90)
        Garra.dc(-90)
        wait(1500)
        quant_meio = 1
    timer.reset()
    canto_verde = 0
    canto_verde_alinhamento = 0
    varrer_meio = 0
    canto_vermelho = 0
    hub.imu.reset_heading(0)
    parede = 0
    abudega = 0
    while True:

        print(canto_verde)

        if canto_verde == 2:
            break
        Drive.straight(30,wait = False )
        print(separar_dados('I'))
        print("DEIXANDO")
        if any(numero < 300 for numero in separar_dados('I')) and UltrassonicoF.distance()>= 200:
            Drive.straight(50)
            Drive.stop()
            wait(200)
            if any(numero < 300 for numero in separar_dados('I')) and UltrassonicoF.distance()>= 200:
                print(separar_dados('I'))
                if varrer_meio == quant_meio and any(numero < 300 for numero in separar_dados('I')):
                    Drive.straight(40)
                    guinada("E", 85, 100)
                    left_Motor.dc(-100)
                    right_Motor.dc(-100)
                    wait(3000)
                    left_Motor.dc(100)
                    right_Motor.dc(95)
                    wait(2350)
                    left_Motor.dc(-100)
                    right_Motor.dc(-100)
                    wait(2450)
                    Drive.straight(25)
                    guinada("D", 89, 100)
                    hub.imu.reset_heading(0)
                    varrer_meio += 1
                elif varrer_meio != quant_meio and any(numero < 300 for numero in separar_dados('I')):
                    if canto_vermelho == 1:
                        print("vermelho alinha")
                        Drive.straight(40)
                        guinada("E", 85, 100)
                        left_Motor.dc(-100)
                        right_Motor.dc(-100)
                        wait(3000)
                        left_Motor.dc(100)
                        right_Motor.dc(100)
                        wait(2350)
                        left_Motor.dc(-100)
                        right_Motor.dc(-100)
                        wait(2450)
                        Drive.straight(25)
                        guinada("D", 89, 100)
                        hub.imu.reset_heading(0)
                        varrer_meio += 1
                        canto_vermelho += 1
                    elif canto_verde_alinhamento == 1 and any(numero < 300 for numero in separar_dados('I')):
                        print("verde alinha")
                        Drive.straight(40)
                        guinada("E", 85, 100)
                        left_Motor.dc(-100)
                        right_Motor.dc(-100)
                        wait(3000)
                        left_Motor.dc(100)
                        right_Motor.dc(100)
                        wait(2350)
                        left_Motor.dc(-100)
                        right_Motor.dc(-100)
                        wait(2450)
                        Drive.straight(25)
                        guinada("D", 89, 100)
                        hub.imu.reset_heading(0)
                        varrer_meio += 1
                        canto_verde_alinhamento += 1
                    elif any(numero < 300 for numero in separar_dados('I')):    
                        Drive.straight(40)
                        guinada("E", 85, 100)
                        left_Motor.dc(-100)
                        right_Motor.dc(-100)
                        wait(1500)
                        Drive.straight(40)
                        left_Motor.dc(-100)
                        right_Motor.dc(-100)
                        wait(2800)
                        Drive.straight(25)
                        guinada("D", 89, 100)
                        hub.imu.reset_heading(0)
                        varrer_meio += 1  
            else :
                print("segue")     
        while True:
            print(UltrassonicoF.distance())
            left_Motor.dc(93)
            right_Motor.dc(90)
            parede = 0
            if UltrassonicoF.distance() < 120 and UltrassonicoF.distance() > 100 :
                timer.reset()
                while True :
                    left_Motor.dc(90)
                    right_Motor.dc(87)
                    if (UltrassonicoF.distance() < 120):
                        parede += 1

                    if timer.time()>700 or sensor_CorD.reflection() < 18 and sensor_CorE.reflection() < 18 or hub.imu.heading() < -19 or sensor_CorD.reflection() > 90 and sensor_CorE.reflection() > 90:
                        parede = 0 
                        break
                    if (UltrassonicoF.distance() < 120 and hub.imu.heading() > -11 and hub.imu.heading() <11 and parede > 555):
                        break

                    if UltrassonicoF.distance() > 140 :
                        parede = 0 
            if (UltrassonicoF.distance() < 120 and hub.imu.heading() > -11 and hub.imu.heading() < 11 and parede > 550  or
                    (sensor_CorD.reflection() < 18 and sensor_CorE.reflection() < 18) or
                    hub.imu.heading() < -19 or
                    (sensor_CorD.reflection() > 90 and sensor_CorE.reflection() > 90) ):
                print(hub.imu.heading())
                print(separar_dados('S'))
                Drive.brake()
                break 
        if UltrassonicoF.distance() < 120 and hub.imu.heading() > -11 and hub.imu.heading() < 11 and parede > 550 :
            print("viu parede")
            left_Motor.dc(100)
            right_Motor.dc(100)
            wait(200)
            run_task(main())
            left_Motor.dc(100)
            right_Motor.dc(100)
            wait(300)
            left_Motor.dc(-100)
            right_Motor.dc(-100)
            wait(250)
            left_Motor.dc(100)
            right_Motor.dc(100)
            wait(250)
            left_Motor.dc(100)
            right_Motor.dc(100)
            wait(300)
            Drive.brake()
            run_task(sobe())
            left_Motor.dc(100)
            right_Motor.dc(100)
            wait(1050)
            right_Motor.dc(-90)
            wait(200)
            Drive.brake()
            left_Motor.dc(-90)
            wait(200)
            left_Motor.dc(-100)
            right_Motor.dc(-100)
            wait(80)
            guinada("E", 82, 100)
            Drive.brake()
            Garra.dc(-100)
            wait(2000)
            Drive.brake()
            hub.imu.reset_heading(0)         
        if (sensor_CorD.reflection() < 18 and sensor_CorE.reflection() < 18):
            print("viu saida")
            Garra.dc(100)
            wait(1200)
            left_Motor.dc(-100)
            right_Motor.dc(-100)
            wait(300)
            guinada("E", 85, 80)
            Drive.brake()
            Garra.dc(-100)
            wait(1200)
            Drive.straight(200)
            hub.imu.reset_heading(0)
        if hub.imu.heading() < -18:
            Drive.brake()
            timer.reset()
            hub.ble.broadcast("COR")
            hub.ble.broadcast("COR")
            abudega += 1
            while timer.time() < 1100:
                

                if any(item.startswith("Color.GREEN") for item in separar_dados("S")) or any(item.startswith("Color.GRENL") for item in separar_dados("S")) or any(item.startswith("Color.GRENLL") for item in separar_dados("S")) and abudega > 2:
                    abudega = 0
                    hub.ble.broadcast("PARAR")
                    print("Viu verde")
                    left_Motor.dc(60)
                    right_Motor.dc(60)
                    wait(700)
                    Drive.brake()
                    guinada("E", 5, 80)
                    run_task(resg())
                    '''Garra.dc(100)
                    wait(1100)
                    Garra.dc(-100)
                    wait(900)'''
                    Drive.straight(50)
                    Garra.dc(100)
                    wait(1200)
                    guinada("E", 90, 100)
                    left_Motor.dc(-100)
                    right_Motor.dc(-100)
                    wait(500)
                    left_Motor.dc(100)
                    right_Motor.dc(100)
                    wait(500)
                    left_Motor.dc(-100)
                    right_Motor.dc(-100)
                    wait(500)
                    hub.ble.broadcast(2)
                    wait(600)
                    Garra.dc(-100)
                    wait(1100)
                    left_Motor.dc(100)
                    right_Motor.dc(100)
                    wait(100)
                    left_Motor.dc(-100)
                    right_Motor.dc(-100)
                    wait(200)
                    left_Motor.dc(100)
                    right_Motor.dc(100)
                    hub.ble.broadcast(0)
                    wait(100)
                    left_Motor.dc(-100)
                    right_Motor.dc(-100)
                    wait(200)
                    left_Motor.dc(100)
                    right_Motor.dc(100)
                    wait(2100)
                    Drive.brake()
                    Garra.dc(100)
                    wait(1200)
                    Garra.brake()
                    wait(200)
                    Garra.dc(100)
                    wait(1200)
                    left_Motor.dc(-100)
                    right_Motor.dc(-100)
                    wait(3000)
                    left_Motor.dc(100)
                    right_Motor.dc(100)
                    wait(500)
                    left_Motor.dc(-100)
                    right_Motor.dc(-100)
                    wait(500)
                    hub.ble.broadcast(2)
                    Garra.dc(-100)
                    wait(1100)
                    wait(400)
                    hub.ble.broadcast(0)
                    left_Motor.dc(100)
                    right_Motor.dc(100)
                    wait(100)
                    left_Motor.dc(-100)
                    right_Motor.dc(-100)
                    wait(200)
                    left_Motor.dc(100)
                    right_Motor.dc(100)
                    wait(100)
                    left_Motor.dc(-100)
                    right_Motor.dc(-100)
                    wait(100)
                    Garra.dc(100)
                    wait(1000)
                    hub.ble.broadcast(0)
                    left_Motor.dc(0)
                    right_Motor.dc(0)
                    wait(500)
                    guinada("D", 90, 100)
                    left_Motor.dc(-100)
                    right_Motor.dc(-100)
                    wait(350)
                    Drive.brake()
                    Garra.dc(-100)
                    wait(1000)
                    left_Motor.dc(100)
                    right_Motor.dc(100)
                    wait(700)
                    guinada("E",37,90)
                    Drive.straight(80) #170
                    """while True:
                        left_Motor.dc(30)
                        right_Motor.dc(90)
                        if any(numero > 50 for numero in separar_dados('I')):
                            break"""
                    # guinada("E",12,90)
                    Drive.brake()
                    hub.imu.reset_heading(0)
                    canto_verde += 1
                    canto_verde_alinhamento += 1
                    hub.imu.reset_heading(0)
                    abudega = 0 
                    hub.ble.broadcast("PARAR")
    

                if any(item.startswith("Color.RED") for item in separar_dados("S")) or any(item.startswith("Color.REDL") for item in separar_dados("S")) or any(item.startswith("Color.REDLL") for item in separar_dados("S")) and abudega >2:
                    hub.ble.broadcast("PARAR")
                    print("Viu vermelho")
                    left_Motor.dc(60)
                    right_Motor.dc(60)
                    wait(700)
                    Drive.brake()
                    guinada("E", 5, 80)
                    run_task(resg())
                    '''Garra.dc(100)
                    wait(1100)
                    Garra.dc(-100)
                    wait(900)'''
                    Drive.straight(50)
                    Garra.dc(100)
                    wait(1200)
                    guinada("E", 90, 100)
                    wait(600)
                    Garra.dc(-100)
                    wait(1200)
                    left_Motor.dc(-100)
                    right_Motor.dc(-100)
                    wait(500)
                    Garra.dc(-100)
                    wait(1100)
                    left_Motor.dc(100)
                    right_Motor.dc(100)
                    wait(1900)
                    Drive.brake()
                    Garra.dc(100)
                    wait(1200)
                    Garra.brake()
                    wait(200)
                    Garra.dc(100)
                    wait(1200)
                    left_Motor.dc(-100)
                    right_Motor.dc(-100)
                    wait(3000)
                    guinada("D", 90, 100)
                    left_Motor.dc(-100)
                    right_Motor.dc(-100)
                    wait(350)
                    Drive.brake()
                    Garra.dc(-100)
                    wait(1000)
                    left_Motor.dc(100)
                    right_Motor.dc(100)
                    wait(700)
                    """while True:
                        left_Motor.dc(30)
                        right_Motor.dc(90)
                        if any(numero > 50 for numero in separar_dados('I')):
                            break
                    wait(600)"""
                    # guinada("E",12,90)
                    guinada("E",37,90)
                    Drive.straight(80)
                    Drive.brake()
                    hub.imu.reset_heading(0)
                    canto_vermelho += 1
                    abudega = 0
                    hub.ble.broadcast("PARAR")


        if sensor_CorD.reflection() >= 90 and sensor_CorE.reflection() > 90 :
            print("Viu nada")
            Drive.straight(30)
            Drive.brake()
            Garra.dc(100)
            wait(1200)
            Drive.straight(-100)
            wait(900)
            Drive.brake()
            guinada("E", 89, 80)
            Drive.brake()
            Garra.dc(-100)
            wait(1200)
            Drive.straight(200)
            hub.imu.reset_heading(0)
        
    contagem = 0
    buraco = 0
    hub.imu.reset_heading(0)
    while True:
        Drive.straight(30)
        print("SAINDO")
        if any(numero < 350 for numero in separar_dados('I')):
            Drive.straight(30)
            Drive.stop()
            wait(200)
            if any(numero < 350 for numero in separar_dados('I')):
                if varrer_meio == quant_meio:
                    Drive.straight(40)
                    guinada("E", 85, 100)
                    left_Motor.dc(-100)
                    right_Motor.dc(-100)
                    wait(3000)
                    left_Motor.dc(100)
                    right_Motor.dc(100)
                    wait(2350)
                    left_Motor.dc(-100)
                    right_Motor.dc(-100)
                    wait(2450)
                    Drive.straight(25)
                    guinada("D", 89, 100)
                    hub.imu.reset_heading(0)
                    varrer_meio += 1
                else :
                    Drive.straight(40)
                    guinada("E", 85, 100)
                    left_Motor.dc(-100)
                    right_Motor.dc(-100)
                    wait(3000)
                    Drive.straight(25)
                    guinada("D", 89, 100)
                    hub.imu.reset_heading(0)
                    varrer_meio += 1
        while True:
            print(UltrassonicoF.distance())
            left_Motor.dc(90)
            right_Motor.dc(90)
            parede = 0 
            if UltrassonicoF.distance() < 120 and UltrassonicoF.distance() > 100 :
                timer.reset()
                while True :
                    left_Motor.dc(90)
                    right_Motor.dc(87)
                    if (UltrassonicoF.distance() < 120):
                        parede += 1

                    if timer.time()>700 or sensor_CorD.reflection() < 18 and sensor_CorE.reflection() < 18 or hub.imu.heading() < -22 or any(numero > 300 for numero in separar_dados('I')) or sensor_CorD.reflection() > 90 and sensor_CorE.reflection() > 90: 
                        parede = 0 
                        break
                    if (UltrassonicoF.distance() < 120 and hub.imu.heading() > -11 and hub.imu.heading() < 11 and parede > 555):
                        break

                    if UltrassonicoF.distance() > 140 :
                        parede = 0 
            
            if (UltrassonicoF.distance() < 120 and hub.imu.heading() > -11 and hub.imu.heading() < 11 and parede > 550  or
                    (sensor_CorD.reflection() < 18 and sensor_CorE.reflection() < 18) or
                    hub.imu.heading() < -22 or any(numero > 360 for numero in separar_dados('I')) or
                    (sensor_CorD.reflection() > 90 and sensor_CorE.reflection() > 90)):
                print(hub.imu.heading())
                Drive.brake()
                break


        if UltrassonicoF.distance() < 120 and (hub.imu.heading() > -11 and hub.imu.heading() < 11) and parede > 550:
            if any(numero > 360 for numero in separar_dados('I')) :
                Drive.brake()
                wait(100)
                timer.reset()
                while True :
                    if timer.time()> 600 and any(numero > 360 for numero in separar_dados('I')) :
                        print("SAIDA - BURACO(NAO VIU PAREDE)")
                        print("saiu")
                        Garra.dc(100)
                        wait(1900)
                        timer.reset()
                        while True:
                            print(separar_dados('I'))
                            right_Motor.dc(-60)
                            left_Motor.dc(-60)
                            if any(numero <= 200 for numero in separar_dados('I')) or timer.time()>6000:
                                Drive.brake()
                                Drive.straight(100)
                                break
                        while True:
                            right_Motor.dc(60)
                            left_Motor.dc(60)
                            if any(numero <= 200 for numero in separar_dados('I')) or UltrassonicoF.distance()<50:
                                Drive.brake()
                                Drive.straight(-100)
                                break
                        timer.reset()
                        while True:
                            right_Motor.dc(-60)
                            left_Motor.dc(-60)
                            if any(numero <= 170 for numero in separar_dados('I')) or timer.time()>6000:
                                Drive.brake()
                                Drive.straight(70)
                                break
                        left_Motor.dc(80)
                        right_Motor.dc(80)
                        wait(700)
                        guinada("D", 85, 80)
                        timer.reset()
                        while True:
                            left_Motor.dc(80)
                            right_Motor.dc(80)
                            print(timer.time())
                            if sensor_CorE.reflection() < 19 and sensor_CorD.reflection() < 19 or sensor_CorE.reflection() > 80 or sensor_CorD.reflection() > 80 or timer.time() > 2000:
                                if sensor_CorE.reflection() < 19 and sensor_CorD.reflection() < 19:
                                    print("indentificou preto")
                                    left_Motor.dc(80)
                                    right_Motor.dc(80)
                                    wait(700)
                                    guinada("E", 40, 80)
                                    while not sensor_CorE.reflection() < 15:
                                        left_Motor.dc(80)
                                        right_Motor.dc(-80)
                                    hub.ble.broadcast(3)
                                    while True:
                                        seguir_Linha(5, 80)
                                        curvabrusca()
                                        verifica_verde()
                                        FitaRED()
                                        Obstaculo()
                                        rampa()
                                if timer.time() > 2000 or sensor_CorE.reflection() > 85 or sensor_CorD.reflection() > 85:
                                    while True:
                                        right_Motor.dc(-70)
                                        left_Motor.dc(-70)
                                        if any(numero <= 150 for numero in separar_dados('I')) or sensor_CorE.reflection() > 80 or sensor_CorD.reflection() > 80:
                                            Drive.brake()
                                            break
                                    print("tem nada, segue")
                                    left_Motor.dc(-80)
                                    right_Motor.dc(-80)
                                    wait(900)
                                    Drive.brake()
                                    guinada("E", 89, 80)
                                    Drive.brake()
                                    wait(250)
                                    if UltrassonicoF.distance() <= 90:
                                        guinada("E", 89, 80)
                                        left_Motor.dc(-80)
                                        right_Motor.dc(-80)
                                        wait(300)
                                        Drive.brake()
                                        Garra.dc(-100)
                                        wait(1200)
                                        hub.imu.reset_heading(0)
                                    else:
                                        Garra.dc(-100)
                                        wait(1200)
                                        left_Motor.dc(80)
                                        right_Motor.dc(80)
                                        wait(1500)
                                        hub.imu.reset_heading(0)
                            if timer.time()> 600 and not any(numero > 300 for numero in separar_dados('I')) :
                                break
            else:                
                Drive.brake()
                print("viu parede")
                Drive.brake()
                left_Motor.dc(-100)
                right_Motor.dc(-100)
                wait(700)
                Drive.brake()
                Garra.dc(90)
                wait(2000)
                Drive.brake()
                left_Motor.dc(100)
                right_Motor.dc(100)
                wait(800)
                guinada("E", 89, 100)
                left_Motor.dc(-100)
                right_Motor.dc(-100)
                wait(140)
                Drive.brake()
                Garra.dc(-90)
                wait(2000)
                Drive.brake()
                hub.imu.reset_heading(0)

        if (sensor_CorD.reflection() < 18 and sensor_CorE.reflection() < 18):
            print("viu saida")
            Garra.dc(100)
            wait(1200)
            left_Motor.dc(100)
            right_Motor.dc(100)
            wait(400)
            guinada("E", 35, 80)
            while not sensor_CorE.color() == Color.BLACK:
                left_Motor.dc(80)
                right_Motor.dc(-80)
            hub.ble.broadcast(3)
            while True:
                seguir_Linha(5, 80)
                curvabrusca()
                verifica_verde()
                FitaRED()
                Obstaculo()
                rampa()

        elif hub.imu.heading() < -21:
            Drive.brake()
            timer.reset()
            hub.ble.broadcast("COR")
            while timer.time() < 1100:
                if any(item.startswith("Color.GREEN") for item in separar_dados("S")) or any(item.startswith("Color.GRENL") for item in separar_dados("S")) or any(item.startswith("Color.GRENLL") for item in separar_dados("S")) :
                    hub.ble.broadcast("PARAR")
                    print("Viu verde")
                    left_Motor.dc(100)
                    right_Motor.dc(100)
                    wait(700)
                    """while True:
                        left_Motor.dc(30)
                        right_Motor.dc(90)
                        if any(numero > 50 for numero in separar_dados('I')):
                            break
                    wait(600)"""
                    guinada("E",40,90)
                    Drive.straight(80)
                    Drive.brake()
                    hub.imu.reset_heading(0)

                if any(item.startswith("Color.RED") for item in separar_dados("S")) or any(item.startswith("Color.REDL") for item in separar_dados("S")) or any(item.startswith("Color.REDLL") for item in separar_dados("S")):
                    hub.ble.broadcast("PARAR")
                    print("Viu verde")
                    left_Motor.dc(100)
                    right_Motor.dc(100)
                    wait(700)
                    """while True:
                        left_Motor.dc(30)
                        right_Motor.dc(90)
                        if any(numero > 50 for numero in separar_dados('I')):
                            break
                    wait(600)"""
                    guinada("E",40,90)
                    Drive.straight(80)
                    Drive.brake()
                    hub.imu.reset_heading(0)
                                                                                                                                                                                                                                                                                                                      
        elif any(numero > 360 for numero in separar_dados('I')) :
            Drive.brake()
            wait(100)
            timer.reset()
            while True :
                if timer.time()> 600 and any(numero > 360 for numero in separar_dados('I')) :
                    print("SAIDA - BURACO(NAO VIU PAREDE)")
                    print("saiu")
                    Garra.dc(100)
                    wait(1900)
                    while True:
                        print(separar_dados('I'))
                        right_Motor.dc(-60)
                        left_Motor.dc(-60)
                        if any(numero <= 200 for numero in separar_dados('I')):
                            Drive.brake()
                            Drive.straight(100)
                            break
                    while True:
                        right_Motor.dc(60)
                        left_Motor.dc(60)
                        if any(numero <= 200 for numero in separar_dados('I')) or UltrassonicoF.distance()<50:
                            Drive.brake()
                            Drive.straight(-100)
                            break
                    while True:
                        right_Motor.dc(-60)
                        left_Motor.dc(-60)
                        if any(numero <= 170 for numero in separar_dados('I')):
                            Drive.brake()
                            Drive.straight(70)
                            break
                    left_Motor.dc(80)
                    right_Motor.dc(80)
                    wait(550)
                    guinada("D", 85, 80)
                    timer.reset()
                    while True:
                        left_Motor.dc(80)
                        right_Motor.dc(80)
                        print(timer.time())
                        if sensor_CorE.reflection() < 19 and sensor_CorD.reflection() < 19 or sensor_CorE.reflection() > 80 or sensor_CorD.reflection() > 80 or timer.time() > 2000:
                            if sensor_CorE.reflection() < 19 and sensor_CorD.reflection() < 19:
                                print("indentificou preto")
                                left_Motor.dc(80)
                                right_Motor.dc(80)
                                wait(500)
                                guinada("E", 40, 80)
                                while not sensor_CorE.reflection() < 15:
                                    left_Motor.dc(80)
                                    right_Motor.dc(-80)
                                hub.ble.broadcast(3)
                                while True:
                                    seguir_Linha(5, 80)
                                    curvabrusca()
                                    verifica_verde()
                                    FitaRED()
                                    Obstaculo()
                                    rampa()
                            if timer.time() > 2000 or sensor_CorE.reflection() > 85 or sensor_CorD.reflection() > 85:
                                while True:
                                    right_Motor.dc(-70)
                                    left_Motor.dc(-70)
                                    if any(numero <= 150 for numero in separar_dados('I')) or sensor_CorE.reflection() > 80 or sensor_CorD.reflection() > 80:
                                        Drive.brake()
                                        break
                                print("tem nada, segue")
                                left_Motor.dc(-80)
                                right_Motor.dc(-80)
                                wait(900)
                                Drive.brake()
                                guinada("E", 89, 80)
                                Drive.brake()
                                wait(250)
                                if UltrassonicoF.distance() <= 90:
                                    guinada("E", 89, 80)
                                    left_Motor.dc(-80)
                                    right_Motor.dc(-80)
                                    wait(300)
                                    Drive.brake()
                                    Garra.dc(-100)
                                    wait(1200)
                                    hub.imu.reset_heading(0)
                                else:
                                    Garra.dc(-100)
                                    wait(1200)
                                    left_Motor.dc(80)
                                    right_Motor.dc(80)
                                    wait(1500)
                                    hub.imu.reset_heading(0)
                        if timer.time()> 600 and not any(numero > 300 for numero in separar_dados('I')) :
                            break

        if sensor_CorD.reflection() >= 90 and sensor_CorE.reflection() > 90 :
            print("Viu nada")
            Drive.straight(30)
            Drive.brake()
            Garra.dc(100)
            wait(1200)
            Drive.straight(-100)
            wait(900)
            Drive.brake()
            guinada("E", 89, 80)
            Drive.brake()
            Garra.dc(-100)
            wait(1200)
            Drive.straight(200)
            hub.imu.reset_heading(0)

                
                                
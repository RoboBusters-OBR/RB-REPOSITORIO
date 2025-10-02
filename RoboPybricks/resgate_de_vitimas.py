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
    await multitask(Drive.straight(-40), move_gripper())

async def resg():
    await multitask(Drive.straight(-20), move_gripper())    

async def sobe():
    await multitask(Drive.straight(-40), sobe_gripper())        

def identifica_sala():
    from seguimento_de_linha import seguir_Linha, FitaRED, curvabrusca, verifica_verde
    from obstaculos_trajeto import Obstaculo, separar_dados
    if any(numero < 260 for numero in separar_dados('I')) or sensor_CorD.reflection() > 90 and sensor_CorE.reflection() > 90  :
        Drive.brake()
        guinada('D', 10,100)
        timer.reset()
        while True :
            mover(-100)
            if sensor_CorD.reflection()< 20 or timer.time() > 500 :
                break
        Drive.stop()
        if sensor_CorD.reflection()< 20: 
            while True :
                seguir_Linha(5,80)
                curvabrusca()
                verifica_verde()
                FitaRED()
                Obstaculo()
                if timer.time() > 1500:
                    break
        else:
            Drive.brake()
            hub.speaker.beep(500,500)
            hub.ble.broadcast("AREA_DE_RESGATE")
            guinada("D", 30, 100)
            left_Motor.dc(80)
            right_Motor.dc(80)
            wait(350)
            Drive.brake()
            fazer_resgate()

def fazer_resgate():
    from seguimento_de_linha import seguir_Linha, verifica_verde, curvabrusca, FitaRED
    from obstaculos_trajeto import rampa,separar_dados,Obstaculo

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
        guinada("E", 90, 90)
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
        wait(500)
        Drive.brake()
        guinada("D", 89, 70)
        Drive.brake()
        Garra.dc(-90)
        wait(1200)
        Drive.straight(200)
        Garra.dc(-90)
        wait(1500)
        quant_meio = 0
    timer.reset()
    canto_verde = 0
    varrer_meio = 0
    canto_vermelho = 0
    hub.imu.reset_heading(0)
    parede = 0
    abudega = 0
    while True:

        print(canto_verde)

        if canto_verde == 2:
            break
        Drive.straight(30)
        print("DEIXANDO")
        if any(numero < 300 for numero in separar_dados('I')):
            if varrer_meio == quant_meio:
                if canto_vermelho == 1:
                    Drive.straight(40)
                    guinada("E", 80, 100)
                    left_Motor.dc(-100)
                    right_Motor.dc(-100)
                    wait(3000)
                    left_Motor.dc(100)
                    right_Motor.dc(95)
                    wait(2350)
                    left_Motor.dc(-100)
                    right_Motor.dc(-100)
                    wait(2450)
                    Drive.straight(35)
                    guinada("D", 89, 100)
                    hub.imu.reset_heading(0)
                    varrer_meio += 1
                elif canto_verde == 1:
                    Drive.straight(40)
                    guinada("E", 80, 100)
                    left_Motor.dc(-100)
                    right_Motor.dc(-100)
                    wait(3000)
                    left_Motor.dc(100)
                    right_Motor.dc(95)
                    wait(2350)
                    left_Motor.dc(-100)
                    right_Motor.dc(-100)
                    wait(2450)
                    Drive.straight(35)
                    guinada("D", 89, 100)
                    hub.imu.reset_heading(0)
                    varrer_meio += 1
                else:    
                    Drive.straight(40)
                    guinada("E", 80, 100)
                    left_Motor.dc(-100)
                    right_Motor.dc(-100)
                    wait(3000)
                    left_Motor.dc(100)
                    right_Motor.dc(95)
                    wait(2350)
                    left_Motor.dc(-100)
                    right_Motor.dc(-100)
                    wait(2450)
                    Drive.straight(35)
                    guinada("D", 89, 100)
                    hub.imu.reset_heading(0)
                    varrer_meio += 1
            elif varrer_meio != quant_meio:
                if canto_vermelho == 1:
                    Drive.straight(40)
                    guinada("E", 80, 100)
                    left_Motor.dc(-100)
                    right_Motor.dc(-100)
                    wait(3000)
                    left_Motor.dc(100)
                    right_Motor.dc(95)
                    wait(2350)
                    left_Motor.dc(-100)
                    right_Motor.dc(-100)
                    wait(2450)
                    Drive.straight(35)
                    guinada("D", 89, 100)
                    hub.imu.reset_heading(0)
                    varrer_meio += 1
                elif canto_verde == 1:
                    Drive.straight(40)
                    guinada("E", 80, 100)
                    left_Motor.dc(-100)
                    right_Motor.dc(-100)
                    wait(3000)
                    left_Motor.dc(100)
                    right_Motor.dc(95)
                    wait(2350)
                    left_Motor.dc(-100)
                    right_Motor.dc(-100)
                    wait(2450)
                    Drive.straight(35)
                    guinada("D", 89, 100)
                    hub.imu.reset_heading(0)
                    varrer_meio += 1
                else:    
                    Drive.straight(40)
                    guinada("E", 80, 100)
                    left_Motor.dc(-100)
                    right_Motor.dc(-100)
                    wait(1500)
                    Drive.straight(20)
                    left_Motor.dc(-100)
                    right_Motor.dc(-100)
                    wait(2000)
                    Drive.straight(35)
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
                    right_Motor.dc(90)
                    parede += 1
                    if timer.time()>700 or sensor_CorD.reflection() < 18 and sensor_CorE.reflection() < 18 or hub.imu.heading() < -19 or sensor_CorD.reflection() > 90 and sensor_CorE.reflection() > 90 or sensor_CorD.reflection() > 33 and sensor_CorE.reflection() > 33 and sensor_CorD.reflection() < 42 and sensor_CorE.reflection() < 42: 
                        break
                    if UltrassonicoF.distance() > 200 :
                        parede = 0 
            if (UltrassonicoF.distance() < 120 and hub.imu.heading() > -9 and hub.imu.heading() < 9 and parede > 40  or
                    (sensor_CorD.reflection() < 18 and sensor_CorE.reflection() < 18) or
                    hub.imu.heading() < -19 or
                    (sensor_CorD.reflection() > 90 and sensor_CorE.reflection() > 90) or 
                    (sensor_CorD.color() == Color.SILVER and sensor_CorE.color() == Color.SILVER and sensor_CorD.reflection() >= 36 and sensor_CorD.reflection() <= 42 and sensor_CorE.reflection() >= 36 and sensor_CorE.reflection() <=42) ):
                print(hub.imu.heading())
                print(separar_dados('S'))
                Drive.brake()
                break 
        if UltrassonicoF.distance() < 120 :
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

                if any(item.startswith("Color.GREEN") for item in separar_dados("S")) or any(item.startswith("Color.GRENL") for item in separar_dados("S")) or any(item.startswith("Color.GRENLL") for item in separar_dados("S")) :
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
                    guinada("E",35,90)
                    Drive.straight(70)
                    """while True:
                        left_Motor.dc(30)
                        right_Motor.dc(90)
                        if any(numero > 50 for numero in separar_dados('I')):
                            break"""
                    # guinada("E",12,90)
                    Drive.brake()
                    hub.imu.reset_heading(0)
                    canto_verde += 1
                    hub.imu.reset_heading(0)
                    abudega = 0 
    

                if any(item.startswith("Color.RED") for item in separar_dados("S")) or any(item.startswith("Color.REDL") for item in separar_dados("S")) or any(item.startswith("Color.REDLL") for item in separar_dados("S")):
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
                    Drive.straight(20)
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
                    guinada("E",35,90)
                    Drive.straight(70)
                    Drive.brake()
                    hub.imu.reset_heading(0)
                    canto_vermelho += 1
                    abudega = 0

        

        if (sensor_CorD.color() == Color.SILVER and sensor_CorE.color() == Color.SILVER and sensor_CorD.reflection() >= 36 and sensor_CorD.reflection() <= 42 and sensor_CorE.reflection() >= 36 and sensor_CorE.reflection() <=42) :
            print("Viu nada")
            print(hub.imu.heading())
            Drive.straight(40)
            Drive.brake()
            Garra.dc(100)
            wait(1200)
            Drive.straight(-100)
            guinada("E", 90, 80)
            Drive.brake()
            Garra.dc(-100)
            wait(1200)
            hub.imu.reset_heading(0)  # deixação acaba aqui
            Drive.straight(200)

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
        if any(numero < 400 for numero in separar_dados('I')):
            if varrer_meio == quant_meio:
                Drive.straight(40)
                guinada("E", 80, 100)
                left_Motor.dc(-100)
                right_Motor.dc(-100)
                wait(3000)
                left_Motor.dc(100)
                right_Motor.dc(95)
                wait(2350)
                left_Motor.dc(-100)
                right_Motor.dc(-100)
                wait(2450)
                Drive.straight(50)
                guinada("D", 89, 100)
                hub.imu.reset_heading(0)
                varrer_meio += 1
            else:
                Drive.straight(40)
                guinada("E", 80, 100)
                left_Motor.dc(-100)
                right_Motor.dc(-100)
                wait(3000)
                Drive.straight(50)
                guinada("D", 89, 100)
                hub.imu.reset_heading(0)
                varrer_meio += 1
        while True:
            print(UltrassonicoF.distance())
            left_Motor.dc(100)
            right_Motor.dc(100)
            if UltrassonicoF.distance() < 120 and UltrassonicoF.distance() > 100 :
                timer.reset()
                while True :
                    left_Motor.dc(100)
                    right_Motor.dc(100)
                    parede += 1
                    if timer.time()>700 or sensor_CorD.reflection() < 18 and sensor_CorE.reflection() < 18 or hub.imu.heading() < -22 or any(numero > 300 for numero in separar_dados('I')) or sensor_CorD.reflection() > 90 and sensor_CorE.reflection() > 90 or sensor_CorD.reflection() > 33 and sensor_CorE.reflection() > 33 and sensor_CorD.reflection() < 42 and sensor_CorE.reflection() < 42: 
                        break
                    if UltrassonicoF.distance() > 200  :
                        parede = 0 
            if (UltrassonicoF.distance() < 120 and hub.imu.heading() > -9 and hub.imu.heading() < 9 and parede > 40  or
                    (sensor_CorD.reflection() < 18 and sensor_CorE.reflection() < 18) or
                    hub.imu.heading() < -22 or any(numero > 300 for numero in separar_dados('I')) or
                    (sensor_CorD.reflection() > 90 and sensor_CorE.reflection() > 90) or
                    (sensor_CorD.color() == Color.SILVER and sensor_CorE.color() == Color.SILVER and sensor_CorD.reflection() >= 36 and sensor_CorD.reflection() <= 42 and sensor_CorE.reflection() >= 36 and sensor_CorE.reflection() <=42)):
                print(hub.imu.heading())
                Drive.brake()
                break


        if UltrassonicoF.distance() < 120 and (hub.imu.heading() > -9 and hub.imu.heading() < 9) :
            Drive.brake()
            print("viu parede")
            Drive.brake()
            left_Motor.dc(-100)
            right_Motor.dc(-100)
            wait(70)
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

        if hub.imu.heading() < -21:
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
                    guinada("E",35,90)
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
                    guinada("E",35,90)
                    Drive.straight(80)
                    Drive.brake()
                    hub.imu.reset_heading(0)
        if (sensor_CorD.color() == Color.SILVER and sensor_CorE.color() == Color.SILVER and sensor_CorD.reflection() >= 36 and sensor_CorD.reflection() <= 42 and sensor_CorE.reflection() >= 36 and sensor_CorE.reflection() <=42):
            Drive.straight(0.8)
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
            else:    
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
        elif any(numero > 300 for numero in separar_dados('I')) :
            Drive.brake()
            wait(100)
            timer.reset()
            while True :

                if timer.time()> 600 and any(numero > 300 for numero in separar_dados('I')) :
                    print("SAIDA - BURACO(NAO VIU PAREDE)")
                    print("saiu")
                    Drive.straight(-60)
                    Garra.dc(100)
                    wait(1200)
                    left_Motor.dc(80)
                    right_Motor.dc(80)
                    wait(1100)
                    guinada("D", 87, 80)
                    timer.reset()
                    while True:
                        left_Motor.dc(80)
                        right_Motor.dc(80)
                        if sensor_CorE.reflection() < 20 and sensor_CorD.reflection() < 20 or timer.time() > 900:
                            Drive.brake()
                            break
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
                    else:
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

                
                                
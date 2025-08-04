# obstaculos_trajeto
from config import hub, left_Motor, right_Motor, Drive, UltrassonicoF, timer, Garra, my_colors, sensor_CorD, sensor_CorE, Color
from movimentos_bases import guinada, mover
from pybricks.tools import wait


def rampa():
    from seguimento_de_linha import seguir_Linha, verifica_verde, FitaRED

    if hub.imu.tilt()[1] < -15:
        while not hub.imu.tilt()[1] > -5:
            seguir_Linha(6, 59)
            verifica_verde()
            Obstaculo()

    if hub.imu.tilt()[0] < -15:
        Drive.brake()
        wait(200)
        print('RAMPA')
        Garra.run_angle(90, -150)

        timer.reset()
        while True:
            # 5, 72 # CURVA  > 5 < 19 AND > 20 < 42 4.2 , 75
            seguir_Linha(0.9, 100)
            verifica_verde()
            FitaRED()
            if hub.imu.tilt()[0] > -1 and timer.time() > 500:
                Drive.brake()
                wait(500)
                Garra.run_target(100, -1)
                break

            if hub.imu.tilt()[0] > 4 and hub.imu.tilt()[0] < 40:
                break
            elif hub.imu.tilt()[0] > -2 and hub.imu.tilt()[0] < 6:
                Drive.brake()
                Garra.dc(100)
                wait(800)
                while True:
                    seguir_Linha(6, 55)
                    verifica_verde()
                    FitaRED()
                    Obstaculo()
                    if hub.imu.tilt()[0] > 6:
                        break

    elif hub.imu.tilt()[0] < -1 and hub.imu.tilt()[0] > -4 and sensor_CorD.reflection() > 30 and sensor_CorE.reflection() > 30:
        print('LOMBADA')
        timer.reset()
        while True:
            if timer.time() > 1200:
                break
            seguir_Linha(6, 60)
            identifica_sala()  # 5, 72 # CURVA  > 5 < 19 AND > 20 < 42 4.2 , 75
            verifica_verde()
            Obstaculo()
            FitaRED()

        while True:
            if not hub.imu.tilt()[0] < 1:
                Drive.brake()
                break
            seguir_Linha(6, 40)
            identifica_sala()  # 5, 72 # CURVA  > 5 < 19 AND > 20 < 42 4.2 , 75
            verifica_verde()
            Obstaculo()
            FitaRED()

    elif hub.imu.tilt()[0] > 10 and hub.imu.tilt()[0] < 40:
        print('DESCIDA')
        Drive.brake()

        timer.reset()
        while True:
            seguir_Linha(0.9, 50)
            verifica_verde()
            Obstaculo()
            if hub.imu.tilt()[0] < 2:
                Drive.brake()
                Garra.dc(100)
                wait(700)
                break
            if hub.imu.tilt()[0] > 60:
                Garra.dc(-100)
                wait(2000)
                Garra.dc(100)
                wait(2000)

    if hub.imu.tilt()[0] > 60:
        Garra.dc(100)
        wait(1000)
        Garra.dc(-100)
        wait(1500)


def Obstaculo():

    from seguimento_de_linha import seguir_Linha
    if UltrassonicoF.distance() <= 50:
        timer.reset()
        while True:  # gira para esquerrda até que ache a linha com o sensor da direita
            seguir_Linha(1, 40)
            if timer.time() >= 300:
                Drive.brake()
                break
    if UltrassonicoF.distance() <= 50:
        Drive.settings(straight_speed=500, straight_acceleration=500)

        Drive.straight(-30)
        guinada('E', 90, 90)
        Drive.straight(50)
        while True:
            Drive.drive(-100, 0)
            if sensor_CorD.reflection() < 29 and sensor_CorE.reflection() < 29:
                Drive.brake()
                break
        while True:
            Drive.drive(100, 0)
            if sensor_CorD.color() == Color.WHITE and sensor_CorE.color() == Color.WHITE:
                Drive.brake()
                break
        '''while True:
            left_Motor.run(-150)
            if sensor_CorE.reflection() <=16 and sensor_CorE.reflection() >=7:
                Drive.brake()
                break
        while True:
            right_Motor.run(-150)
            if sensor_CorD.reflection() <= 8:
                Drive.brake()
                break'''

        Drive.straight(60)
        hub.imu.reset_heading(0)
        while True:
            left_Motor.dc(90)
            right_Motor.dc(41)
            if abs(hub.imu.heading()) > 180 and abs(hub.imu.heading()) < 187:
                Drive.straight(40)
                guinada('D', 90, 80)
                while True:
                    left_Motor.dc(60)
                    right_Motor.dc(60)
                    if UltrassonicoF.distance() < 50:
                        Drive.straight(10)
                        Drive.brake()
                        break
                '''while True:
                    mover(80)
                    if UltrassonicoF.distance()< 220:
                        Drive.brake()
                        guinada('D',20, 100)
                        while True:
                            left_Motor.dc(60)
                            right_Motor.dc(60)
                            if UltrassonicoF.distance()< 50:
                                Drive.straight(10)
                                Drive.brake()
                                break 
                        timer.reset()
                        Drive.brake()'''

                timer.reset()
                while True:
                    guinada('8', 9, 70)
                    mover(-80)
                    if sensor_CorD.reflection() < 20:
                        print("Tem sim")
                        guinada("E", 80, 100)
                        while True:
                            mover(-70)
                            if sensor_CorD.reflection() < 12:
                                Drive.straight(-40)
                                return 0
                                break

                        # elif timer.time() > 500 :
                        # print("Tem nada")
                        # guinada('E',80,80)
                        # print("voltando")
                        # hub.imu.reset_heading(0)

                        # break
                        # break

                # break

        '''Drive.straight(70)
        while True:  # se nao achou proucura no lado oposto
            right_Motor.dc(80)
            left_Motor.dc(-80)
            if (sensor_CorD.reflection() >= 9) and (sensor_CorD.reflection() <= 18):
                #guinada('D', 12, 80)
                Drive.stop()
                break
        Drive.straight(60) 
        guinada('D', 120, 80)         
        while True:  
            right_Motor.dc(-80)
            left_Motor.dc(80)
            if (sensor_CorE.reflection() >= 9) and (sensor_CorE.reflection() <= 18):
                guinada('E', 8, 80)
                Drive.stop()
                break  
        while True:  
            right_Motor.dc(80)
            left_Motor.dc(-80)
            if (sensor_CorD.reflection() >= 9) and (sensor_CorD.reflection() <= 18):
                guinada('D', 16, 80)
                Drive.stop()
                break                
        while True:  
            right_Motor.dc(60)
            left_Motor.dc(60)
            if UltrassonicoF.distance() <= 60:
                Drive.straight(30)
                Drive.stop()
                break
        guinada('E', 120, 80)
        while True:  
            right_Motor.dc(80)
            left_Motor.dc(-80)
            if (sensor_CorE.reflection() >= 9) and (sensor_CorE.reflection() <= 18):
                guinada('E', 20, 80)
                Drive.stop()
                break'''


def separar_dados(tipo):
    inteiros = []
    strings = []

    # Obtenha os dados da função
    tuplaultra = hub.ble.observe(2)

    # Verifique se tuplaultra é uma sequência (tupla, lista, etc.)
    if isinstance(tuplaultra, (list, tuple)):  # Verifica se é uma sequência
        for item in tuplaultra:
            if isinstance(item, int):  # Verifica se é um inteiro
                inteiros.append(item)
            elif isinstance(item, str):  # Verifica se é uma string
                strings.append(item)
    else:
        # Caso não seja uma sequência, trata como um único item
        if isinstance(tuplaultra, int):
            inteiros.append(tuplaultra)
        elif isinstance(tuplaultra, str):
            strings.append(tuplaultra)

    # Retorna os valores conforme o parâmetro 'tipo'
    if tipo == 'S':
        return strings
    elif tipo == 'I':
        return inteiros
    else:
        return None  # Retorna None se o tipo não for 'S' ou 'I'


def identifica_sala():
    from seguimento_de_linha import seguir_Linha, verifica_verde, curvabrusca, FitaRED

    if any(numero < 260 for numero in separar_dados('I')) or sensor_CorD.reflection() > 90 and sensor_CorE.reflection() > 90:
        Drive.brake()
        guinada('D', 10, 100)
        timer.reset()
        while True:
            mover(-100)
            if sensor_CorD.reflection() < 20 or timer.time() > 500:
                break
        Drive.stop()
        if sensor_CorD.reflection() < 20:
            while True:
                seguir_Linha(5, 80)
                curvabrusca()
                verifica_verde()
                FitaRED()
                Obstaculo()
                if timer.time() > 1500:
                    break
        else:
            hub.ble.broadcast("AREA_DE_RESGATE")
            guinada("D", 30, 100)
            left_Motor.dc(80)
            right_Motor.dc(80)
            wait(350)
            Drive.brake()
            fazer_resgate()


def fazer_resgate():
    from seguimento_de_linha import seguir_Linha, verifica_verde, curvabrusca, FitaRED

    timer.reset()
    while True:
        if any(numero < 200 for numero in separar_dados('I')):
            leitura_ultra = 50
        if any(numero > 200 for numero in separar_dados('I')):
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
    elif leitura_ultra == 100:  # se nao esta encostado
        left_Motor.dc(80)
        right_Motor.dc(80)
        wait(600)
        Drive.brake()
        guinada("D", 90, 70)
        Drive.brake()
        Garra.dc(-90)
        wait(1200)
        Drive.straight(250)
        Garra.dc(-90)
        wait(1500)
    timer.reset()
    canto_verde = 0
    hub.imu.reset_heading(0)
    while True:

        print(canto_verde)

        if canto_verde == 2:
            break
        Drive.straight(30)
        print("DEIXANDO")
        if any(numero < 300 for numero in separar_dados('I')):
            Drive.straight(40)
            guinada("E", 80, 100)
            left_Motor.dc(-100)
            right_Motor.dc(-100)
            wait(3000)
            Drive.straight(50)
            guinada("D", 89, 100)
            hub.imu.reset_heading(0)

        while True:

            left_Motor.dc(90)
            right_Motor.dc(90)
            if (UltrassonicoF.distance() < 120 or
                    (sensor_CorD.reflection() < 18 and sensor_CorE.reflection() < 18) or
                    hub.imu.heading() < -19 or
                    (sensor_CorD.reflection() > 90 and sensor_CorE.reflection() > 90)):
                print(hub.imu.heading())
                print(separar_dados('S'))
                Drive.brake()
                break
        if UltrassonicoF.distance() < 120:
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
            guinada("E", 90, 80)
            Drive.brake()
            Garra.dc(-100)
            wait(1200)
            hub.imu.reset_heading(0)
        if hub.imu.heading() < -18:
            Drive.brake()
            timer.reset()
            hub.ble.broadcast("COR")
            while timer.time() < 1800:
                if any(item.startswith("Color.GREEN") for item in separar_dados("S")):
                    hub.ble.broadcast("PARAR")
                    print("Viu verde")
                    left_Motor.dc(60)
                    right_Motor.dc(60)
                    wait(550)
                    Drive.brake()
                    guinada("E", 5, 80)
                    run_task(resg())
                    '''Garra.dc(100)
                    wait(1100)
                    Garra.dc(-100)
                    wait(900)'''
                    Drive.straight(20)
                    Garra.dc(100)
                    wait(800)
                    guinada("E", 90, 100)
                    Garra.dc(-100)
                    wait(800)
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
                    wait(200)
                    hub.ble.broadcast(0)
                    Garra.dc(-100)
                    wait(1100)
                    left_Motor.dc(100)
                    right_Motor.dc(100)
                    wait(2100)
                    Drive.brake()
                    Garra.dc(100)
                    wait(500)
                    Garra.brake()
                    wait(200)
                    Garra.dc(100)
                    wait(800)
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
                    wait(580)
                    while True:
                        left_Motor.dc(30)
                        right_Motor.dc(90)
                        if any(numero > 50 for numero in separar_dados('I')):
                            break
                    wait(600)
                    # guinada("E",12,90)
                    Drive.brake()
                    hub.imu.reset_heading(0)
                    canto_verde += 1

                if any(item.startswith("Color.RED") for item in separar_dados("S")):
                    hub.ble.broadcast("PARAR")
                    print("Viu vermelho")
                    left_Motor.dc(60)
                    right_Motor.dc(60)
                    wait(550)
                    Drive.brake()
                    guinada("E", 5, 80)
                    run_task(resg())
                    '''Garra.dc(100)
                    wait(1100)
                    Garra.dc(-100)
                    wait(900)'''
                    Drive.straight(20)
                    Garra.dc(100)
                    wait(800)
                    guinada("E", 90, 100)
                    wait(600)
                    Garra.dc(-100)
                    wait(800)
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
                    wait(500)
                    Garra.brake()
                    wait(200)
                    Garra.dc(100)
                    wait(800)
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
                    wait(580)
                    while True:
                        left_Motor.dc(30)
                        right_Motor.dc(90)
                        if any(numero > 50 for numero in separar_dados('I')):
                            break
                    wait(600)
                    # guinada("E",12,90)
                    Drive.brake()
                    hub.imu.reset_heading(0)
        elif (sensor_CorD.reflection() > 90 and sensor_CorE.reflection() > 90):
            print("Viu nada")
            print(hub.imu.heading())
            Drive.straight(40)
            Drive.brake()
            Garra.dc(90)
            wait(1200)
            while True:
                left_Motor.dc(-100)
                right_Motor.dc(-100)
                if sensor_CorD.reflection() > 92 and sensor_CorE.reflection() > 92:
                    break
            Drive.straight(-60)
            guinada("E", 90, 80)
            Drive.brake()
            Garra.dc(-100)
            wait(1200)
            hub.imu.reset_heading(0)  # deixassancia acaba aqui
    repetir_saida = 0
    timer.reset()
    repetir_saida = 4
    hub.imu.reset_heading(0)
    saida = 0
    while True:
        if saida == repetir_saida:
            break
        Drive.straight(30)
        print("SAINDO")
        if any(numero < 300 for numero in separar_dados('I')):
            Drive.straight(40)
            guinada("E", 80, 100)
            left_Motor.dc(-100)
            right_Motor.dc(-100)
            wait(3000)
            Drive.straight(50)
            guinada("D", 89, 100)
            hub.imu.reset_heading(0)
        while True:
            left_Motor.dc(90)
            right_Motor.dc(90)
            if (UltrassonicoF.distance() < 160 or
                    (sensor_CorD.reflection() < 18 and sensor_CorE.reflection() < 18) or
                    hub.imu.heading() < -22 or any(numero > 400 for numero in separar_dados('I')) or
                    (sensor_CorD.reflection() > 90 and sensor_CorE.reflection() > 90)):
                print(hub.imu.heading())
                Drive.brake()
                break
        if UltrassonicoF.distance() < 120:
            Drive.brake()
            saida += 1
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
            while True:
                seguir_Linha(5, 80)
                curvabrusca()
                verifica_verde()
                FitaRED()
                Obstaculo()

        if hub.imu.heading() < -21:
            Drive.brake()
            timer.reset()
            hub.ble.broadcast("COR")
            while timer.time() < 2000:
                if any(item.startswith("Color.GREEN") for item in separar_dados("S")):
                    hub.ble.broadcast("PARAR")
                    saida += 1
                    print("Viu verde")
                    left_Motor.dc(100)
                    right_Motor.dc(100)
                    wait(580)
                    while True:
                        left_Motor.dc(30)
                        right_Motor.dc(90)
                        if any(numero > 50 for numero in separar_dados('I')):
                            break
                    wait(600)
                    Drive.brake()
                    hub.imu.reset_heading(0)

                if any(item.startswith("Color.RED") for item in separar_dados("S")):
                    hub.ble.broadcast("PARAR")
                    saida += 1
                    print("Viu vermelho")
                    left_Motor.dc(100)
                    right_Motor.dc(100)
                    wait(580)
                    while True:
                        left_Motor.dc(30)
                        right_Motor.dc(90)
                        if any(numero > 50 for numero in separar_dados('I')):
                            break
                    wait(600)
                    Drive.brake()
                    hub.imu.reset_heading(0)

        if (sensor_CorD.reflection() > 90 and sensor_CorE.reflection() > 90):
            saida += 1
            print("Viu nada")
            Drive.straight(40)
            Drive.brake()
            Garra.dc(100)
            wait(1200)
            while True:
                left_Motor.dc(-100)
                right_Motor.dc(-100)
                if sensor_CorD.reflection() > 92 and sensor_CorE.reflection() > 92:
                    break
            Drive.straight(-60)
            wait(900)
            Drive.brake()
            guinada("E", 89, 80)
            Drive.brake()
            Garra.dc(-100)
            wait(1200)
            left_Motor.dc(100)
            right_Motor.dc(100)
            wait(600)
            hub.imu.reset_heading(0)

        elif any(numero > 300 for numero in separar_dados('I')):
            print("SAIDA - BURACO(NAO VIU PAREDE)")
            print("saiu")
            Drive.straight(-60)
            Garra.dc(100)
            wait(1200)
            left_Motor.dc(80)
            right_Motor.dc(80)
            wait(1300)
            guinada("D", 87, 80)
            timer.reset()
            while True:
                left_Motor.dc(80)
                right_Motor.dc(80)
                if sensor_CorE.reflection() < 20 and sensor_CorD.reflection() < 20 or timer.time() > 900:
                    Drive.brake()
                    break
            if sensor_CorE.reflection() < 25 and sensor_CorD.reflection() < 25:
                print("indentificou preto")
                left_Motor.dc(80)
                right_Motor.dc(80)
                wait(500)
                guinada("E", 40, 80)
                while not sensor_CorE.reflection() < 15:
                    left_Motor.dc(80)
                    right_Motor.dc(-80)
                while True:
                    seguir_Linha(5, 90)
                    curvabrusca()
                    verifica_verde()
                    FitaRED()
                    Obstaculo()
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
                    wait(900)
                    hub.imu.reset_heading(0)
                    saida += 1
                else:
                    Garra.dc(-100)
                    wait(900)
                    left_Motor.dc(80)
                    right_Motor.dc(80)
                    wait(1500)
                    hub.imu.reset_heading(0)
                    saida += 1

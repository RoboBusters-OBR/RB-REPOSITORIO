# obstaculos_trajeto
from config import hub, left_Motor, right_Motor, Drive, UltrassonicoF, timer, Garra, my_colors, sensor_CorD, sensor_CorE, Color
from movimentos_bases import guinada, mover
from pybricks.tools import wait


def rampa():
    from seguimento_de_linha import seguir_Linha, verifica_verde, FitaRED, curvalombada
    from resgate_de_vitimas import identifica_sala
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
            
            if timer.time() > 2500: 
                Drive.brake()
                print('Acabou o tempo da lombada')
                return 0
            print(hub.imu.tilt()[0])   
            seguir_Linha(4, 60)
            identifica_sala()  # 5, 72 # CURVA  > 5 < 19 AND > 20 < 42 4.2 , 75
            verifica_verde()
            Obstaculo()
            FitaRED()
            curvalombada()

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
        Garra.dc(-100)
        Drive.brake()
        wait(1500)
        Drive.brake()
        wait(800)
        Garra.dc(100)
        Drive.brake()
        wait(1000)


def Obstaculo():
    from resgate_de_vitimas import identifica_sala
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
            right_Motor.dc(39)
            if abs(hub.imu.heading()) > 180 and abs(hub.imu.heading()) < 187:
                Drive.straight(80)
                while True:
                    left_Motor.dc(-70)
                    right_Motor.dc(-70)
                    if sensor_CorD.reflection() < 30 and sensor_CorE.reflection() < 30:
                        break
                Drive.straight(80)    
                guinada('D', 91, 80)
                while True:
                    left_Motor.dc(60)
                    right_Motor.dc(60)
                    if UltrassonicoF.distance() < 50:
                        Drive.straight(15)
                        Drive.brake()
                        break
                print("Tem sim")
                guinada("E", 195, 100)
                while True:
                    mover(70)
                    if sensor_CorE.reflection() < 30:
                        Drive.straight(-47) 
                        return 0



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


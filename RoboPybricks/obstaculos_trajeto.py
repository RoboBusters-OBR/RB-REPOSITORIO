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
                Garra.dc(100)
                Drive.brake()
                wait(1000)
                return 0
                

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
            
            if timer.time() >2000:
                Drive.brake()
                print('Acabou o tempo da lombada')
                return 0
            print(hub.imu.tilt()[0])   
            seguir_Linha(3, 55)
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
        while True:  
            seguir_Linha(1, 40)
            if timer.time() >= 300:
                Drive.brake()
                break
        guinada("E", 60, 100)
        while True:  
            right_Motor.dc(-60)
            left_Motor.dc(60)
            if UltrassonicoF.distance() >= 39 and UltrassonicoF.distance() <= 58:
                Drive.brake()
                wait(400)
                break
        guinada("E",55,100)
        Drive.straight(200)
        guinada("D", 84,100)
        Drive.straight(150)
        while True:
            right_Motor.dc(80)
            left_Motor.dc(80)
            if any(numero > 200 for numero in separar_dados('I')):
                break
        Drive.straight(100)
        guinada("D",85,100)
        while True:
            right_Motor.dc(80)
            left_Motor.dc(80)
            if sensor_CorD.color() == Color.BLACK:
                break
        Drive.straight(50)        
        while not sensor_CorD.color() == Color.BLACK:
            left_Motor.dc(-80)
            right_Motor.dc(80)
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


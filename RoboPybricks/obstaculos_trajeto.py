# obstaculos_trajeto
from config import hub, left_Motor, right_Motor, Drive, UltrassonicoF, timer, Garra, my_colors, sensor_CorD, sensor_CorE, Color
from movimentos_bases import guinada, mover, girar_absoluto
from pybricks.tools import wait



def rampa():
    from seguimento_de_linha import seguir_Linha, verifica_verde, FitaRED, curvalombada,seguir_Linha2,curvabrusca
    from resgate_de_vitimas import identifica_sala
    if hub.imu.tilt()[1] < -15:
        while not hub.imu.tilt()[1] > -5:
            seguir_Linha(6, 59)
            verifica_verde()
            Obstaculo()

    if hub.imu.tilt()[0] < -15 :
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
                wait(800)
                
                break
                

        if hub.imu.tilt()[0] < 1 and hub.imu.tilt()[0] > -40:
            print(hub.imu.tilt()[0] )
            print("AQUI")
            while True:
        
                seguir_Linha(5, 60)
                verifica_verde()
                FitaRED()
                curvabrusca()
                Obstaculo()
                if hub.imu.tilt()[0] < -7:
                    break
            
        if hub.imu.tilt()[0] > 8 and hub.imu.tilt()[0] < 40:
            print("OUTRO AQUI")
            Drive.brake()
            Garra.dc(100)
            wait(800)
            Garra.dc(-100)
            wait(700)
            Garra.dc(100)
            wait(700)
            Drive.straight(-10)
            guinada("D", 20, 100)
            timer.reset()
            achou = 0
            while True :
                mover(-60)
                if sensor_CorD.reflection()< 19 or sensor_CorE.reflection()< 19 or timer.time()>1100:
                    if sensor_CorD.reflection()< 19 or sensor_CorE.reflection()< 19 :
                        Drive.brake()
                        achou += 1
                    elif sensor_CorD.reflection()> 20 and sensor_CorE.reflection()> 20 and timer.time()>1000   : 
                        guinada("D", 45, 100)
                        Drive.straight(40)
                
                        timer.reset()
                if achou == 1:
                    break
                
            while True:
                seguir_Linha(6, 55)
                verifica_verde()
                FitaRED()
                Obstaculo()
                if hub.imu.tilt()[0] > 0:
                    break

    elif (hub.imu.tilt()[0] < -1 and hub.imu.tilt()[0] > -4) and (sensor_CorD.reflection() > 30 and sensor_CorE.reflection() > 30):
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
            seguir_Linha2(4, 40)
            verifica_verde()
            
           
            if hub.imu.tilt()[0] < 2:
                Drive.brake()
                Garra.dc(-100)
                wait(1000)
                Garra.dc(100)
                wait(700)
                Drive.straight(-50)
                guinada("D",20,100)
                timer.reset()
                while True :
                    mover(-60)
                    if sensor_CorD.reflection()< 19 or sensor_CorE.reflection()< 19:
                        Drive.brake()
                        timer.reset()
                        while True :
                            seguir_Linha(3, 55)
                            identifica_sala()  # 5, 72 # CURVA  > 5 < 19 AND > 20 < 42 4.2 , 75
                            verifica_verde()
                            FitaRED()
                            curvalombada()
                            if timer.time() > 500:
                                Drive.brake()
                                return 0
    
            if hub.imu.tilt()[0] > 60:
                Drive.brake()
                Garra.dc(-100)
                wait(2000)
                Garra.dc(100)
                wait(2000)
                Drive.straight(-60)
                timer.reset()
                guinada("D", 20, 100)
                while True :
                    mover(-60)
                    if sensor_CorD.reflection()< 19 or sensor_CorE.reflection()< 19:
                        Drive.brake()
                        break 
                while True :
                    seguir_Linha(3, 55)
                    identifica_sala()  # 5, 72 # CURVA  > 5 < 19 AND > 20 < 42 4.2 , 75
                    verifica_verde()
                    FitaRED()
                    curvalombada()
                    if timer.time() > 500:
                        Drive.brake()
                        return 0
                        

    if hub.imu.tilt()[0] > 60:
        Drive.brake()
        Garra.dc(-100)
        Drive.brake()
        wait(1500)
        Drive.brake()
        wait(800)
        Garra.dc(100)
        Drive.brake()
        wait(1000)
        Drive.straight(-60)
        guinada("D", 20, 100)
        while True :
            mover(-60)
            if sensor_CorD.reflection()< 19 or sensor_CorE.reflection()< 19:
                Drive.brake()
                break 
        timer.reset()        
        while True :
            seguir_Linha(3, 55)
            identifica_sala()  # 5, 72 # CURVA  > 5 < 19 AND > 20 < 42 4.2 , 75
            verifica_verde()
            FitaRED()
            curvalombada()
            if timer.time() > 500:
                Drive.brake()
                break

def Obstaculo():

    from resgate_de_vitimas import identifica_sala
    from seguimento_de_linha import seguir_Linha
    if UltrassonicoF.distance() <= 70:
        hub.speaker.beep(500,100)
        timer.reset()
        Drive.straight(-30)
        guinada("D",30,100)
        Drive.straight(30)
        girar_absoluto(55)
        hub.speaker.beep(500,100)
        if UltrassonicoF.distance() <= 70:
            while True :
                left_Motor.dc(60)
                right_Motor.dc(60)
                if UltrassonicoF.distance() <= 60:
                    break
            guinada("E",90,60)
            movimentoobs()
        else:
            while True:
                if UltrassonicoF.distance() <= 100:
                    while True :
                        left_Motor.dc(60)
                        right_Motor.dc(60)
                        if UltrassonicoF.distance() <= 60:
                            break
                    guinada("E",90,60)
                    movimentoobs()

                    return 0
                    
                guinada("E",90,55)
                Drive.brake()
                wait(60)
        
                

def movimentoobs():
    hub.imu.reset_heading(0)
    while True :  
        left_Motor.dc(100) 
        right_Motor.dc(41)
        
        if hub.imu.heading()>89:
            Drive.brake()
            while True :
                left_Motor.dc(-60) 
                right_Motor.dc(-60)
                if any(numero > 250 for numero in separar_dados('I')):
                    Drive.brake()
                    break
            while True :
                left_Motor.dc(60) 
                right_Motor.dc(60)
                if any(numero < 250 for numero in separar_dados('I')) or  sensor_CorD.reflection()<15:
                    if sensor_CorE.reflection()<15 or sensor_CorD.reflection()<15:
                        Drive.straight(40)
                        guinada("E",90,90)
                        while True:
                            left_Motor.dc(60) 
                            right_Motor.dc(-60)
                            if sensor_CorE.reflection()<15 or sensor_CorD.reflection()<15 :
                                Drive.straight(-20)
                                return 0
                    else :
                        Drive.brake()
                        hub.imu.reset_heading(0)
                        break
                    
            while True :
                left_Motor.dc(60) 
                right_Motor.dc(60)
                if any(numero > 250 for numero in separar_dados('I')) or  sensor_CorD.reflection()<15:
                    if sensor_CorE.reflection()<15 or sensor_CorD.reflection()<15:
                        Drive.straight(40)
                        guinada("E",90,90)
                        while True:
                            left_Motor.dc(60) 
                            right_Motor.dc(-60)
                            if sensor_CorE.reflection()<15 or sensor_CorD.reflection()<15 :
                                Drive.straight(-20)
                                return 0
                
                    else :
                        Drive.brake()
                        Drive.straight(-30)
                        hub.imu.reset_heading(0)
                        break
                

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

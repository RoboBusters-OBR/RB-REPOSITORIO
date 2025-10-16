# obstaculos_trajeto
from config import hub, left_Motor, right_Motor, Drive, UltrassonicoF, timer, Garra, my_colors, sensor_CorD, sensor_CorE, Color
from movimentos_bases import guinada, mover
from pybricks.tools import wait



def rampa():
    from seguimento_de_linha import seguir_Linha, verifica_verde, FitaRED, curvalombada,seguir_Linha2,curvabrusca
    from resgate_de_vitimas import identifica_sala
    if hub.imu.tilt()[0] < -15 :
        Drive.brake()
        wait(200)
        print('RAMPA')
        Garra.run_angle(90, -170)
        contador = 0
        timer.reset()
        while True:
            # 5, 72 # CURVA  > 5 < 19 AND > 20 < 42 4.2 , 75
            seguir_Linha(0.9, 100)

            FitaRED()
            if hub.imu.tilt()[0] < -45 and contador== 0:
                Drive.brake()
                wait(500)
                Garra.dc(-100)
                wait(1200)
                Drive.use_gyro(True)
                Drive.straight(200)
                Drive.use_gyro(False)
                contador += 1


                
            
            if hub.imu.tilt()[0] >-1 and timer.time() > 500:
                if hub.imu.tilt()[0] > 6 and hub.imu.tilt()[0] < 40 :
                    Drive.straight(-30)
                    print("aqui voltando")
                    break 
                elif hub.imu.tilt()[0] > -1 and hub.imu.tilt()[0] <10 :
                    Drive.brake()
                    wait(500)
                    Garra.dc(100)
                    wait(800)
                    break
                

        if hub.imu.tilt()[0] < 2 and hub.imu.tilt()[0] > -40:
            print(hub.imu.tilt()[0] )
            print("AQUI")
            Drive.straight(30)
            guinada("E",30,90)
            while True:
        
                mover(90)
                if sensor_CorE.reflection()< 30 :
                    Drive.straight(-10)
                    break
            while True:
        
                seguir_Linha(5, 60)
                verifica_verde()
                FitaRED()
                Obstaculo()
                #curvabrusca()
                if hub.imu.tilt()[0] < -15 :
                    rampadupla()
                    
                if hub.imu.tilt()[0] >10:#AQUI ELE IDENTIFICA QUE TA DESCENDO A RAMPA 
                    while True:
                        seguir_Linha2(4, 40)
                        if hub.imu.tilt()[0] <3:
                            print("Descendo rapido")
                            guinada("D", 20, 100)
                            timer.reset()
                            achou = 0
                            while True :
                                if achou == 1:
                                    return 0 
                                mover(-80)
                                if sensor_CorD.reflection()< 19 or sensor_CorE.reflection()< 19 or timer.time()>1100:
                                    if sensor_CorD.reflection()< 25 or sensor_CorE.reflection()< 25 :
                                        Drive.brake()
                                        Drive.straight(-10)
                                        achou += 1
                                        return 0
                    
                                    elif sensor_CorD.reflection()> 30 and sensor_CorE.reflection()> 30 and timer.time()>1000   : 
                                        guinada("D", 30, 100)
                                        Drive.straight(30)
                                        
                                        timer.reset()
                                    
                                if achou == 1:
                                    return 0
                                """if proucurou == 4:
                                    guinada("D", 30, 100)
                                    return 0"""
            
        elif hub.imu.tilt()[0] > 7 and hub.imu.tilt()[0] < 40:
            print("OUTRO AQUI")
            Drive.brake()
            Garra.dc(100)
            wait(800)
            Garra.dc(-100)
            wait(700)
            Garra.dc(100)
            wait(700)
            Drive.straight(20)
            if sensor_CorD.reflection()> 50 and sensor_CorE.reflection()>50:
                guinada("D", 20, 100)
                timer.reset()
                achou = 0
                while True :
                    if achou == 1:
                        break
                    mover(-70)
                    if sensor_CorD.reflection()< 19 or sensor_CorE.reflection()< 19 or timer.time()>1100:
                        if sensor_CorD.reflection()< 25 or sensor_CorE.reflection()< 25 :
                            Drive.brake()
                            Drive.straight(-10)
                            achou += 1
                            return 0
        
                        elif sensor_CorD.reflection()> 30 and sensor_CorE.reflection()> 30 and timer.time()>1000   : 
                            guinada("D", 50, 100)
                            Drive.straight(30)
                    
                            timer.reset()
                        break 
                    if achou == 1:
                        break

    if (hub.imu.tilt()[0] <= -2 and hub.imu.tilt()[0] > -6) :
        print('LOMBADA')
        timer.reset()
        while True:
            seguir_Linha(3, 55)
            identifica_sala()
            if timer.time() >1000:
                Drive.brake()
                print('Acabou o tempo da lombada')
                break
        timer.reset()
        while True:
            
            if timer.time() >2000 or (hub.imu.tilt()[0] > 10 and hub.imu.tilt()[0] < 40) or  hub.imu.tilt()[0] > 0 or hub.imu.tilt()[0] < -7  :
                Drive.brake()
                print('Acabou o tempo da lombada')
                return 0
            print(hub.imu.tilt()[0])   
            seguir_Linha(3, 55)
            print(sensor_CorE.reflection(),sensor_CorD.reflection())
            identifica_sala()  # 5, 72 # CURVA  > 5 < 19 AND > 20 < 42 4.2 , 75
            #verifica_verde()
            Obstaculo()
            FitaRED()
            #curvalombada()

    if hub.imu.tilt()[0] > 10 and hub.imu.tilt()[0] < 40:
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
                guinada("D", 20, 100)
                timer.reset()
                achou = 0
                while True :
                    if achou == 1:
                        return 0
                    mover(-60)
                    if sensor_CorD.reflection()< 19 or sensor_CorE.reflection()< 19 or timer.time()>1100:
                        if sensor_CorD.reflection()< 25 or sensor_CorE.reflection()< 25 :
                            Drive.brake()
                            Drive.straight(-10)
                            achou += 1
                            return 0
        
                        elif sensor_CorD.reflection()> 30 and sensor_CorE.reflection()> 30 and timer.time()>1000   : 
                            guinada("D", 30, 100)
                            Drive.straight(40)
                    
                            timer.reset()
                    
                    if achou == 1:
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
    if UltrassonicoF.distance() <= 60:
        Drive.straight(-10)
        guinada('E', 35, 80)
        while True:
            left_Motor.dc(70) 
            right_Motor.dc(-70) 
            if UltrassonicoF.distance() <= 70:
              break
        guinada('E', 70, 80)     
        movimentoobs()

def movimentoobs():
    hub.imu.reset_heading(0)
    Drive.straight(200)
    guinada("D",89,100)
    Drive.straight(350)
    guinada("D",89,100)
    Drive.straight(170)
    """while True :  
        left_Motor.dc(100) 
        right_Motor.dc(30)
        
        if hub.imu.heading()>175:
            guinada("E",110,90)
            Drive.straiight(-40)"""
    while True:
        left_Motor.dc(-80) 
        right_Motor.dc(80)
        if sensor_CorD.reflection()<25 :
            Drive.straight(-20)
            return 0
            """Drive.brake()
            Drive.straight(20)
            guinada("D",89,100)
            Drive.sttraight(400)
            guinada("D",89,100)
            Drive.straight(20)
            
            while True :
                print(separar_dados("I"))
                left_Motor.dc(-60) 
                right_Motor.dc(-60)
                if any(numero < 250 for numero in separar_dados('I')):
                    Drive.brake()
                    break
            while True :
                print(separar_dados("I"))
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
                        Drive.straight(60)
                        guinada("E",150,90)
                        while True:
                            left_Motor.dc(80) 
                            right_Motor.dc(-80)
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
                        Drive.straight(60)
                        guinada("E",150,90)
                        while True:
                            left_Motor.dc(80) 
                            right_Motor.dc(-80)
                            if sensor_CorE.reflection()<15 or sensor_CorD.reflection()<15 :
                                Drive.straight(-30)
                                return 0
                
                    else :
                        Drive.brake()
                        Drive.straight(-30)
                        hub.imu.reset_heading(0)
                        break               
"""
def separar_dados(tipo):
    inteiros = []
    strings = []

    # Obtenha os dados da função
    tuplaultra = hub.ble.observe(41)

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

def rampadupla():
    from seguimento_de_linha import seguir_Linha, verifica_verde, FitaRED,seguir_Linha2,curvabrusca
    
    if hub.imu.tilt()[0] < -15 :
        Drive.brake()
        wait(200)
        print('RAMPA')
        Garra.run_angle(90, -170)
        timer.reset()

        while True:
            
            seguir_Linha(0.9, 100)
            verifica_verde()
            FitaRED()
            
            if hub.imu.tilt()[0] > -1 and timer.time() > 500:
                if hub.imu.tilt()[0] > 5 and hub.imu.tilt()[0] < 40 :
                    Drive.straight(-30)
                    break 
                else :
                    Drive.brake()
                    wait(500)
                    Garra.dc(100)
                    wait(800)
                    break
                

        if hub.imu.tilt()[0] < 2 and hub.imu.tilt()[0] > -40:
            print(hub.imu.tilt()[0] )
            print("AQUI")
            Drive.straight(30)
            guinada("E",30,100)
            while True:
        
                mover(90)
                if sensor_CorE.reflection()< 30 :
                    break
            while True:
        
                seguir_Linha(5, 60)
                verifica_verde()
                FitaRED()
                Obstaculo()
                if hub.imu.tilt()[0] >10:#AQUI ELE IDENTIFICA QUE TA DESCENDO A RAMPA 
                    while True:
                        seguir_Linha2(4, 40)
                        if hub.imu.tilt()[0] <3:
                            print("Descendo rapido")
                            guinada("D", 20, 100)
                            timer.reset()
                            achou = 0
                            while True :
                                if achou == 1:
                                    return 0 
                                mover(-60)
                                if sensor_CorD.reflection()< 19 or sensor_CorE.reflection()< 19 or timer.time()>1100:
                                    if sensor_CorD.reflection()< 25 or sensor_CorE.reflection()< 25 :
                                        Drive.brake()
                                        Drive.straight(-10)
                                        achou += 1
                                        return 0
                    
                                    elif sensor_CorD.reflection()> 30 and sensor_CorE.reflection()> 30 and timer.time()>1000   : 
                                        guinada("D", 30, 100)
                                        Drive.straight(30)
                                        
                                        timer.reset()
                                    
                                if achou == 1:
                                    return 0
# Caderno de Programação - RoboBusters

O objetivo deste caderno é auxiliar os juízes a avaliarem o processo de desenvolvimento do nosso robô, apresentando a programação de forma organizada e explicada.

---

## Arquivo: `main.py`

```python
from config import sensor_CorE, sensor_CorD, Garra, left_Motor, right_Motor, sensor_CorD, sensor_CorE, UltrassonicoF, Color, timer, hub, Axis
from seguimento_de_linha import seguir_Linha, verifica_verde, curvabrusca, FitaRED
from resgate_de_vitimas import identifica_sala
from obstaculos_trajeto import Obstaculo, rampa, separar_dados
from pybricks.tools import wait
from pybricks.pupdevices import Motor

Garra.dc(100)
wait(1000)
Garra.stop()

while True:
  seguir_Linha(5, 80) #5, 80
  curvabrusca()
  verifica_verde()
  FitaRED()
  Obstaculo()
  rampa()
  identifica_sala()
```
### Explicação do módulo

Este módulo é responsável por **executar as funções principais** do robô, rodando continuamente em loop e identificando todos os desafios do trajeto.

As funções utilizadas são:

- **`seguir_Linha(5, 80)`**  
  Executa o seguidor de linha proporcional, utilizando:  
  - `KP = 5` → constante de proporcionalidade.  
  - `Velocidade = 80` → velocidade de movimentação.  

- **`curvabrusca()`**  
  Detecta e executa curvas muito fechadas, que o seguidor proporcional não consegue realizar sozinho.  

- **`verifica_verde()`**  
  Identifica **interseções e becos sem saída**.  
  Decide se deve ignorar o marcador ou realizar a movimentação correspondente.  

- **`FitaRED()`**  
  Detecta a **fita vermelha**, utilizada para marcar a área de chegada.  

- **`Obstaculo()`**  
  Verifica se há um **obstáculo** no trajeto e, caso positivo, executa a movimentação de desvio adequada.  

- **`rampa()`**  
  Detecta **mudanças de inclinação** no trajeto (rampas, lombadas ou irregularidades).  
  Utiliza o **IMU (giroscópio)** para ajustar o comportamento do robô de acordo com a situação.  

- **`identifica_sala()`**  
  Reconhece a **sala de resgate** quando o robô chega até ela.  
  Executa os movimentos necessários para entrar, realizar o **resgate das vítimas** e sair da área de resgate.  

## Arquivo: `config.py`

```python
from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from pybricks.parameters import Axis
from pybricks.tools import multitask, run_task

# Inicializa o hub com canal de comunicação
hub = InventorHub(top_side=Axis.Z, front_side=Axis.Y, broadcast_channel=1, observe_channels=[2])

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

# Inicialização de leitura de cor na superfície
sensor_CorE.color(surface=True)

# Variável auxiliar para contagem de cantos verdes
canto_verde = 0
```
### Explicação do módulo

O módulo `config.py` é responsável por **configurar e inicializar todos os componentes físicos do robô**, definindo sensores, motores, parâmetros e constantes que serão utilizados durante a execução do programa. Ele é essencial para garantir que todas as partes do robô estejam preparadas antes de qualquer ação.

As principais funções e configurações são:

- **Hub**  
  Inicializa o `InventorHub` com orientação definida (`top_side`, `front_side`) e canais de comunicação (`broadcast_channel`, `observe_channels`), permitindo comunicação entre hubs e dispositivos.

- **Motores**  
  - `Garra`: controla a garra do robô.  
  - `left_Motor`: motor da roda esquerda, configurado em sentido contrário (`COUNTERCLOCKWISE`) para sincronizar o movimento.  
  - `right_Motor`: motor da roda direita.  

- **DriveBase**  
  Configura o robô como um sistema de condução, definindo o diâmetro das rodas (`wheel_diameter`) e a distância entre eixos (`axle_track`), garantindo movimentos precisos.

- **Temporizador (`timer`)**  
  Inicializa e reseta um cronômetro para medir tempo durante a execução de ações no robô.

- **Sensores de cor**  
  - `sensor_CorE`: sensor de cor posicionado no lado esquerdo do robô.  
  - `sensor_CorD`: sensor de cor posicionado no lado direito.  
  Ambos configurados para detectar cores específicas.

- **Sensor ultrassônico**  
  - `UltrassonicoF`: mede distâncias à frente do robô, permitindo detectar obstáculos.

- **Definição de cores personalizadas**  
  Cores como preto, verde, branco, cinza, vermelho e prata são definidas com valores HSV personalizados para maior precisão na detecção pelo robô.

- **Lista de cores detectáveis**  
  Configura os sensores para reconhecer somente as cores definidas, evitando leituras incorretas.

- **Inicialização de leitura de cor**  
  Ativa a leitura inicial do sensor esquerdo para preparar a navegação.

- **Variável auxiliar (`canto_verde`)**  
  Utilizada para armazenar a contagem de cantos verdes detectados durante o trajeto, auxiliando na lógica de decisão.

## Arquivo: `seguimento_de_linha.py`

```python
from config import sensor_CorE, sensor_CorD, left_Motor, right_Motor, Drive, timer, Color
from movimentos_bases import mover, guinada
from pybricks.tools import wait
from config import hub 
from resgate_de_vitimas import identifica_sala
from obstaculos_trajeto import Obstaculo, rampa

def seguir_Linha(KP, velocidade_base):
    erro = (sensor_CorE.reflection()) - (sensor_CorD.reflection()) 
    correcao = erro * KP
    esquerda_power = velocidade_base + correcao 
    direita_power = velocidade_base - correcao 
    left_Motor.dc(esquerda_power)
    right_Motor.dc(direita_power)

def verifica_verde():
    if sensor_CorE.color() == Color.GREEN or sensor_CorD.color() == Color.GREEN:
        timer.reset()
        while timer.time() < 150 :
            seguir_Linha(1,40)
        Drive.brake()
    
        if sensor_CorE.color() == Color.GREEN and sensor_CorD.color() == Color.GREEN:
            timer.reset()
            while True:
                if (sensor_CorE.reflection() < 15 or sensor_CorE.reflection() > 40) and sensor_CorE.color() != Color.GREEN and (sensor_CorE.reflection() < 15 or sensor_CorE.reflection() > 40) and sensor_CorE.color() != Color.GREEN:
                    Drive.brake()
                    break
                left_Motor.dc(-60)
                right_Motor.dc(-60)
            if sensor_CorD.reflection() < 15:
                hub.speaker.beep(500,100)
                left_Motor.dc(100)
                right_Motor.dc(100)
                wait(200)
                Drive.brake()
                while True:
                    mover(100)
                    if sensor_CorE.reflection() < 40:
                        Drive.stop()
                        break   
            elif sensor_CorE.reflection() > 40:
                hub.speaker.beep(500,100)
                left_Motor.dc(90) 
                right_Motor.dc(90) 
                wait(450)
                guinada('E', 200, 100)
                while True:
                    mover(100)
                    if sensor_CorE.reflection() < 20:
                        Drive.stop()
                        break
                Drive.straight(-15)
        
        if sensor_CorE.color() == Color.GREEN and sensor_CorD.color() != Color.GREEN:
            Drive.brake()
            timer.reset()
            timer.reset()
            
            while True:
                if (sensor_CorE.reflection() < 15 and sensor_CorE.reflection() > 5 and sensor_CorE.color() != Color.GREEN  or sensor_CorE.reflection() > 50 and sensor_CorE.color() != Color.GREEN ) :
                    Drive.brake()

                    break
                left_Motor.dc(-60)
                right_Motor.dc(-60)
            if sensor_CorD.reflection() < 15:
                hub.speaker.beep(500,100)
                left_Motor.dc(100)
                right_Motor.dc(100)
                wait(200)
                Drive.brake()
                while True:
                    mover(100)
                    if sensor_CorE.reflection() < 25:
                        Drive.stop()
                        break   
            elif sensor_CorE.reflection() > 50:
                hub.speaker.beep(500,100)
                left_Motor.dc(90) 
                right_Motor.dc(90) 
                wait(450)
                guinada('E', 95, 100)
                while True:
                    mover(100)
                    if sensor_CorE.reflection() < 20:
                        Drive.stop()
                        break
        if sensor_CorD.color() == Color.GREEN and sensor_CorE.color() != Color.GREEN :
            Drive.brake()
            hub.speaker.beep(500,100)
            
            timer.reset()

            while True:
                if (sensor_CorD.reflection() < 15 and sensor_CorD.reflection() > 5 and sensor_CorD.color() != Color.GREEN  or sensor_CorD.reflection() > 50 and sensor_CorD.color() != Color.GREEN ) :
                    Drive.brake()
                    break
                left_Motor.dc(-70)
                right_Motor.dc(-70)
            wait(200)
            if sensor_CorD.reflection() < 15:
                hub.speaker.beep(500,100)
                left_Motor.dc(100)
                right_Motor.dc(100)
                wait(200)
                Drive.brake()
                while True:
                    mover(-100)
                    if sensor_CorD.reflection() < 28:
                        Drive.stop()
                        break   
            elif sensor_CorD.reflection() > 50:
                hub.speaker.beep(500,100)
                left_Motor.dc(90) 
                right_Motor.dc(90) 
                wait(450)
                guinada('D', 95, 100)
                while True:
                    mover(-100)
                    if sensor_CorD.reflection() < 28:
                        Drive.stop()
                        break 

def curvabrusca():
    # código omitido para brevidade
    pass

def FitaRED():
    if sensor_CorD.color() == Color.RED or sensor_CorD.color() == Color.RED:
        hub.ble.broadcast(2)
        Drive.stop()
        wait(1000000)

def curvalombada():
    # código omitido para brevidade
    pass

def seguir_Linha2(KP, velocidade_base):
    erro = sensor_CorE.reflection() - (sensor_CorD.reflection() + 2)
    correcao = erro * KP
    correcao = max(-15, min(15, correcao))
    esquerda_power = velocidade_base + correcao
    direita_power = velocidade_base - correcao
    esquerda_power = max(0, min(velocidade_base, esquerda_power))
    direita_power = max(0, min(velocidade_base, direita_power))
    left_Motor.dc(esquerda_power)
    right_Motor.dc(direita_power)

def mapp(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
```
### Explicação do módulo

O módulo `seguimento_de_linha.py` é responsável por implementar a lógica do **seguimento de linha** e detectar situações especiais ao longo do trajeto do robô. Ele contém funções para controle proporcional da movimentação, identificação de interseções, curvas bruscas, lombadas e a fita de chegada.

As principais funções são:

- **`seguir_Linha(KP, velocidade_base)`**  
  Implementa o algoritmo de seguimento proporcional. Calcula o erro entre os sensores de cor e aplica uma correção proporcional (`KP`) à velocidade base, garantindo que o robô mantenha-se alinhado à linha.

- **`verifica_verde()`**  
  Detecta interseções ou becos sem saída marcados pela cor verde. Baseia suas decisões nas leituras dos sensores de cor e luminosidade. Executa movimentos que proucuram por linha atrás dos marcadores verdes para saber se deve ignorar ou atravessar a interseção, mantendo a navegação precisa.

- **`curvabrusca()`**  
  Detecta e executa curvas fechadas que o seguidor proporcional não consegue realizar sozinho. Utiliza leituras dos sensores de cor e luminosidade e dados do IMU para corrigir a rota e garantir movimentações precisas, garantindo uma transição suave e precisa.

- **`FitaRED()`**  
  Detecta a fita vermelha que marca o final do percurso. Quando identificada, o robô para completamente e envia um sinal via Bluetooth para o hub, interrompendo todas as atividades do robô.

- **`curvalombada()`**  
  Variante do algoritmo de detecção de curva brusca, ajustada para operar em velocidade reduzida durante a passagem por redutores de velocidade. Essencial para garantir que o robô mantenha precisão na trajetória, evitando movimentos bruscos no próprio eixo.

- **`seguir_Linha2(KP, velocidade_base)`**  
  Variante do algoritmo de seguimento proporcional, com correção limitada para evitar movimentos bruscos. Ajusta a potência dos motores dentro de limites definidos, sendo especialmente útil em descidas de rampas, onde o robô precisa manter precisão sem gerar movimentos abruptos no próprio eixo.

- **`mapp(x, in_min, in_max, out_min, out_max)`**  
  Função utilitária para realizar mapeamento de valores. Converte uma faixa de entrada para outra faixa de saída, sendo essencial para ajustes finos nos sensores e controle de movimentos.

## Arquivo: `obstaculos_trajeto.py`

```python 
# obstaculos_trajeto
from config import hub, left_Motor, right_Motor, Drive, UltrassonicoF, timer, Garra, my_colors, sensor_CorD, sensor_CorE, Color
from movimentos_bases import guinada, mover, girar_absoluto
from pybricks.tools import wait



def rampa():
    from seguimento_de_linha import seguir_Linha, verifica_verde, FitaRED, curvalombada,seguir_Linha2
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
                Garra.dc(100)
                wait(700)
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
                Garra.dc(-100)
                wait(2000)
                Garra.dc(100)
                wait(2000)
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
        Garra.dc(-100)
        Drive.brake()
        wait(1500)
        Drive.brake()
        wait(800)
        Garra.dc(100)
        Drive.brake()
        wait(1000)
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
                return 0


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

```
### Explicação do módulo

O módulo `obstaculos_trajeto.py` é responsável por detectar e tratar mudanças no trajeto do robô, como rampas, lombadas e obstáculos, garantindo a continuidade e segurança da navegação. Ele utiliza sensores como IMU, ultrassônico e sensores de cor para ajustar a movimentação do robô de forma inteligente.

As principais funções são:

- **`rampa()`**  
  Detecta mudanças na inclinação do percurso usando o sensor IMU e ajusta o comportamento do robô para subir, descer ou atravessar áreas elevadas e redutores de velocidade.  
  Dependendo da inclinação detectada, o robô executa diferentes estratégias de movimento, como ajuste de velocidade, curvas, frenagens e movimentações específicas da garra.

- **`Obstaculo()`**  
  Detecta obstáculos à frente usando o sensor ultrassônico. Caso um obstáculo seja identificado, o robô realiza uma sequência de manobras para contorná-lo, incluindo frenagem, curvas, movimento de recuo e nova trajetória, os principais sensores utilizados são o IMU, sensores de cor e luminosidade para identificar linhas  
  Essa função também chama **`movimentoobs()`** para realizar a movimentação de desvio.

- **`movimentoobs()`**  
  Executa a lógica detalhada de desvio de obstáculos, combinando movimentos dos motores e leituras dos sensores para garantir que o robô volte à linha correta após o desvio.  
  Utiliza o sensor IMU para manter orientação e faz ajustes finos usando os sensores de cor.

- **`separar_dados(tipo)`**  
  Função utilitária que recebe dados do canal Bluetooth e separa valores inteiros de strings. Retorna uma lista específica de acordo com o parâmetro `tipo`:
  - `'S'` → retorna apenas strings.
  - `'I'` → retorna apenas inteiros.  
  Isso permite processar dados recebidos de sensores remotos ou outros dispositivos conectados.

## Arquivo: `movimentos_base.py`

```python
#movimentos_bases
from config import left_Motor, right_Motor, Drive, hub, Axis
from pybricks.tools import wait
def mover(GIRO):
    left_Motor.dc(GIRO)
    right_Motor.dc(-GIRO)

def guinada(LADO, GRAUS, VELOCIDADE):  
    hub.imu.reset_heading(0)
    if LADO == 'D':
        while True:
            mover(VELOCIDADE)
            if hub.imu.heading() >= GRAUS:
                Drive.brake()
                break
    else:
        while True:
            mover(-VELOCIDADE)
            if hub.imu.heading() <= -GRAUS:
                Drive.brake()
                break

def girar_absoluto(velocidade):
    """
    Gira o robô até um ângulo absoluto 'destino' usando IMU.
    - direita = negativo
    - esquerda = positivo
    Compensa qualquer erro automaticamente.
    """
    while True:
        

        if hub.imu.rotation(Axis.Z, calibrated=True) <=2 and hub.imu.rotation(Axis.Z, calibrated=True) >=-2:
            Drive.brake()
            break  # chegou no destino

        if hub.imu.rotation(Axis.Z, calibrated=True) <=0:         # precisa girar para direita
            left_Motor.dc(-velocidade)
            right_Motor.dc(velocidade)
        elif  hub.imu.rotation(Axis.Z, calibrated=True) >=0:
            left_Motor.dc(velocidade)
            right_Motor.dc(-velocidade)


    left_Motor.stop()
    right_Motor.stop()

```
### Explicação do módulo

O módulo `movimentos_bases.py` é responsável por controlar movimentos básicos do robô, principalmente rotações e guinadas, utilizando os motores e o sensor IMU para manter precisão no movimento.

As principais funções são:

- **`mover(GIRO)`**  
  Controla ambos os motores para girar o robô em torno do seu eixo.  
  O parâmetro `GIRO` define a potência aplicada: valores positivos giram em uma direção, valores negativos giram na direção oposta.

- **`guinada(LADO, GRAUS, VELOCIDADE)`**  
  Realiza uma guinada precisa em um determinado lado (`'D'` para direita ou qualquer outro valor para esquerda).  
  Utiliza o sensor IMU para medir o ângulo girado e parar o movimento assim que o ângulo desejado (`GRAUS`) for atingido.  
  O parâmetro `VELOCIDADE` define a velocidade da guinada.

- **`girar_absoluto(velocidade)`**  
  Gira o robô até alcançar um ângulo absoluto definido pelo sensor IMU.  
  Nesse caso, a função orienta o robô para o **ângulo zero absoluto**, definido no momento em que o robô é ligado.  
  Utiliza leituras contínuas do IMU para corrigir a rotação, parando automaticamente quando o alinhamento é atingido.

## Arquivo: `inferior_hub.py`

```python
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
```

### Explicação do módulo

O módulo controla a **lógica de comunicação entre os hubs**, além do **controle dos motores e sensores do hub de baixo**, utilizando o Hub do Spike Prime, sensores e motores. Ele faz uso de comunicação Bluetooth BLE para receber comandos e enviar dados em tempo real, gerenciando movimentações específicas da cancela conforme o cenário detectado. Essa programação é responsável por rodar no hub de baixo, observando leituras de sensores importantes para a área de resgate e em alguns casos do seguidor de linha.

- **Inicialização dos sensores e motores**  
  Define os sensores de cor (`CorD`), sensor ultrassônico (`UltrassonicoL`) e motor da cancela (`cancelaE`).  
  Configura também cores personalizadas para detectar tonalidades específicas no percurso e inicializa o temporizador (`timer`) e o hub.

- **Lógica principal (loop infinito)**  
  O robô fica em execução contínua verificando comandos via Bluetooth (`hub.ble.observe`) e atuando conforme o comando recebido.

  - **Comando `3`** → Abre a cancela completamente usando `cancelaE.run_target()`.  
  - **Comando `2`** → Abre parcialmente a cancela com movimento controlado e depois retorna.  
  - **Comando `"AREA_DE_RESGATE"`** → Executa uma rotina específica para resgate: abre a cancela parcialmente, coleta dados de distância do sensor ultrassônico, envia via Bluetooth (`hub.ble.broadcast`) e gerencia ações adicionais baseadas em comandos recebidos, como movimentações da cancela ou parada.

- **Rotina de detecção de cor**  
  Quando detectado o comando `"COR"` via Bluetooth, o robô entra em um loop onde captura a cor detectada pelo sensor `CorD`, envia o valor via Bluetooth e imprime no console até receber o comando `"PARAR"`.

- **Rotina de detecção apenas de distância**  
  Se não estiver em modo de resgate, o robô continua monitorando a distância com o sensor ultrassônico, envia os valores via Bluetooth e executa ações da cancela conforme os comandos recebidos (`2` ou `3`).

Esse módulo integra comunicação Bluetooth, controle de motores e leitura de sensores para criar uma gestão inteligente da cancela em diferentes situações de operação.

## Arquivo: `identifica_sala.py`
```python 

#resgate_de_vitimas
from config import (
    Garra, Drive, timer, left_Motor, right_Motor,
    sensor_CorD, sensor_CorE, UltrassonicoF, hub, Color 
)
from movimentos_bases import guinada, mover
from pybricks.tools import wait, run_task, multitask
from obstaculos_trajeto import Obstaculo, separar_dados


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
    from obstaculos_trajeto import rampa

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
                    Drive.straight(10)
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

                if any(item.startswith("Color.GREEN") for item in separar_dados("S")) or any(item.startswith("Color.GRENL") for item in separar_dados("S")) :
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
    

                if any(item.startswith("Color.RED") for item in separar_dados("S")):
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
                if any(item.startswith("Color.GREEN") for item in separar_dados("S")):
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
                    Drive.straight(70)
                    Drive.brake()
                    hub.imu.reset_heading(0)

                if any(item.startswith("Color.RED") for item in separar_dados("S")):
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
                    Drive.straight(70)
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

```
### Explicação do módulo

O módulo **`resgate_de_vitimas`** é responsável pela lógica de operação da sala de resgate. Ele coordena movimentos do robô, ações da garra e decisões baseadas nas leituras de sensores para realizar a missão de resgate, transportar vítimas e sair da sala.  

A programação utiliza funções assíncronas (`async`) para executar múltiplas tarefas simultaneamente, como movimentação do robô e operação da garra. O módulo integra sensores de cor, ultrassônicos e giroscópio, combinados com motores e o hub do Spike Prime, permitindo tomada de decisões em tempo real.  

A lógica de movimentação da sala de resgate é estruturada em um loop onde o robô percorre paralelamente às paredes da sala até que uma das condições principais seja detectada: presença de uma parede à frente, identificação de área de resgate, presença de saída à frente ou identificação da entrada da sala.  

Para cada condição, o robô executa uma ação específica seguida de verificações adicionais. Ao sair da sala após passar duas vezes pela área de resgate, o robô mantém a mesma lógica, mas também busca por uma saída lateral.

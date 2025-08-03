# Projeto Pybricks - Robô

## Passo a passo para rodar neste computador:

1. Instale o Python 3.10 ou superior: https://www.python.org/
2. Instale as dependências:
   pip install -r requirements.txt

3. Conecte seu hub LEGO com Pybricks Firmware via Bluetooth.
4. Dê dois cliques no arquivo "enviar.bat" para rodar o código no robô.

> Certifique-se de que o nome do hub seja "hub 6", ou edite o .bat para o nome correto.
pybricksdev scan ble, este comando escaneia os hubs proximos e seus nomes

Atualize o firmware do seu hub e a biblioteca Pybricksdev com:

   pip install --upgrade pybricksdev

COMANDO PARA ENVIAR O CODIGO VIA BLE :

   pybricksdev run ble main.py -n "NOME_DO_SEU_HUB"


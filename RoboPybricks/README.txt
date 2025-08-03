# RoboBusters - Projeto Pybricks

-Este é o repositório oficial do projeto de programação 
em Python da equipe de robótica **RoboBusters**, utilizando
o kit **LEGO Spike Prime** com o firmware **Pybricks**.

Nosso objetivo é desenvolver soluções eficientes e modulares 
para desafios da **RoboCupJunior Rescue Line**, utilizando 
boas práticas de programação, versionamento de código e 
colaboração em equipe.

----------------------------------------------------------

## Sobre a equipe RoboBusters ##

A **RoboBusters** é uma equipe de robótica educacional do 
SESI Ananindeua - PA, com destaque estadual, nacional e internacional. 
Desenvolvemos projetos com foco em inovação, trabalho em equipe e 
aplicação prática da tecnologia em competições como a OBR e a RoboCup, 
liga Rescue Line.

----------------------------------------------------------

## Objetivo do Projeto ##

Este repositório contém o código-fonte do robô programado com as bibliotecas 
**Pybricks**, incluindo controle de motores, sensores e estratégias 
inteligentes para navegação, identificação de obstáculos, resgate e
seguimento preciso do trajeto de linha.

----------------------------------------------------------
## Objetivo deste Repositório ##

Este projeto organiza toda a lógica de movimentação, resgate, tomada de decisões e sensores do robô. Aqui você encontra:

- Código-fonte principal (`main.py`)
- Módulos organizados em `utils/`
- Scripts de instalação e envio do código para o hub
- Dependências listadas em `requirements.txt`
- Um ambiente completo que pode ser configurado em qualquer máquina com **VS Code e internet**

----------------------------------------------------------

## Como preparar um notebook do zero ##

-Se você está usando um computador novo (apenas com VS Code instalado), siga os passos abaixo:

### 1. Instalar o Python 3.10 ou superior

Acesse: https://www.python.org/downloads/
Durante a instalação, marque a opção **"Add Python to PATH"**

----------------------------------------------------------

### 2. Clonar este repositório

Clone este repositório no VS Code via terminal:  
  
   git clone https://github.com/RoboBusters-OBR/RB-REPOSITORIO.git
   cd RB-REPOSITORIO

Clone este repositório no VS Code pelo VS Code: 
   Abra o VS Code e pressione `Ctrl + Shift + P`, depois:

   1. Escolha **"Git: Clone"**
   2. Cole o link do seu repositório GitHub
   3. Abra a pasta clonada no VS Code

----------------------------------------------------------

## Como usar Git pelo terminal do VS Code - Passo a passo completo ##

### Requisitos
- Git instalado no seu computador.  
- Projeto já iniciado com `git init` ou clonado com `git clone`.

--------------------------------

### 1. Abrir o terminal no VS Code
- No VS Code, vá em **Terminal > Novo Terminal**  
- Ou use o atalho: `` Ctrl + ` `` (crase)

---------------------------------


### 2. Verificar o status do repositório

```bash
git status

-------------------------------------------------------------

## Comandos basicos de Git e como usar junto do GitHub ##

# 1. Adicionar arquivos para o commit
# Para adicionar todos os arquivos modificados:
git add .

# Para adicionar um arquivo específico:
git add nome_do_arquivo.py

# 2. Fazer um commit (salvar as alterações localmente)
# Com uma mensagem explicativa:
git commit -m "Mensagem explicativa sobre a mudança"

# Exemplo:
git commit -m "Corrige bug na função de seguir linha"

# 3. Enviar as alterações para o GitHub (push)
git push

# Se for a primeira vez enviando um branch, use:
git push -u origin main
# ou, se seu branch for master:
git push -u origin master

# 4. Baixar atualizações do GitHub (pull)
git pull

# 5. Visualizar o histórico de commits
git log --oneline

# Fluxo típico de trabalho:
# Sempre que modificar arquivos, execute:
git status       # Verifica mudanças
git add .        # Adiciona todas as mudanças ao staging
git commit -m "Descrição do que mudou"  # Salva as mudanças localmente
git push         # Envia as mudanças para o GitHub


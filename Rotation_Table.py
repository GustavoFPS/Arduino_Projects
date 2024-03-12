import serial
from Exec_Aquisition import aquisition
import os 

# Configuração da porta serial
serial_port = '/dev/ttyUSB0'  # Verificar a porta serial
baud_rate = 9600
ser = serial.Serial(serial_port, baud_rate, timeout=1)

# Step
t = 0

# Nome do arquivo 
name = ""

# Cria a pasta com os dados 
os.mkdir(name)

diretorio = os.path.dirname(name)

while t <= 400:
    
    # Inicia a aquisição
    aquisition(name, t, diretorio)
     
    # Envia um sinal para o Arduino para iniciar a rotação
    ser.write(b'r')

    # Aguarda o sinal de rotação concluída enviado pelo Arduino
    while True:
        # Lê uma linha da porta serial que sinaliza o fim da rotação
        line = ser.readline().decode().strip()
        if line == "rotation_complete":
            print("Rotação concluída")
            break
        
    t += 1

# Salva o ultimo arquivo
aquisition(name, t)

# Fechamento da porta serial
ser.close()


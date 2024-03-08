import pyautogui as py
import time

# Armazena as imagens dos botões do programa de aquisição
botoes = ["botoes.png"]
tela = []

# Tempo para sair da sala
time.sleep(60) 
# Armazena as coordenadas dos botões na tela
for element in botoes:
    tela.append(py.locateOnScreen(element))

# Função de aquisição
def aquisition(name, t):
    """
    
    """ 
    # Salva o arquivo
    if t != 0:
        py.click(tela[0])
        py.write('{0}_aquisition{1}'.format(name, t - 1))
        py.press("enter")
    
    # Limpa aquisição
    py.click(tela[1])
    
    # Começa nova aquisição
    py.click(tela[2])
    
    
    
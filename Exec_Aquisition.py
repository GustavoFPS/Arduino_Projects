import pyautogui as py
import time

# Armazena as imagens dos botões do programa de aquisição
botoes = ["botao.png"]
tela = []

# Tempo para sair da sala
time.sleep(60) 
# Armazena as coordenadas dos botões na tela
for element in botoes:
    tela.append(py.locateOnScreen(element))

# Função de aquisição
def aquisition(name, t, diretorio):
    '''
    Automatiza a aquisição do espectro

    Parameters
    ----------
    name : string
        Nome do arquivo
    t : int
        Passo da interação

    Returns None
    -------
    '''
    
    # Salva o arquivo
    if t != 0:
        py.hotkey("ctrl", "s")
        py.write(str(diretorio))
        py.press("enter")
        py.write('{0}_aquisition{1}'.format(name, t - 1))
        py.press("enter")
    
    # Limpa aquisição
    py.hotkey("ctrl", "a")
    
    # Começa nova aquisição
    py.click(tela[0])
    
    
    
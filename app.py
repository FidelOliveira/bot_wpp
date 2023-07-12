import webbrowser
import pyautogui
import time
# Com somente é utilizado uma função do time, também seria possível from time import sleep (e utilizar apenas sleep())
    
telefones = ['Código do pais + DDD da região + Número de contato']

'''
# Caso tenha uma lista de contatos utilizando bloco de notas (exemplo)
telefones = []

with open('fones.txt','r') as arquivo:
    for linha in arquivo:
        telefones.append(linha.split('\n')[0])
    print(telefones)'''
      
 
for telefone in telefones:
    webbrowser.open(f'https://api.whatsapp.com/send?phone={telefone}')
    time.sleep(3)
    pyautogui.click(968,321,duration=1)
    time.sleep(3)
    pyautogui.click(1083,220,duration=1)
    time.sleep(3)
    pyautogui.click(764,981,duration=1)
    time.sleep(3)
    pyautogui.typewrite('Por favor, evitar ofender pessoas. Passar bem e tenha uma boa noite de sono.')
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(3)
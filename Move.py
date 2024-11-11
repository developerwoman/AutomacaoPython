#!/usr/bin/env python
# coding: utf-8

# In[21]:

import pyautogui as py
import time
import datetime
import webbrowser
import os
import logging


logging.basicConfig(level=logging.INFO, filename="logs.log", format="%(asctime)s - %(levelname)s - %(message)s")


py.PAUSE=1
print(os.environ)
E1 = datetime.time(8,4).strftime("%H:%M")
S1 = datetime.time(12,20).strftime("%H:%M")
E2 = datetime.time(13,15).strftime("%H:%M")
S2 = datetime.time(17,45).strftime("%H:%M")
url = "https://www.ahgora.com.br/novabatidaonline/?defaultDevice=a524560"

while True:
    
    if datetime.datetime.now().isoweekday() != 6 and datetime.datetime.now().isoweekday() != 7:
            print(datetime.datetime.now().isoweekday())
            current_time = datetime.datetime.now().strftime("%H:%M")
            current_date = datetime.datetime.now().strftime("%m/%d/%Y")

            if current_time == E1 or current_time == S1 or current_time == E2 or current_time == S2:
                
                logging.info("Aguarde...Data: " + current_date + " - Hora: " + datetime.datetime.now().strftime("%H:%M:%S"))

                #Código marcação de ponto

                #Abrir Url 
                webbrowser.open(url)
                time.sleep(5)   
                
                #maximiza tela
                py.hotkey('win', 'up')                
                time.sleep(1)
                
                #pega o retorno da posicao atual de x e y do mouse e passa o valor da tupla para as duas variaveis
                # x, y = py.position()
                # print("Registre seu ponto:")
                # print("x = "+str(x)+" y = "+str(y))

                #clica em Registre seu ponto
                py.click(x=1127, y=693)
                time.sleep(3)
                #clica em acessar via SSO
                py.click(x=960, y=825)
                time.sleep(5)
                
                #Confirmar batida
                # py.click(x=1007, y=756)
                time.sleep(5)                

                #fecha browser
                py.click(x=1339, y=12)
                
                #volta para notepad
                py.hotkey('alt', 'tab')
                time.sleep(2)

                time.sleep(60)
                
            else :
                logging.info("Nada a marcar - Data: " + current_date + " - Hora: " + datetime.datetime.now().strftime("%H:%M:%S"))
                time.sleep(8)        
    else:
        
        logging.info("Data: " + datetime.datetime.today().strftime("%A") + " - Hora: " + datetime.datetime.now().strftime("%H:%M:%S"))                
        logging.info("Aguardando por 1 horas")
        time.sleep(3600)
        
    
# código da empresa a524560
# matrícula 10237


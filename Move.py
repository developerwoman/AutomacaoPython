#!/usr/bin/env python
# coding: utf-8

# In[21]:

import pyautogui as py
import time
import datetime
import webbrowser
import os

py.PAUSE=1
print("ALESSANDRA")
print(os.environ)
E1 = datetime.time(8,4).strftime("%H:%M")
S1 = datetime.time(12,20).strftime("%H:%M")
E2 = datetime.time(13,15).strftime("%H:%M")
S2 = datetime.time(18,9).strftime("%H:%M")
url = "https://www.ahgora.com.br/novabatidaonline/?defaultDevice=a524560"

#abrir busca do windows
py.press("winleft")

#digitar Notepad
py.write("bloco de notas")
py.press("enter")

#maximizar notepad
py.hotkey('win', 'up')


# Abrir arquivo
# arquivo = open(r'C:/Users/T807409/Desktop/testePython.txt', "r")# Abra o arquivo (leitura)
# conteudo = arquivo.readlines()     

while True:
    
    if datetime.datetime.now().isoweekday() != 6 and datetime.datetime.now().isoweekday() != 7:
            print(datetime.datetime.now().isoweekday())
            current_time = datetime.datetime.now().strftime("%H:%M")
            current_date = datetime.datetime.now().strftime("%m/%d/%Y")

            if current_time == E1 or current_time == S1 or current_time == E2 or current_time == S2:
                
                py.write("Aguarde...Data: " + current_date + " - Hora: " + datetime.datetime.now().strftime("%H:%M:%S"))
                py.press("enter")
               
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

                #pega o retorno da posicao atual de x e y do mouse e passa o valor da tupla para as duas variaveis
                # x, y = py.position()
                # print("Registrar ponto:")
                # print("x = "+str(x)+" y = "+str(y))
                
                #Confirmar batida
                # py.click(x=1007, y=756)
                time.sleep(5)                

                #fecha browser
                py.click(x=1339, y=12)
                
                #volta para notepad
                py.hotkey('alt', 'tab')
                time.sleep(2)

                py.write("___________________________________________________")
                py.press("enter")
                time.sleep(60)
                
            else :
                py.write("Nada a marcar - Data: " + current_date + " - Hora: " + datetime.datetime.now().strftime("%H:%M:%S"))
                py.press("enter")
                time.sleep(8)        
    else:
        
        py.write("wkn Hora" + datetime.datetime.now().strftime("%H:%M:%S") + "Data: " + datetime.datetime.today().strftime("%A") + "(" + str(datetime.datetime.now().isoweekday()) + ")")
        py.press("enter")
        time.sleep(8)


    # arquivo = open(r'C:/Users/T807409/Desktop/testePython.txt', "w") # Abre novamente o arquivo (escrita)
    # arquivo.writelines(conteudo)    # escreva o conteúdo criado anteriormente nele.
    # arquivo.close()            
# código da empresa a524560
# matrícula 10237


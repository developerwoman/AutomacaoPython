#!/usr/bin/env python
# coding: utf-8

# In[21]:

from calendar import weekday
import pyautogui as py
import time
import pyperclip
import datetime

py.PAUSE=1

E1 = datetime.time(8,4).strftime("%H:%M")
S1 = datetime.time(12,20).strftime("%H:%M")
E2 = datetime.time(13,15).strftime("%H:%M")
S2 = datetime.time(18,0).strftime("%H:%M")

#abrir busca do windows
py.press("winleft")

#digitar Notepad
py.write("notepad")
py.press("enter")

#maximizar notepad
with py.hold('alt'): 
    py.press("space")
    py.press("x")


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
               
                #Código marcação de ponto

                #Abrir Chrome 
                py.press("winleft")
                py.write("Chrome")
                py.press("enter")
                time.sleep(2)   
                
                #maximiza tela
                with py.hold('alt'): 
                        py.press("space")
                        py.press("x")
                time.sleep(1)
                
                #clica no perfil Nava
                py.click(x=683, y=441)
                
                #testar se tela ja ta maximizada
                with py.hold('alt'): 
                        py.press("space")
                        py.press("x")
                
                # py.click(x=1227, y=101)
                py.click(x=182, y=162)
                #focus na barra de endereço
                py.click(x=397, y=51)

                #Copiar e colar endereço 
                url = "https://www.ahgora.com.br/novabatidaonline/?defaultDevice=a524560"
                pyperclip.copy(url)
                py.hotkey("ctrl", "v")
                py.press("enter")
                time.sleep(15)

                #pegar position Registre seu ponto
                py.click(x=667, y=442)
                time.sleep(1)

                #acessar via SSO
                py.click(x=685, y=575)
                time.sleep(10)

                #escolher conta
                py.click(x=645, y=368)
                time.sleep(10)

                #Confirmar batida
                py.click(x=723, y=520)
                time.sleep(8)

                #fecha browser
                py.click(x=1339, y=12)

                py.write("___________________________________________________")
                time.sleep(60)
                
            else :
                py.write("Sem - Data: " + current_date + " - Hora: " + datetime.datetime.now().strftime("%H:%M:%S") + " ___________________________________________________ ")
                time.sleep(8)        
    else:
        
        py.write("wkn Hora" + datetime.datetime.now().strftime("%H:%M:%S") + "Data: " + datetime.datetime.today().strftime("%A") + "(" + str(datetime.datetime.now().isoweekday()) + ")")
        time.sleep(8)


    # arquivo = open(r'C:/Users/T807409/Desktop/testePython.txt', "w") # Abre novamente o arquivo (escrita)
    # arquivo.writelines(conteudo)    # escreva o conteúdo criado anteriormente nele.
    # arquivo.close()            



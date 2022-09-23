#!/usr/bin/env python
# coding: utf-8

# In[4]:
import pyautogui as py
import time
import pyperclip
from datetime import datetime

py.PAUSE = 1

dt = datetime.now()
#print ("Datetime is :", dt)
print("Weekday is:", dt.isoweekday())
#current_time = dt.strftime("%H:%M:%S")
#print("Current Time is :", current_time)

if dt.isoweekday() != 6 and dt.isoweekday() != 7:
   
        #Abrir Chrome 
        py.press("winleft")
        py.write("Chrome")
        py.press("enter")
        time.sleep(2)   
        #maximiza tela
        py.click(x=1125, y=33)
        time.sleep(1)
        #clica no perfil
        py.click(x=417, y=435)
        #testar se tela ja ta maximizada
        py.click(x=1214, y=27)
        
        #focus na barra de endereço
        py.click(x=397, y=51)

        #Copiar e colar endereço (https://navasoftware127725.rm.cloudtotvs.com.br/FrameHTML/Web/App/RH/PortalMeuRH/#/login)
        pyperclip.copy("https://navasoftware127725.rm.cloudtotvs.com.br/FrameHTML/Web/App/RH/PortalMeuRH/#/login")
        py.hotkey("ctrl", "v")
        py.press("enter")
        time.sleep(10)

        #pegar position campo login e campo senha
        py.click(x=291, y=388, clicks=2)
        py.write ("07389")
        py.press("tab")
        py.write("31105125807")
        py.press("enter")
        time.sleep(5)

        #pegar position seta Ponto
        py.click(x=233, y=322)

        #pegar position Relógio e click
        py.click(x=81, y=469)
        time.sleep(3)

        #pegar poistion Bater Ponto (moveRel())
        py.click(x=805, y=405)
        time.sleep(3)
        py.dragTo(905, 505, 2, button="left")
        #deslogar
        py.click(x=1329, y=126)
        py.click(x=1237, y=328)
        #fecha browser
        py.click(x=1339, y=12)
        
#
#
#
#
#
#
#


# In[5]:


#import time
#import pyautogui

#time.sleep(5)
#pyautogui.position()


# In[ ]:





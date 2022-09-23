from calendar import weekday
import pyautogui as py
import time
import pyperclip
import os


arquivo = open(r'C:/Users/T807409/Desktop/testePython.txt', "r")# Abra o arquivo (leitura)
conteudo = arquivo.readlines()  
conteudo.append('_____Alessandra')   # insira seu conteúdo

arquivo = open(r'C:/Users/T807409/Desktop/testePython.txt', "w") # Abre novamente o arquivo (escrita)
arquivo.writelines(conteudo)    # escreva o conteúdo criado anteriormente nele.
print(conteudo)
arquivo.close()


# while True:
#     line = data.readline()
#     print(line)
#     if ("" == line):
#         print("file finished")
#         break;
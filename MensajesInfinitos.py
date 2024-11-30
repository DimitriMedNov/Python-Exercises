import pyautogui as spam
import time

limite = input('Numero de mensajes:')
mensaje = input('Que mensaje quieres enviar?:')

i = 0

time.sleep(5)

while i < int (limite):
    spam.typewrite(mensaje)
    spam.press('Enter')
    i+1
    print('Enviado')




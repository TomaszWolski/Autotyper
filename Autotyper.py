import pyautogui
import time
numbers = range(1,10) #ilosc powtorzeni
for number in numbers:
    time.sleep(2) #czas miedzy powtorzeniami
    pyautogui.typewrite('tekst do kopiowania')
    pyautogui.press('enter')
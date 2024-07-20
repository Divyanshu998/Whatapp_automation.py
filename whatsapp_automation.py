import pyautogui
import time
time.sleep(3)
count = 0
while count<100:
    pyautogui.typewrite("kya haal chal")
    pyautogui.press("enter")
    count = count+1
    time.sleep(1)
    
    
    
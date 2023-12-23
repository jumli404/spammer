import pyautogui as auto
import time

counter = 0

while counter < 1000: 
    auto.write(str(counter))
    auto.press('enter')
    counter += 1
    time.sleep(0)  

print("Finished typing.")



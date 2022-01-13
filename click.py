import timeit
from time import sleep
import pyautogui
import win32api

print("Register click location - Left click, Start - enter, Stop - esc")

pyautogui.PAUSE = 0.01
start = False
been_clicked = 0
click_pos = []
num1 = 0
num2 = 2

left_Key = win32api.GetKeyState(0x01)
enter_Key = win32api.GetKeyState(0x0D)

#detect click and stores pos
while True:
    # when left click is clicked store the pos and make the been_clicked var to true
    if left_Key < 0:
        been_clicked = 1
        x1, y1 = pyautogui.position()
        click_pos.extend([x1, y1])
        sleep(1)
        print(f"okay location at {click_pos[num1:num2]} has been registered. Press enter to start or esc to stop ")
        num1 += 2
        num2 += 2

    # when enter key is clicked we will check if we have already clicked using the been_clicked var and warn when it is not
    elif enter_Key < 0:
        if been_clicked == 1:
            start = True
            break
        else:
            sleep(1)
            print("please register click location first")
            continue
#move to the click pos
while start:
    try:
        pyautogui.click(x1, y1)
        # stops program if esc key is pressed
        if win32api.GetKeyState(0x1B) < 0:
            break
    except pyautogui.FailSafeException:
        print("A error has occured closing the program")
        break
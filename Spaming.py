import pyautogui
import time
import random, string

number = input("Enter number of messages:")

time.sleep(5)

for i in range(int(number)):
    strg = string.ascii_uppercase
    message ="".join(random.sample(strg, 10)) # 10 characters long
    pyautogui.typewrite(message)
    pyautogui.press('Enter')
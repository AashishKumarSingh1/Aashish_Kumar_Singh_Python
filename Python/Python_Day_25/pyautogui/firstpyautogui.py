#Mouse Controller

#function -> 1) size(), position()

import pyautogui
pyautogui.PAUSE=2.5
x,y=pyautogui.size()
print(x,y)

mouse_x,mouse_y=pyautogui.position()
print(mouse_x,mouse_y)

while True:
    mouse_x,mouse_y=pyautogui.position()
    pyautogui.sleep(2)
    print(mouse_x,mouse_y)
    pyautogui.alert('Good Morning!')
    pyautogui.write("Hello! , I am Aashish Kumar Singh!")
    pyautogui.sleep(3)

import pyautogui

x,y=pyautogui.size()
print(x,y)
while False:
    print(pyautogui.position())
    pyautogui.sleep(2)

print(pyautogui.onScreen(500,700))
pyautogui.moveTo(500,700,2)
pyautogui.moveRel(100,100,4)

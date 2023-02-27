#mouse function

import pyautogui
pyautogui.onScreen(100,10)

import pyautogui
print(pyautogui.size())

import pyautogui
print(pyautogui.position())

import pyautogui
print(pyautogui.moveRel())

import pyautogui
print(pyautogui.moveTo(200,0,duration=1.5))

import pyautogui
print(pyautogui.dragRel())

import pyautogui
print(pyautogui.displayMousePosition())


####### Keyboard Functions
#write
import pyautogui
import time
time.sleep(5)
pyautogui.click(300,1060)
pyautogui.write("# Hello world!",0.25)

#hotkey
import pyautogui
import time
time.sleep(5)

pyautogui.click(300,1060)
pyautogui.keyDown('ctrl')
pyautogui.keyDown('c')
pyautogui.keyUp('c')
pyautogui.keyUp('ctrl')


#Screenshot And Image Recognition
#locateOnScreen
import pyautogui
 
box = pyautogui.locateOnScreen("chrome_icon.png")
pyautogui.moveTo(box.left, box.top, duration = 1)
print(box) 

 
#locateCenterOnScreen
import pyautogui
 
x, y= pyautogui.locateCenterOnScreen("chrome_icon.png")
pyautogui.moveTo(x, y, duration = 1)
print(x, y)

#screenshot
import pyautogui
img = pyautogui.screenshot(region=(0, 0, 400, 300))
import pyautogui
import keyboard
import time
import win32api, win32con 

# x: 660: y: 500
# x: 760: y: 500
# x: 860: y: 500
# x: 950: y: 500

def ClickOn(X, Y):
    win32api.SetCursorPos((X, Y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    # will stop of 0.1S
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)



while keyboard.is_pressed(' ') == False:
    if pyautogui.pixel(660, 500) == (0, 0, 0):
      ClickOn(660, 500)
    elif pyautogui.pixel(760, 500) == (0, 0, 0):
      ClickOn(760, 500)
    
    elif pyautogui.pixel(860, 500) == (0, 0, 0):
      ClickOn(860, 500)
    
    elif pyautogui.pixel(950, 500) == (0, 0, 0):
      ClickOn(950, 500)
    
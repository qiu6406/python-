from tkinter import *
import os,subprocess
import pyautogui
import win32gui,win32api,win32con
class App:
    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        self.button = Button(
            frame, text="后退", fg="red", command=self.back,height=5, width=10
            )
        self.button.pack(side=RIGHT)

        self.hi_there = Button(
            frame, text="主页", command=self.say_hi,height=5, width=10
            )
        self.hi_there.pack(side=LEFT)

    def back(self):
        #pyautogui.hotkey('altleft','left')
        if(win32gui.FindWindow("Chrome_WidgetWin_1",None)==0):
            return 
        handler = win32gui.FindWindow("Chrome_WidgetWin_1",None)
        #print(handler)
        #print(win32gui.GetClassName(handler))
        win32gui.SetForegroundWindow(handler)
        pyautogui.hotkey('ctrl', 'w')
        if(win32gui.FindWindow("Chrome_WidgetWin_1",None)==0):
            self.say_hi()
    def say_hi(self):
        subprocess.Popen("C:\\Users\\Administrator\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe --kiosk http://www.changshalib.cn/xsdxx")

root = Tk()
root.wm_attributes('-topmost',1)

app = App(root)

root.mainloop()
root.destroy() # optional; see description below
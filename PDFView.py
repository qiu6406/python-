#coding=utf-8
from tkinter import *
import os,subprocess
import pyautogui
import win32gui,win32api,win32con
class App:
    def __init__(self, master):

        frame = Frame(master)
        frame.pack()
        
        self.button = Button(
            frame, text="下一页", command=self.forward,height=5, width=10
            )
        self.button.pack(side=RIGHT)

        self.hi_there = Button(
            frame, text="首页", command=self.home,height=5, width=10
            )
        self.hi_there.pack(side=RIGHT)

        self.hi_there = Button(
            frame, text="上一页", command=self.backward,height=5, width=10
            )
        self.hi_there.pack(side=RIGHT)
        subprocess.Popen("FoxitReader.exe E:\desktop\jfinal-3.3-manual.pdf")

    def forward(self):
        #pyautogui.hotkey('altleft','left')
        if(win32gui.FindWindow("classFoxitReader",None)==0):
            print("没找到")
            return 
        handler = win32gui.FindWindow("classFoxitReader",None)
        #print(handler)
        #print(win32gui.GetClassName(handler))
        win32gui.SetForegroundWindow(handler)
        pyautogui.hotkey('right')
        if(win32gui.FindWindow("classFoxitReader",None)==0):
            self.home()
    def home(self):
        if(win32gui.FindWindow("classFoxitReader",None)==0):
            subprocess.Popen("FoxitReader.exe E:\desktop\jfinal-3.3-manual.pdf")
        else:
            handler = win32gui.FindWindow("classFoxitReader",None)
            win32gui.SetForegroundWindow(handler)
            pyautogui.hotkey('home')
    def backward(self):
        if(win32gui.FindWindow("classFoxitReader",None)==0):
            subprocess.Popen("FoxitReader.exe E:\desktop\jfinal-3.3-manual.pdf")
        else:
            handler = win32gui.FindWindow("classFoxitReader",None)
            win32gui.SetForegroundWindow(handler)
            pyautogui.hotkey('left')

def close(self):
    return

root = Tk()
root.geometry("1920x90+0+0") 
root.wm_attributes('-topmost',1)
root.resizable(0, 0)
root.overrideredirect(True)

app = App(root)

root.mainloop()
root.destroy() # optional; see description below
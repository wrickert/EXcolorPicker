import sys
import tkinter as tk
#from PIL import Image, ImageTk
from tkinter import *
from lifxlan import * #BLUE, COLD_WHITE, CYAN, GOLD, GREEN, LifxLAN, ORANGE, PINK, PURPLE, RED, WARM_WHITE, WHITE, YELLOW
def __init__():
    status = 65530

lifxlan = LifxLAN()

#Define our lights
#This is the mini
#one = Light("d0:73:d5:30:7b:d9", "192.168.0.111")
one = Light("d0:73:d5:20:e0:98", "192.168.0.104")
#This is the other one
#two = Light("d0:73:d5:20:93:d5", "192.168.0.109")

status = 0

win = tk.Tk()

win.title("Zoe and Eliot's Awesome Color Picker!!")
win.overrideredirect(True)

#=========This is the line that works for fullscreen======
#win.geometry("{0}x{1}+0+0".format(win.winfo_screenwidth(), win.winfo_screenheight()))

def checkPower():
    status = one.get_power()
    if status < 300:
        one.set_power(65535, 1000, rapid=True)
        two.set_power(65535, 1000, rapid=True)
        dim.set(65535)
    print(status)

def whiteBtn():
    print('white')
    checkPower()
    one.set_color(WHITE, rapid=True)
    two.set_color(WHITE, rapid=True)

def offBtn():
    print('off')
    if one.get_power() < 300:
        one.set_power(65535, 1000, rapid=True)
        two.set_power(65535, 1000, rapid=True)
        dim.set(65535)
    else:
        one.set_power(0, 1000, rapid=True)
        two.set_power(0, 1000, rapid=True)
        dim.set(0)
        status = 0

def redBtn():
    print('red') 
    checkPower()
    one.set_color(RED, rapid=True)
    two.set_color(RED, rapid=True)

def bluBtn():
    print('blue')
    checkPower()
    one.set_color(BLUE, rapid=True)
    two.set_color(BLUE, rapid=True)

def greenBtn():
    print('green')
    checkPower()
    one.set_color(GREEN, rapid=True)
    two.set_color(GREEN, rapid=True)

def pinkBtn():
    print('pink')
    checkPower()
    one.set_color(PINK, rapid=True)
    two.set_color(PINK, rapid=True)

def purpleBtn():
    print('purple')
    checkPower()
    one.set_color(PURPLE, rapid=True)
    two.set_color(PURPLE, rapid=True)

def orangeBtn():
    print('orange')
    checkPower()
    one.set_color(ORANGE, rapid=True)
    two.set_color(ORANGE, rapid=True)
    
def yellowBtn():
    print('yellow') 
    checkPower()
    one.set_color(YELLOW, rapid=True)
    two.set_color(YELLOW, rapid=True)

#minor annoyance, to set the brightness you have to set hue,saturation,and color
def doDim(value):
    hue = one.get_color()
    one.set_hue(hue[0], rapid=True)
    one.set_saturation(hue[1], rapid=True)
    one.set_brightness(value, rapid=True)
    one.set_colortemp(hue[3], rapid=True)

    two.set_hue(hue[0], rapid=True)
    two.set_saturation(hue[1], rapid=True)
    two.set_brightness(value, rapid=True)
    two.set_colortemp(hue[3], rapid=True)
    
#Set our 9 buttons
white = Button(win, text="WHITE", command=whiteBtn)
off = Button(win, text="ON/OFF", command=offBtn)
red = Button(win, text="RED", command=redBtn, background='red' )
blue = Button(win, text="BLUE ", command=bluBtn, bg="blue")
green = Button(win, text="GREEN ", command=greenBtn, bg="green" )
pink = Button(win, text="PINK", command=pinkBtn, bg="pink" )
purple = Button(win, text="PURPLE", command=purpleBtn, bg="purple" )
orange = Button(win, text="ORANGE", command=orangeBtn, bg="orange" )
yellow = Button(win, text="YELLOW", command=yellowBtn, bg="yellow" )

#Global height and width settings
x = 33
y = 8

white.grid(row = 3, column = 1, sticky = W)
white.config(height=y, width=x)
off.grid(row = 3, column = 3, sticky = W)
off.config(height=y, width=x)
red.config(height=y, width=x)
red.grid(row = 1, column = 1, sticky = W)
red.config(height=y, width=x)
red.config(height=y, width=x)
blue.grid(row = 1, column = 2, sticky = W)
blue.config(height=y, width=x)
green.grid(row = 1, column = 3, sticky = W)
green.config(height=y, width=x)
pink.grid(row = 2, column = 1, sticky = W)
pink.config(height=y, width=x)
purple.grid(row = 2, column = 2, sticky = W)
purple.config(height=y, width=x)
orange.grid(row = 2, column = 3, sticky = W)
orange.config(height=y, width=x)
yellow.grid(row = 3, column = 2, sticky = W)
yellow.config(height=y, width=x)

#Lets try for a dimmer
dim = Scale(win, from_=0, to=65535, orient=HORIZONTAL, width=20, length=500, sliderlength= 40, command=doDim)
dim.set(65535)
dim.grid(sticky = S, columnspan=4, pady=10)

win.mainloop()

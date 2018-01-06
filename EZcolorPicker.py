import sys
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import *
from lifxlan import * #BLUE, COLD_WHITE, CYAN, GOLD, GREEN, LifxLAN, ORANGE, PINK, PURPLE, RED, WARM_WHITE, WHITE, YELLOW

lifxlan = LifxLAN()

#Define our lights
#This is the mini
one = Light("d0:73:d5:30:7b:d9", "192.168.0.111")
two = Light("d0:73:d5:20:93:d5", "192.168.0.109")

win = tk.Tk()

win.title("Zoe and Eliot's Awesome Color Picker!!")
win.overrideredirect(True)

#=========This is the line that works for fullscreen======
#win.geometry("{0}x{1}+0+0".format(win.winfo_screenwidth(), win.winfo_screenheight()))

#redjImg = Image.open("red.jpg")
#redImg = ImageTk.PhotoImage(redjImg)
#blueImg = Image.open("blue.jpg")

def whiteBtn():
    print('white')
    one.set_color(WHITE)
    two.set_color(WHITE)

def offBtn():
    print('off')
    one.set_color()
    two.set_color()

def redBtn():
    print('red') 
    one.set_color(RED)
    two.set_color(RED)

def bluBtn():
    print('blue')
    one.set_color(BLUE)
    two.set_color(BLUE)

def greenBtn():
    print('green')
    one.set_color(GREEN)
    two.set_color(GREEN)

def pinkBtn():
    print('pink')
    one.set_color(PINK)
    two.set_color(PINK)

def purpleBtn():
    print('purple')
    one.set_color(PURPLE)
    two.set_color(PURPLE)

def orangeBtn():
    print('orange')
    one.set_color(ORANGE)
    two.set_color(ORANGE)
    
def yellowBtn():
    print('yellow') 
    one.set_color(YELLOW)
    two.set_color(YELLOW)

white = Button(win, text="WHITE", command=whiteBtn)
off = Button(win, text="OFF", command=offBtn)
red = Button(win, text="RED", command=redBtn, background='red' )
blue = Button(win, text="BLUE ", command=bluBtn, bg="blue")
green = Button(win, text="GREEN ", command=greenBtn, bg="green" )
pink = Button(win, text="PINK", command=pinkBtn, bg="pink" )
purple = Button(win, text="PURPLE", command=purpleBtn, bg="purple" )
orange = Button(win, text="ORANGE", command=orangeBtn, bg="orange" )
yellow = Button(win, text="YELLOW", command=yellowBtn, bg="yellow" )

white.grid(row = 4, column = 1, sticky = W)
white.config(height=10, width=40)
off.grid(row = 4, column = 3, sticky = W)
off.config(height=10, width=40)
red.config(height=10, width=40)
red.grid(row = 1, column = 1, sticky = W)
red.config(height=10, width=40)
red.config(height=10, width=40)
blue.grid(row = 1, column = 2, sticky = W)
blue.config(height=10, width=40)
green.grid(row = 1, column = 3, sticky = W)
green.config(height=10, width=40)
pink.grid(row = 2, column = 1, sticky = W)
pink.config(height=10, width=40)
purple.grid(row = 2, column = 2, sticky = W)
purple.config(height=10, width=40)
orange.grid(row = 2, column = 3, sticky = W)
orange.config(height=10, width=40)
yellow.grid(row = 4, column = 2, sticky = W)
yellow.config(height=10, width=40)

win.mainloop()

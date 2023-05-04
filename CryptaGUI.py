#!/usr/bin/python3
#https://realpython.com/python-gui-tkinter/#displaying-clickable-buttons-with-button-widgets

#Notes:

#Imports
import tkinter as tk
from CryptaCipher import enc,dec

#Setup Window
window = tk.Tk()
window.rowconfigure([0,1,2,3,4,5], minsize=0, weight=1)
window.columnconfigure([0,1,2], minsize=10, weight=1)
window.title("Crypta 3 - GUI")
#Title
greeting = tk.Label(text="-Crypta GUI-")
greeting.grid()

#Key Input
keylabel = tk.Label(text="Enter key (int):")
keyentry = tk.Entry(fg="darkred",bg="white",width=25)
keylabel.grid(row=2,column=0)
keyentry.grid(row=2, column=2)

#Message Input
textlabel = tk.Label(text="Enter Text: ")
textin = tk.Entry(fg="darkred",bg="white",width=25)
textlabel.grid(row=3, column=0)
textin.grid(row=3, column=2)

#Action Button Setup
ptbutton = tk.Button(
    text="Encrypt",
    width=25,
    height=5,
    bg="lightgrey",
    fg="black"
)
ptbutton.grid(row=4, column=0)

decbutton = tk.Button(
    text="Decrypt",
    width=25,
    height=5,
    bg="lightgrey",
    fg="black"
)
decbutton.grid(row=4, column=2)

#Output Messages
outputmessagel = tk.Label(text="Previous Encrypt")
outputmessager = tk.Label(text="Previous Decrypt")

outputmessagel.grid(row=5, column=0)
outputmessager.grid(row=5, column=2)

#Event Handle Functions

#Encrypt
def encbuttonf(event):
    output = ""
    message = textin.get()
    key = keyentry.get()
    result = enc(key,message)
    output = key + "/ " + result
    resultout = tk.Label(text=(output))
    window.clipboard_append (result)
    resultout.grid(row=6, column=0)


#Decrypt
def decbuttonf(event):
    output = ""
    decmessage = textin.get()
    key = keyentry.get()
    result = dec(key,decmessage)
    output = key + "/ " + result
    resultout = tk.Label(text=(output))
    window.clipboard_append (result) # This is the process of copying to the clipboard
    resultout.grid(row=6, column=2)


#Setup Button Bind to Function
ptbutton.bind("<Button-1>", encbuttonf)
decbutton.bind("<Button-1>",decbuttonf)

#Mainloop
window.mainloop()

from tkinter import *
from tkinter import messagebox

def ok():
    messagebox.showinfo('What`s happen?', 'You just clicked OK button !')

def cancel():
    messagebox.showinfo('What`s happen now?', 'You just CANCEL it!')
    
def close():
    messagebox.showinfo('What`re you doing right now?!', 'You clicked the exit button bro! Good Bye!')

def main():
    window=Tk()
    topB = Button(window, text = 'OK', fg = 'red', bg = 'black', command = ok)
    bottomB = Button(window, text = 'CANCEL', fg = 'black', bg = 'red', command = cancel)
    topB.pack(fill=X)
    bottomB.pack(side='bottom', fill=X)
    window.mainloop()

main()
#if you close the window, you will receive the close() messagebox.
if(close()):
    exit
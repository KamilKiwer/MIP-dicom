from tkinter import *
from tkinter import filedialog as fd
from pydicom import *
import glob
from PIL import Image, ImageTk
import os
from numpy import *


class obraz:
    def __init__(s):
        s.pix = []
        s.zdj = ImageTk
        s.canvas = Canvas(root)
        s.pixl = []
        s.zdjl = ImageTk
        s.click = 0
        s.b = 0


    def fun(s, pix):
        s.canvas.destroy()
        if len(pix) > 0:
            s.pix = rot90(pix, 1, (1,0))
            print(pix)
            szerokosc = 1024
            wysokosc = 512
            s.canvas = Canvas(root, width=szerokosc, height=wysokosc)
            s.canvas.pack(side='right')
            s.rys()






    def rys(s):
        s.canvas.delete('all')
        s.zdj = ImageTk.PhotoImage(image=Image.fromarray(s.pix[1]))
        s.canvas.create_image(0, 0, anchor="nw", image=s.zdj)



    def wczytaj(s, path):
        pix = []
        if os.path.isdir(path):
            for file in glob.glob(path + '/*.dcm'):
                ds = dcmread(file)
                pix.append(ds.pixel_array)
        return pix



    def obrot(s):
        s.click=s.click+1




root = Tk()
root.state('zoomed')
root.title('MIP')

pole = obraz()

menu = Frame(root)
menu.pack(side='left', padx=20, pady=20)

title = Label(menu, text='MIP', font=('Arial', 20))
title.pack()

button1 = Button(menu, text='wybierz folder', command=lambda: pole.fun(pole.wczytaj(fd.askdirectory())))
button1.pack()

button2 = Button(menu, text='obróć', command=lambda: pole.obrot())
button2.pack()

root.mainloop()


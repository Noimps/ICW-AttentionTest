import tkinter as tk
from PIL import Image, ImageTk
from tkinter import Frame, Label, Button
import pygame
import time

class ShowLetter(Frame):

    def __init__(self):
        self.beeps = [  './Peeps/beepMid.mp3', './Peeps/beepLaag.mp3', './Peeps/beepHoog.mp3',  './Peeps/beepMid.mp3', './Peeps/beepLaag.mp3',  './Peeps/beepMid.mp3',]
        self.pijlen = [  './Pijlen/Hoog.png', './Pijlen/Laag.png', './Pijlen/Midden.png',  './Pijlen/Hoog.png', './Pijlen/Midden.png', './Pijlen/Laag.png']
        self.player = pygame.mixer
        self.player.init()
        super().__init__()
        self.master.title("Bedrijf Omzetter")
        self.configure(background="white", height=800, width=1500)
        self.pack()
        
        self.lf = ('Helvetica', 14)
        self.Test1Button = Button(self, text="Test 1", command=self.test1)
        self.Test1Button.place(x=350, y=700)

        self.counter1 = 0
        self.counter2 = 0
        self.counter3 = 0

        self.Test2Button = Button(self, text="Test 2", command=self.test2)
        self.Test2Button.place(x=450, y=700)
        

        
        self.AHoog = Button(self, text= " Piep Hoog", command=self.Ahoog)
        self.AMid = Button(self, text= "Piep Mid", command=self.Amid)
        self.ALaag = Button(self, text= "Piep Laag", command=self.Alaag)
        self.AHoog.place(x=100, y=640)
        self.AMid.place(x=100, y=670)
        self.ALaag.place(x=100, y=700)
        
        self.PHoog = Button(self, text= " Pijl Hoog", command=self.Phoog)
        self.PMid = Button(self, text= "Pijl Mid", command=self.Pmid)
        self.PLaag = Button(self, text= "Pijl Laag", command=self.Plaag)
        self.PHoog.place(x=200, y=640)
        self.PMid.place(x=200, y=670)
        self.PLaag.place(x=200, y=700)
        
    def Phoog(self):
        imagetest1 = Image.open(f"{self.pijlen[0]}")
        self.fotopijl = ImageTk.PhotoImage(imagetest1)
        self.TestFoto = Label(self, image=self.fotopijl, bd=0, highlightthickness=0)
        self.TestFoto.place(x=500, y=150)

        self.after(1000, lambda: self.hide_image())
    def Pmid(self):
        imagetest1 = Image.open(f"{self.pijlen[2]}")
        self.fotopijl = ImageTk.PhotoImage(imagetest1)
        self.TestFoto = Label(self, image=self.fotopijl, bd=0, highlightthickness=0)
        self.TestFoto.place(x=500, y=150)

        self.after(1000, lambda: self.hide_image())

    def Plaag(self):
        imagetest1 = Image.open(f"{self.pijlen[1]}")
        self.fotopijl = ImageTk.PhotoImage(imagetest1)
        self.TestFoto = Label(self, image=self.fotopijl, bd=0, highlightthickness=0)
        self.TestFoto.place(x=500, y=150)

        self.after(1000, lambda: self.hide_image())

    def Ahoog(self):
        self.player.music.load(self.beeps[2]) 
        self.player.music.play()
    
    def Amid(self):
        self.player.music.load(self.beeps[0]) 
        self.player.music.play()

    def Alaag(self):
        self.player.music.load(self.beeps[1]) 
        self.player.music.play()

    def test1(self):
        self.counter1 += 1
        if self.counter1 > 6: 
            self.counter1 = 1

        # Show the "kruis" image
        imagekruis = Image.open(f"./Pijlen/Kruis.png")
        self.fotokruis = ImageTk.PhotoImage(imagekruis)
        self.TestFoto = Label(self, image=self.fotokruis, bd=0, highlightthickness=0)
        self.TestFoto.place(x=675, y=300)

        self.after(1000, self.show_pijl)

    def test2(self):
        self.counter2 += 1
        if self.counter2 > 6:
            self.counter2 = 1
        
        imagekruis = Image.open(f"./Pijlen/Kruis.png")
        self.fotokruis = ImageTk.PhotoImage(imagekruis)
        self.TestFoto = Label(self, image=self.fotokruis, bd=0, highlightthickness=0)
        self.TestFoto.place(x=675, y=300)

        self.after(1000, lambda: self.peep(self.beeps[self.counter2 - 1]))

    def show_pijl(self):
        self.TestFoto.place_forget()  

        imagetest1 = Image.open(f"{self.pijlen[self.counter1 - 1]}")
        self.fotopijl = ImageTk.PhotoImage(imagetest1)
        self.TestFoto = Label(self, image=self.fotopijl, bd=0, highlightthickness=0)
        self.TestFoto.place(x=500, y=150)

        self.after(500, lambda: self.show_letter(1, self.counter1))

    def show_letter(self, test, counter):
        self.TestFoto.place_forget()  

        imagetest = Image.open(f"./Letters/Test{test}Letters{counter}.png")
        self.fototest = ImageTk.PhotoImage(imagetest)
        self.TestFoto = Label(self, image=self.fototest, bd=0, highlightthickness=0)
        self.TestFoto.place(x=300, y=125)

        self.after(200, self.hide_image)

    def peep(self, piepje):
        self.player.music.load(piepje) 
        self.player.music.play()

        self.after(500, lambda: self.done())

    def done(self):
        self.player.music.stop()
        self.show_letter(2, self.counter2)
        
    def hide_image(self):
        self.TestFoto.place_forget()

ShowLetter().mainloop()

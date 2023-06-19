import customtkinter as ctk
import tkinter as tk 
import pygame as pg
import PIL
pg.init()

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.APP_WIDTH = 500
        self.APP_HEIGHT = 500
        self.title("TriangleSound")
        self.SONG_END = pg.USEREVENT + 1
        self.geometry(f"{self.APP_WIDTH}x{self.APP_HEIGHT}+{100}+{100}")
        self.iconbitmap("images/logo.ico")
        self.resizable(False, False)
        self.LIST_BOX = tk.Listbox(master= self, 
                                   selectmode= tk.SINGLE, 
                                   width = 52,
                                   height= 37,
                                   bg= "#282828",
                                   font = ("Calibri", 10),
                                   fg = "white",
                                   selectbackground = "gray",
                                   activestyle = "none",
                                   selectforeground = "black")
            
        self.MUSIC_NAME = ctk.CTkLabel(master= self, text= self.LIST_BOX.get(tk.ACTIVE), font = ("Calibri", 20))
        self.MUSIC_NAME.place(x = 325,y = 20)
        self.LIST_BOX.place(x=20 , y=50)
        self.SCROLLBAR = ctk.CTkScrollbar(master=self, height = 398, bg_color= "gray", button_color="white", button_hover_color= "lightgray")
        self.SCROLLBAR.place(x = 254, y = 33)
        self.LIST_BOX.config(yscrollcommand= self.SCROLLBAR.set)
        self.SCROLLBAR.configure(command=self.LIST_BOX.yview)
        self.STOPPED = False
        


main_app = App()

         
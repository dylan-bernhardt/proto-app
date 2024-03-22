from typeguard import typechecked
import tkinter as tk 
from ..view import Home, Nav_bar, Level, Concentration, Settings

@typechecked
class App(tk.Tk) :   
    @typechecked
    def __init__(self)-> None :
        tk.Tk.__init__(self)
        self.__home = Home(self)
        self.__nav_bar = Nav_bar(self)
        self.__level = Level(self)
        self.__settings = Settings(self)
        self.__concentration = Concentration(self)
        self.__next_button = self.__home.get_button()
        self.__concentration_button = self.__nav_bar.get_concentration_button()
        self.__level_button = self.__nav_bar.get_level_button()
        self.__settings_button = self.__nav_bar.get_settings_button()
        self
        self.__home.pack(expand=True, fill='both')
        self.__next_button.config(command= self.next_button_handler)
        self.__concentration_button.config(command= self.concentration_button_handler)
        self.__level_button.config(command= self.level_button_handler)
        self.__settings_button.config(command= self.settings_button_handler)

    @typechecked
    def next_button_handler(self) -> None: 
        self.__home.pack_forget()
        self.__nav_bar.pack(fill= 'x')
        self.__level.pack(expand=True, fill= "both")

    @typechecked
    def concentration_button_handler(self) -> None: 
        self.__level.pack_forget()
        self.__settings.pack_forget()
        self.__concentration.pack(expand=True, fill="both")
    
    @typechecked
    def level_button_handler(self) -> None: 
        self.__concentration.pack_forget()
        self.__settings.pack_forget()
        self.__level.pack(expand= True, fill= 'both')

    @typechecked
    def home_button_handler(self) -> None:
        tk.Frame.__init__()
    
    @typechecked
    def settings_button_handler(self) -> None:
        self.__concentration.pack_forget()
        self.__level.pack_forget()
        self.__settings.pack(expand=True, fill='both') 
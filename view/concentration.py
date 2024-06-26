import tkinter as tk
from typeguard import typechecked
from tkinter import Canvas
from enum import Enum

class Color(Enum):
    VERT = "green",
    JAUNE = "yellow",
    ORANGE = "orange",
    ROUGE = "red"

    @classmethod
    def choose_color(cls, percentage):
        if percentage <= 25:
            return cls.ROUGE.value
        elif percentage <= 50:
            return cls.ORANGE.value
        elif percentage <= 75:
            return cls.JAUNE.value
        else:
            return cls.VERT.value


@typechecked
class Concentration(tk.Frame) : 
    def __init__(self, master : tk.Tk)-> None: 
        tk.Frame.__init__(self, master)
        self.configure(background='#111111')
        self.__frame = tk.Frame(self)
        self.__frame.config(background='#111111')
        self.__label = tk.Label(self.__frame, text= "The concentration in water is : ", bg= '#111111', fg='#7A7A7A', font=("Helvetica", 15))
        self.__value = tk.Label(self.__frame, bg= '#111111', fg='#7A7A7A', font=("Helvetica", 40))
        self.__canvas = Canvas(self.__frame, width=300, height=150, background='#111111',highlightthickness=0)
        self.__form_minmax = tk.Frame(self)
        self.__button_min = tk.Button(self.__form_minmax,
                            text='Set Min',
                            bg = '#111111',
                            borderwidth=0,
                            highlightthickness=0,
                            activebackground= '#111111',
                            fg="#7A7A7A")
        self.__button_max = tk.Button(self.__form_minmax,
                            text='Set Max',
                            bg = '#111111',
                            borderwidth=0,
                            highlightthickness=0,
                            activebackground= '#111111',
                            fg="#7A7A7A")
        self.__canvas.pack()    
        self.__label.pack()
        self.__value.pack()
        self.__form_minmax.pack(side='bottom', expand=True)
        self.__button_min.pack(side="left")
        self.__button_max.pack(side="right")
        self.__frame.pack(expand=True)

    @typechecked
    def get_value(self) -> tk.Label : 
        return self.__value

    @typechecked
    def set_concentration(self, concentration_measured : int, min : int, max : int )-> None: 
        percentage = (concentration_measured - min)*100/(max - min)
        self.__value.config(text=str(100 if percentage > 100 else abs(round(percentage, 1))) + ' %')
        self.__color = Color.choose_color(percentage)
        self.__canvas.delete("all")
        variable_angle = percentage * 1.8
        center_x, center_y = 150, 120
        radius1 = 100
        radius2 = 80
        start_angle = 0
        end_angle = 180
        coord1 = center_x - radius1, center_y - radius1, center_x + radius1, center_y + radius1
        coord2 = center_x - radius2, center_y - radius2, center_x + radius2, center_y + radius2
        coord3 = center_x - radius1 -1, center_y - radius1 - 1, center_x + radius1 + 1, center_y + radius1 + 1
        self.__canvas.create_arc(coord1, start=start_angle, extent=end_angle, fill=self.__color, outline="")
        self.__canvas.create_arc(coord2, start=start_angle, extent=end_angle, fill="#111111",outline="")
        self.__canvas.create_arc(coord3, start=-variable_angle, extent=end_angle, fill="#111111",outline="")

    @typechecked
    def get_min_button(self) -> tk.Button : 
        return self.__button_min
    
    @typechecked
    def get_max_button(self) -> tk.Button : 
        return self.__button_max
    
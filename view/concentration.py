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
        self.__label = tk.Label(self.__frame, text= "The concentration in ethanol is : ", bg= '#111111', fg='#343434', font=("Helvetica", 15))
        self.__value = tk.Label(self.__frame, bg= '#111111', fg='#7A7A7A', font=("Helvetica", 40))
        self.__canvas = Canvas(self.__frame, width=300, height=150, background='#111111',highlightthickness=0)
        self.__canvas.pack()    
        self.__label.pack()
        self.__value.pack()
        self.__frame.pack(expand=True)

    @typechecked
    def get_value(self) -> tk.Label : 
        return self.__value

    @typechecked
    def set_concentration(self, concentration_measured : int)-> None: 
        percentage = (concentration_measured - 520)*100/80
        self.__value.config(text=concentration_measured)
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

import tkinter as tk
from typeguard import typechecked
from tkinter import Canvas

@typechecked
class Concentration(tk.Frame) : 
    def __init__(self, master : tk.Tk)-> None: 
        tk.Frame.__init__(self, master)
        self.configure(background='#111111')
        self.__frame = tk.Frame(self)
        self.__frame.config(background='#111111')
        self.__label = tk.Label(self.__frame, text= "The concentration in ethanol is : ", bg= '#111111', fg='#343434', font=("Helvetica", 15))
        self.__value = tk.Label(self.__frame, text= "50%", bg= '#111111', fg='#7A7A7A', font=("Helvetica", 40))
        canvas = Canvas(self.__frame, width=300, height=150, background='#111111',highlightthickness=0)
        center_x, center_y = 150, 120
        radius1 = 100
        radius2 = 80
        start_angle = 0
        end_angle = 180
        coord1 = center_x - radius1, center_y - radius1, center_x + radius1, center_y + radius1
        coord2 = center_x - radius2, center_y - radius2, center_x + radius2, center_y + radius2
        jauge1 = canvas.create_arc(coord1, start=start_angle, extent=end_angle, fill="red", outline="")
        jauge2 = canvas.create_arc(coord2, start=start_angle, extent=end_angle, fill="#111111",outline="")
        canvas.pack()
        self.__label.pack()
        self.__value.pack()
        self.__frame.pack(expand=True)

    @typechecked
    def get_value(self) -> tk.Label : 
        return self.__value
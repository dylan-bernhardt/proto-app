import tkinter as tk
from typeguard import typechecked

@typechecked
class Level(tk.Frame) : 
    def __init__(self, master : tk.Tk)-> None: 
        tk.Frame.__init__(self, master)
        self.configure(background='#111111')
        self.__frame = tk.Frame(self)
        self.__frame.config(background='#111111')
        self.__label = tk.Label(self.__frame, text= "The level of fuel is : ", bg= '#111111', fg='#343434', font=("Helvetica", 15))
        self.__value = tk.Label(self.__frame, text= "50%", bg= '#111111', fg='#7A7A7A', font=("Helvetica", 40))
        self.__label.pack()
        self.__value.pack()
        self.__frame.pack(expand=True)

    @typechecked
    def get_value(self) -> tk.Label : 
        return self.__value
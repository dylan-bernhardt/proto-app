from typeguard import typechecked
import tkinter as tk

@typechecked
class Home : 
    @typechecked
    def __init__(self, root: tk.Tk, label : str) -> None: 
        self.__loadimage = tk.PhotoImage(file = "img/button.png" )
        self.__active = 1
        self.__label = tk.Label(root, text= label, bg= '#111111', fg='#7A7A7A', font=("Helvetica", 45))
        self.__button = tk.Button(root,
                                    command = self.button_handler,
                                    image = self.__loadimage,
                                    bg = '#111111',
                                    borderwidth=0,
                                    highlightthickness=0)
        self.__label.grid(column = 1, row = 1)
        self.__button.grid(column = 1, row = 2)

    
    @typechecked
    def button_handler(self) -> None: 
        self.__active = 0
        self.__label.grid_forget()
        self.__button.grid_forget()
        self.__active = 0

    @typechecked
    def is_active(self) -> bool : 
        return self.__active == 1
        






from typeguard import typechecked
import tkinter as tk

@typechecked
class Home(tk.Frame) : 
    @typechecked
    def __init__(self, master: tk.Tk) -> None: 
        tk.Frame.__init__(self, master)
        self.configure(background='#111111')
        self.__loadimage = tk.PhotoImage(file = "proto-app/view/img/button.png" )
        self.__label = tk.Label(self, text= "Welcome !", bg= '#111111', fg='#7A7A7A', font=("Helvetica", 35))
        self.__button = tk.Button(self,
                                    image = self.__loadimage,
                                    bg = '#111111',
                                    borderwidth=0,
                                    highlightthickness=0,
                                    activebackground= '#111111')
        self.__label.pack(expand=True)
        self.__button.pack(expand=True)

    @typechecked
    def get_button(self)-> tk.Button :
        return self.__button 






import tkinter as tk
from typeguard import typechecked

class Settings(tk.Frame):
    def __init__(self, master: tk.Tk):
        super().__init__(master)
        self.configure(background='#111111')

        self.__frame = tk.Frame(self)
        self.__frame.configure(background="#111111")

        self.__loadimage = tk.PhotoImage(file = "proto-app/view/img/OK.png" )
        
        self.__frame_baudrate = tk.Frame(self)
        self.__frame_baudrate.configure(background="#111111")
        self.__label_baudrate = tk.Label(self.__frame_baudrate, text="BaudRate", bg='#111111', fg='#7A7A7A', font=("Helvetica", 15))
        self.__entry_baudrate = tk.Entry(self.__frame_baudrate, font=("Helvetica",15), justify="center", width="8", bg= "#7A7A7A", borderwidth=0, fg= "#111111")

        self.__frame_COM = tk.Frame(self)
        self.__frame_COM.configure(background="#111111")
        self.__label_COM = tk.Label(self.__frame_COM, text="COM", bg='#111111', fg='#7A7A7A', font=("Helvetica", 15))
        self.__entry_COM = tk.Entry(self.__frame_COM, font=("Helvetica",15), justify="center", width="8", bg= "#7A7A7A", borderwidth=0, fg= "#111111")

        self.__button_submit = tk.Button(self.__frame,
                                    image = self.__loadimage,
                                    bg = '#111111',
                                    borderwidth=0,
                                    highlightthickness=0,
                                    activebackground= '#111111')
        self.__label_baudrate.pack()
        self.__entry_baudrate.pack()

        self.__label_COM.pack()
        self.__entry_COM.pack()

        self.__button_submit.pack()
        self.__frame_baudrate.pack(expand=True)
        self.__frame_COM.pack(expand=True)

        self.__frame.pack(padx=10, pady=10)

    @typechecked
    def get_submit_button(self) -> tk.Button : 
        return self.__button_submit

    @typechecked
    def get_com(self) -> str:
        com = self.__entry_COM.get()
        self.__entry_COM.delete(0, tk.END)
        return com

    @typechecked
    def get_baudrate(self) -> int:
        baudrate=  self.__entry_baudrate.get()
        self.__entry_baudrate.delete(0, tk.END)
        return int(baudrate)

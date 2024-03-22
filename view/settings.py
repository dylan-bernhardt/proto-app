import tkinter as tk
from tkinter import ttk
from typeguard import typechecked

class Settings(tk.Frame):
    def __init__(self, master: tk.Tk):
        super().__init__(master)
        self.configure(background='#111111')
        
        self.__frame = tk.Frame(self)
        self.__frame.config(background='#111111')
        
        self.__frame_baudrate = tk.Frame(self)
        self.__frame_baudrate.config(background='#111111')
        
        self.__label = tk.Label(self.__frame, text="Settings", bg='#111111', fg='#343434', font=("Helvetica", 15))
        self.__label_baudrate = tk.Label(self.__frame_baudrate, text="BaudRate", bg='#111111', fg='#343434', font=("Helvetica", 15))
        self.__entry_baudrate = ttk.Entry(self.__frame_baudrate, font=("Helvetica",15))
        self.__button_submit_baudrate = ttk.Button(self.__frame_baudrate, text="OK", command=self.get_baud_rate)
        
        self.__label.pack()
        self.__label_baudrate.pack()
        self.__entry_baudrate.pack()
        self.__button_submit_baudrate.pack()

        self.__frame.pack(expand=True)
        self.__frame_baudrate.pack(expand=True)
        
    @typechecked
    def get_baud_rate(self) -> None:
        baud_rate = self.__entry_baudrate.get()
        print("Baud rate selected :", baud_rate)
        self.__entry_baudrate.delete(0, tk.END) 


    @typechecked
    def get_value(self) -> tk.Label : 
        return self.__value
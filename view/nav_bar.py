from typeguard import typechecked
import tkinter as tk

@typechecked
class Nav_bar(tk.Frame) : 
    @typechecked
    def __init__(self, master: tk.Tk) -> None: 
        tk.Frame.__init__(self, master)
        self.configure(background='#111111')
        self.__concentration_image = tk.PhotoImage(file = "proto-app/view/img/concentration.png" )
        self.__concentration_button = tk.Button(self,
                                    image = self.__concentration_image,
                                    bg = '#111111',
                                    borderwidth=0,
                                    highlightthickness=0,
                                    activebackground= '#111111')
        self.__level_image = tk.PhotoImage(file = "proto-app/view/img/lvl.png" )
        self.__level_button = tk.Button(self,
                                    image = self.__level_image,
                                    bg = '#111111',
                                    borderwidth=0,
                                    highlightthickness=0,
                                    activebackground= '#111111')
        self.__settings_image = tk.PhotoImage(file = "proto-app/view/img/settings.png" )
        self.__settings_button = tk.Button(self,
                                    image = self.__settings_image,
                                    bg = '#111111',
                                    borderwidth=0,
                                    highlightthickness=0,
                                    activebackground= '#111111')
        self.__level_button.pack(side='right', expand=True)
        self.__settings_button.pack(side='right', expand=True)
        self.__concentration_button.pack(side='left', expand=True)

    @typechecked
    def get_concentration_button(self) -> tk.Button : 
        return self.__concentration_button

    @typechecked
    def get_level_button(self) -> tk.Button : 
        return self.__level_button

    @typechecked
    def get_settings_button(self) -> tk.Button : 
        return self.__settings_button
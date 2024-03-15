from welcome import Home
import tkinter as tk

root = tk.Tk()
root.configure(background='#111111')
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.geometry('900x600')
root.resizable(height = None, width = None)
home = Home(root, "Welcome to our app !")
root.mainloop()

import pygame
import os
pygame.init()
running = True
import tkinter as tk

import pygame
import tkinter as tk

window = tk.Tk()
window.geometry("300x200")
window.title("Song player")
pygame.mixer.init()




#button

tk.Label(window, text="", bg="lightpink").pack(fill="both", expand=True)
button_row = tk.Frame(window)
button_row.pack(pady=10)
tk.Button(button_row, text="OK").pack(side="left", padx=5)
tk.Button(button_row, text="Cancel").pack(side="left", padx=5)



window.mainloop()
















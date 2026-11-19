import pygame
pygame.init()
running = True
import tkinter as tk

window = tk.Tk()
window.title("Sign Up")
window.configure(bg="#e8eef7")
window.geometry("320x260")

# --- pack() is used for the window's own widgets ---
title = tk.Label(
    window, text="MUSIC PLAYER",
    font=("Arial", 18, "bold"), fg="#1a365d", bg="#e8eef7",
)
title.pack(pady=(15, 5))

card = tk.Frame(window, bg="white", relief="groove", bd=2)
card.pack(padx=20, pady=10, fill="x")


play = tk.Button(
    window, text="PLAY",
    font=("Arial", 12, "bold"),
    bg="#2b6cb0", fg="white",
    activebackground="#1a4a80", activeforeground="white",
    cursor="hand2", padx=20, pady=4,
)
play.pack(pady=10)

window.mainloop()








pygame.quit()


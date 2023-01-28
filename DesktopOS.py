import os
import time as tm
import tkinter as tk

os.system('cls')
tm.sleep(0.2)
print("Initializing..")

window = tk.Tk()

window.attributes('-fullscreen', True)
window.title("MazOS Desktop v0.1.2")

label = tk.Label(window, text="Maz OS Desktop Version")
label.pack()

window.mainloop()
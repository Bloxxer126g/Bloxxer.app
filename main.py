from tkinter import *
import pyautogui

# Root config
root = Tk()
root.title("bloxxer.app")
win_w, win_h = 500, 500
screen_w, screen_h = pyautogui.size()
x = int((screen_w - win_w) / 2)
y = int((screen_h - win_h) / 2)
root.geometry(f"{win_w}x{win_h}+{x}+{y}")

# Items
title = Label(root, text="Bloxxer.app")
subtext = Label(root, text="Nothing's here yet!")
copy = Text(root, height=1, borderwidth=0)
copy.insert(1.0, "winget update bloxxer126g.bloxxapp")
copy.configure(state="disabled")

# Placement
title.pack()
subtext.pack()
copy.pack()

root.mainloop()
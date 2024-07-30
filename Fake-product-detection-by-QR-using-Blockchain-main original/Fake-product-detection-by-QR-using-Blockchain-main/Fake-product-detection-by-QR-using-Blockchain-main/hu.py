
from tkinter import *
from tkinter import colorchooser

def pick_color():
    color = colorchooser.askcolor(title ="Choose color")
    color_me.config(bg=color[1])
    color_me.config(text=color)


ws = Tk()
ws.title('PythonGuides')
ws.geometry('400x300')

color_me = Label(
    ws,
    text='(217, 217, 217) #d9d9d9',
    font = ('Times', 20),
    relief = SOLID,
    padx=20,
    pady=20
)
color_me.pack(expand=True)
button = Button(
    ws,
    text = "Choose Color",
    command = pick_color,
    padx=10,
    pady=10,
    font=('Times', 18),
    bg='#4a7a8c'
)
button.pack()

ws.mainloop()

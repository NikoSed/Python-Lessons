import tkinter
import random


window = tkinter.Tk()
window.title("Диско")
window.geometry("600x500")


label = tkinter.Label(text="ДИСКОТЕКА", fg="yellow", font="Arial 22")
label.place(x=230, y=125)

def random_color():
    colors = ["red", "green", "blue"]
    label["fg"] = random.choice(colors)


button = tkinter.Button(text="Нажать чтобы сменить цвет", command= random_color)
button.place(x=230, y=200)


label["fg"] = "red"





window.mainloop()
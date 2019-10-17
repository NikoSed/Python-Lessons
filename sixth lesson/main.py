import tkinter
import random


window = tkinter.Tk()
window.title("Диско")
window.geometry("600x500")


label = tkinter.Label(text="0", fg="yellow", font="Arial 22")
label.place(x=40, y=0)

def random_color():
    colors = ["red", "green", "blue"]
    label["fg"] = random.choice(colors)

def count():
    random_color()
    num = int(label["text"])
    num = num + 1
    label["text"] = str(num)

button = tkinter.Button(text="счёт", command= count)
button.place(x=40, y=40)



label["fg"] = "red"





window.mainloop()
#комментарий
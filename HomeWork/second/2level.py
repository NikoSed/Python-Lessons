import tkinter
import random


window = tkinter.Tk()
window.title("Диско")
window.geometry("600x500")


def random_place():
    listeg=(random.randint(50, 425))
    button.place(x= listeg, y= listeg)


button = tkinter.Button(text="Не нажимай на меня, иначе я убегу", command= random_place)
button.place(x=230, y=200)


window.mainloop()
#Если, что .randit я посмотрел в Google на официальном сайте Python.
#list я узнал с доп. уроков на ютуб (ещё когда только пытался сам изучать python)
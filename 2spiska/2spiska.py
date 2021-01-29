from tkinter import *
from random import *
x_of_circle = 0
sizes = [23,10,5,12,6,8,3]
colors = ['red', 'yellow', 'blue', 'grey70', 'purple', 'green', 'orange']
okno = Tk()
okno.title("Окно №1")
holst = Canvas(okno, width=300, height=300, bg='white')
holst.pack()
for index in range(0,7):
    holst.create_oval(x_of_circle,100,   x_of_circle+sizes[index],100+sizes[index],   fill=colors[index])
    x_of_circle = x_of_circle + 20


from tkinter import *
import random
import time


def activate_or_deactivate():
    if button['text'] == 'on':
        button['text'] = 'off'
        while button['text'] == 'off':
            colors_copy = colors.copy()
            for ball in balls:
                current_color = random.choice(colors_copy)
                wind_size.itemconfig(ball, fill=current_color)
                colors_copy.remove(current_color)
            wind_size.update()
            time.sleep(1)
    else:
        button['text'] = 'on'
        for ball in balls:
            wind_size.itemconfig(ball, fill='black')


window = Tk()
window.title('Гирлянда')
wind_size = Canvas(window, width=700, height=500, bg='grey')
wind_size.pack()
wind_size.create_line(0, 40, 700, 40)

x = 100
colors = ['red', 'green', 'blue', 'yellow', 'pink', 'orange']
balls = []

for i in range(6):
    wind_size.create_line(x, 40, x, 100)
    ball = wind_size.create_oval(x - 50, 100, x + 50, 200, fill='black')
    balls.append(ball)
    x += 100
button = Button(wind_size, text='on', command=activate_or_deactivate)
button.place(x=300, y=400, height=60, width=60)

window.mainloop()

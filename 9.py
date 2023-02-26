from tkinter import *
import random as r

def rand_figure():
    figure = r.randint(0, 2)

    if figure == 1:
        figure_args = [r.randint(1, 500) for i in range(4)]
        fill_arg = f"#{r.randint(0, 0xFFFFFF):06x}"
        canvas.create_rectangle(figure_args[0], figure_args[1], figure_args[2], figure_args[3], fill = fill_arg)
    elif figure == 2:
        figure_args = [r.randint(1, 500) for i in range(4)]
        fill_arg = f"#{r.randint(0, 0xFFFFFF):06x}"
        canvas.create_oval(figure_args[0], figure_args[1], figure_args[2], figure_args[3], fill = fill_arg)
    else:
        figure_args = [r.randint(1, 500) for i in range(6)]
        fill_arg = f"#{r.randint(0, 0xFFFFFF):06x}"
        canvas.create_polygon(figure_args[0], figure_args[1], figure_args[2], figure_args[3], figure_args[4], figure_args[5],fill = fill_arg)

def clear_canvas():
    canvas.delete("all")

root=Tk()
canvas=Canvas(root, width=500, height=500, bg='white')
canvas.pack()

Button(root, text='Новая фигура', width=15, height=2, bg='white', command=rand_figure).pack()
Button(root, text='Очистить всё', width=15, height=2, bg='red', command=clear_canvas).pack()

root.mainloop()
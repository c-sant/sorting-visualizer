from tkinter import Canvas, Tk
from time import sleep

def render_array(window: Tk, canva: Canvas, array: list, array_colors: list, speed: float):
    canva.delete("all")
    canva_height = int(canva.cget('height'))
    canva_width = int(canva.cget('width'))
    
    unit_height = canva_height / max(array)
    unit_width = canva_width / len(array)

    for i, value in enumerate(array):

        # x0 = leftmost point; x1 = rightmost point

        x0 = unit_width * i
        x1 = unit_width * (i + 1)

        # y0 = bottom; y1 = top

        y0 = canva_height,
        y1 = canva_height - (unit_height * value)

        canva.create_rectangle(x0, y0, x1, y1, fill=array_colors[i])

    window.update_idletasks()
    sleep(speed)
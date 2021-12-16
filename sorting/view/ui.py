from tkinter import *
from tkinter import ttk, messagebox
from .visual_algorithms import bubble_sort, insertion_sort, merge_sort, quick_sort, selection_sort
from .render import render_array
import random
import ctypes

try:
    ctypes.windll.shcore.SetProcessDpiAwareness(2)
except:
    ctypes.windll.user32.SetProcessDPIAware()
##########
# Colors #
##########

WHITE = "#FFFFFF"
BLACK = "#000000"
LIGHT_GRAY = "#c1c1c1"
DARK_GRAY = "#1d1d1d"
MATERIAL_BLACK = "#121212"
BLACK = "#000000"
RED = '#d80000'
GREEN = '#12d800'

###############################
# Algorithms and Speed Levels #
###############################

algorithms = {
    'Bubble Sort': bubble_sort,
    'Insertion Sort': insertion_sort,
    'Selection Sort': selection_sort,
    'Merge Sort': merge_sort,
    'Quick Sort': quick_sort
}

speed_levels = {
    'Low': 0.1,
    'Medium': 0.05,
    'High': 0.015
}

##############
# Visualizer #
##############

def start_visualizer():
    window = Tk()
    window.title("Sorting Algorithms Visualizer")
    window.config(bg=MATERIAL_BLACK)
    window.geometry("820x520")
    window.resizable(width=0, height=0)

    global array
    array = []

    # top menu

    fr_top_menu = Frame(master=window, width=900, height=300, bg=MATERIAL_BLACK)
    fr_top_menu.grid(row=0, column=0, padx=10, pady=5)

    # sample size

    lbl_sample_size = Label(
        master = fr_top_menu, 
        text = "Sample size:", 
        bg = MATERIAL_BLACK, 
        fg = LIGHT_GRAY,
    )
    lbl_sample_size.grid(row=0, column=0, padx=10, pady=5)

    sample_size = StringVar()
    cb_sample_size = ttk.Combobox(
        master = fr_top_menu, 
        state = "readonly",
        values = [*range(25, 251, 25)],
        width = 12,
        textvariable = sample_size
    )
    cb_sample_size.grid(row=1, column=0, padx=5, pady=5)
    cb_sample_size.current(0)

    # algorithm selection dropdown

    lbl_algorithm = Label(
        master = fr_top_menu, 
        text = "Algorithm:", 
        bg = MATERIAL_BLACK, 
        fg = LIGHT_GRAY
    )
    lbl_algorithm.grid(row=0, column=1, padx=10, pady=5)

    selected_algorithm = StringVar()
    cb_algo_selector = ttk.Combobox(
        master = fr_top_menu, 
        state = "readonly", 
        textvariable = selected_algorithm, 
        values = [*algorithms.keys()],
        width = 12
    )
    cb_algo_selector.grid(row=1, column=1, padx=5, pady=5)
    cb_algo_selector.current(0)

    # Speed

    lbl_speed = Label(
        master = fr_top_menu,
        text = "Speed:",
        bg = MATERIAL_BLACK,
        fg = LIGHT_GRAY
    )
    lbl_speed.grid(row=0, column=2, padx=10, pady=5)

    selected_speed = StringVar()
    cb_speed_selector = ttk.Combobox(
        master = fr_top_menu,
        state = "readonly",
        textvariable = selected_speed,
        values = [*speed_levels.keys()],
        width = 12
    )
    cb_speed_selector.grid(row=1, column=2, padx=5, pady=5)
    cb_speed_selector.current(2)

    # generate sample button

    def render_sample():
        max_size = int(sample_size.get())
        
        global array

        array = random.sample(range(1, (max_size + 1)), max_size)

        array_colors = [WHITE for i in array]

        render_array(window, canva, array, array_colors, 0)

    btn_generate_sample = Button(
        master = fr_top_menu, 
        text = "Generate Sample", 
        bg = DARK_GRAY, 
        fg = LIGHT_GRAY,
        command = render_sample
    )
    btn_generate_sample.grid(row=0, column=3, padx=5, pady=5)

    # run button
    def sort_sample():
        global array

        if len(array) == 0:
            messagebox.showerror(
                title = "Empty Array",
                message = "Array must be generated before sorting."
            )
            return
        
        method = selected_algorithm.get()
        speed = speed_levels[selected_speed.get()]

        if method not in [*algorithms.keys()]:
            messagebox.showerror(
                title = "Sorting Method Not Selected",
                message = "A sorting method must be chosen before sorting."
            )
            return

        algorithms[method](window, canva, array, speed)
        max_size = int(sample_size.get())
        final_speed = (0.625 / max_size)
        for i in range(len(array)):
            colors = [WHITE if j > i else (GREEN if j < i else RED) for j in range(len(array))]
            render_array(window, canva, array, colors, final_speed)

    btn_run = Button(
        master = fr_top_menu, 
        text = "Run", 
        bg = DARK_GRAY, 
        fg = LIGHT_GRAY, 
        width = 10,
        command = sort_sample
    )
    btn_run.grid(row=1, column=3, padx=10, pady=5)

    # graphical array space
    canva = Canvas(
        master = window, 
        width = 800, 
        height = 400,
        bg = BLACK,
        highlightthickness = 0
    )
    canva.grid(row=1, column=0, padx=10, pady=5)

    window.mainloop()

if __name__ == '__main__':
    start_visualizer()
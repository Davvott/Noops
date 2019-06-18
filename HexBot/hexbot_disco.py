from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import StringVar, IntVar
import random
from HexBot.hexbot import get_hexbot_colours


class Toolbar(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.toolbar_frame = ttk.LabelFrame(self.parent, text='HexBot Disco', padding=(5, 5, 5, 5), height=40)
        self.toolbar_frame.pack(side='top', fill='x')

        self.toolbar = ttk.Label(
            self.toolbar_frame, textvariable=self.parent.game_type_text, padding=(2, 2, 2, 2),
            justify='center')
        self.toolbar.pack(side='top', fill='y', anchor="n")


class GridBox(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        # Init Grid variables
        self.rows = 40
        self.cols = 40
        self.cellwidth = 20
        self.cellheight = 20

        # Creating Canvas larger than grid
        self.wide = self.cellwidth*self.cols
        self.high = self.cellheight*self.rows

        self.canvas_frame = ttk.Frame(self.parent, padding=(2, 2, 2, 2))
        self.canvas_frame.pack(side='top', fill='both')
        self.canvas = tk.Canvas(
            self.canvas_frame, width=self.wide, height=self.high, borderwidth=0, highlightthickness=0)
        self.canvas.pack(side="top", fill="both", expand="true")

        # Initialize Grid
        self.grid = {}
        for column in range(self.cols):
            for row in range(self.rows):
                x1 = column * self.cellwidth
                y1 = row * self.cellheight
                x2 = x1 + self.cellwidth
                y2 = y1 + self.cellheight
                # Each grid item will return an item_id
                self.grid[row, column] = self.canvas.create_rectangle(
                    x1, y1, x2, y2, fill="white", tags=("rect", 'white'))


class OptionsBox(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        # Labels, Buttons, Entry's

        self.options_frame = ttk.LabelFrame(self.parent, text='Options', width=100, padding=(5, 5, 5, 5))
        self.options_frame.pack(side='right', fill='y', expand=True)

        # Events, Btn Clicks, Mouse Clicks
        self.items_frame = ttk.LabelFrame(self.options_frame, text='Active Items', width=80, padding=(2, 2, 2, 2))
        self.items_frame.pack(side='top', fill='x', expand=True)
        self.item_set = ttk.Entry(self.items_frame, textvariable=self.parent.active_items, width=20)
        self.item_set.pack(side='top', fill='x')
        # self.set_button = ttk.Button(self.items_frame, text='Reset Items', command=self.parent.reset)
        # self.set_button.pack(side='top', fill='x')


class Main(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.colors = get_hexbot_colours(1000)


class MainApp(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        # initialize variables
        self.game_type_text = StringVar()
        self.game_type_text.set('HexBot Disco')

        self.active_items = StringVar()
        self.active_items.set('20')
        # self.active_items = 20

        # Instantiate Frames
        self.toolbar = Toolbar(self)  # instantiates class in order
        self.options_box = OptionsBox(self)
        self.gridbox = GridBox(self)
        self.main = Main(self)

        self.toolbar.pack(side="top", fill="x", padx=5, pady=5)
        self.gridbox.pack(side='top', fill='both', expand=True, padx=5, pady=5)
        self.options_box.pack(side="right", fill="y")
        self.main.pack(side="right", fill="both", expand=True)

        # Select random hex values from HexBot
        self.hex_values = [d['value'] for d in self.main.colors['colors']]

        self.redraw(500)  # auto delayed loop for canvas draw

    def redraw(self, delay):
        # itemconfig(tags='rect', fill='White')  # all items in rect{} tags='rect' as above
        # reset all tags='rect'
        self.gridbox.canvas.itemconfig(
            "rect", fill="white", tags=('rect', 'white'))

        try:
            items = int(self.active_items.get())  # Bound to Text Entry
        except ValueError:
            items = 1

        hex_sample = random.sample(self.hex_values, items)

        # Random Fill --- for x no. of items
        for i in range(items):
            row = random.randint(0, self.gridbox.rows - 1)
            col = random.randint(0, self.gridbox.cols - 1)

            item_id = self.gridbox.grid[row, col]

            # Change fill for item_id
            self.gridbox.canvas.itemconfig(
                item_id, fill=hex_sample[i], tags=('rect', 'black'))

        # black_tiles = self.gridbox.canvas.find_withtag('black')

        self.after(delay, lambda: self.redraw(delay))


if __name__ == "__main__":
    root = Tk()
    root.title('HexBot Disco')
    MainApp(root).pack(side="top", fill="both", expand=True, padx=5, pady=5)

    root.mainloop()

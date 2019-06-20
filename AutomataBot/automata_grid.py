from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import StringVar
import random
from AutomataBot.game_of_life import GameOfLife

MAX_WIN_WIDTH = 1200
MAX_WIN_HEIGHT = 900

class Toolbar(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.toolbar_frame = ttk.LabelFrame(self.parent, text='AutomataBot', padding=(5, 5, 5, 5), height=40)
        self.toolbar_frame.pack(side='top', fill='x')

        self.toolbar = ttk.Label(
            self.toolbar_frame, textvariable=self.parent._game_type_text, padding=(2, 2, 2, 2),
            justify='center')
        self.toolbar.pack(side='top', fill='y', anchor="n")


class GridBox(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        # Init Grid variables
        _c = self.parent.cols
        _r = self.parent.rows

        self.cellheight = MAX_WIN_HEIGHT / _r
        self.cellwidth = self.cellheight

        # Creating Canvas larger than grid
        self.wide = self.cellwidth*_c
        self.high = self.cellheight*_r

        self.canvas_frame = ttk.Frame(self.parent, padding=(2, 2, 2, 2))
        self.canvas_frame.pack(side='top', fill='both')
        self.canvas = tk.Canvas(
            self.canvas_frame, width=self.wide, height=self.high, borderwidth=0, highlightthickness=0)
        self.canvas.pack(side="top", fill="both", expand="true")

        # Initialize Grid
        self.grid = {}
        for column in range(_c):
            for row in range(_r):
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

        self.items_frame = ttk.LabelFrame(self.options_frame, text='Active Items', width=80, padding=(2, 2, 2, 2))
        self.items_frame.pack(side='top', fill='x', expand=True)

        self.change_btn = ttk.Button(
            self.options_frame, text='Switch', command=self.parent.change_state)
        self.change_btn.pack(side='top', fill='x')

class Main(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)


class MainApp(tk.Frame):
    def __init__(self, parent, cells, cols=40, rows=40, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        # initialize variables
        self._game_type = StringVar()
        self._game_type.set('GameOfLife')
        self._game_type_text = StringVar()
        self._game_type_text.set(self._game_type.get())  # update to type of Automata loaded
        self._delay = IntVar()
        self._delay = 700

        self.cols = IntVar()
        self.rows = IntVar()
        self.cols = cols
        self.rows = rows
        self.cells = cells



        # Instantiate Frames
        self.toolbar = Toolbar(self)  # instantiates class in order
        self.options_box = OptionsBox(self)
        self.gridbox = GridBox(self)
        self.main = Main(self)

        self.toolbar.pack(side="top", fill="x", padx=5, pady=5)
        self.gridbox.pack(side='top', fill='both', expand=True, padx=5, pady=5)
        self.options_box.pack(side="right", fill="y")
        self.main.pack(side="right", fill="both", expand=True)

        self.run()

    def run(self):
        self.change_state()
        self.wipe_grid()
        self.redraw(self._delay)

    def redraw(self, delay):
        # itemconfig(tags='rect', fill='White')  # all items in rect{} tags='rect' as above
        # type(black_tiles) = <class 'tuple'> of item_ids
        # grid = dict{(x, y): item_id,}

        black_tiles = self.gridbox.canvas.find_withtag('black')
        tiles_to_change = self.automata.next_state(black_tiles)

        for tile in tiles_to_change:
            # item_id = self.gridbox.grid[tile]
            if tile not in black_tiles:
                self.gridbox.canvas.itemconfig(
                    tile, fill="black", tags=('rect', 'black'))
            else:
                self.gridbox.canvas.itemconfig(
                    tile, fill="white", tags=('rect', 'white'))

        self.after(delay, lambda: self.redraw(delay))

    def change_state(self):
        """Basic Switch, updates automata Class, wipes grid, continues redrawing"""
        cls_type = self._game_type.get()

        if cls_type == 'GameOfLife':
            self.automata = GameOfLife(self.gridbox.grid, self.cells)

        self._game_type_text.set(cls_type)
        self.wipe_grid()


    def wipe_grid(self):
        # WIPE GRID --- reset all tags='rect'
        self.gridbox.canvas.itemconfig(
            "rect", fill="white", tags=('rect', 'white'))


if __name__ == "__main__":
    root = Tk()
    root.title('AutomataBot')
    MainApp(root).pack(side="top", fill="both", expand=True, padx=5, pady=5)

    root.mainloop()

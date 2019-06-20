"""Automata Bot Feeding Ground"""
from tkinter import *
import pprint
from AutomataBot.automata_bot import AutomataBot
from AutomataBot.automata_grid import MainApp

def main():
    automata = AutomataBot()
    print(automata)

    rows = automata.rows
    cols = automata.cols

    root = Tk()
    root.title('AutomataBot')
    MainApp(root, cells=automata.cells, cols=cols, rows=rows).pack(side="top", fill="both", expand=True, padx=5, pady=5)

    root.mainloop()

# generate grid self.height, self.width

# Populate grid according to cells
# for each list in cells, and for each cell in list:
# iterate through grid and color black if == 1


main()

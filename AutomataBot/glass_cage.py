"""Automata Bot Feeding Ground"""
from tkinter import *
from AutomataBot.automata_bot import AutomataBot
from AutomataBot.automata_grid import MainApp


def main():
    automatabot = AutomataBot()
    print(automatabot)

    root = Tk()
    root.title('AutomataBot')
    MainApp(root, bot=automatabot).pack(side="top", fill="both", expand=True, padx=5, pady=5)
    root.mainloop()

# generate grid self.height, self.width

# Populate grid according to cells
# for each list in cells, and for each cell in list:
# iterate through grid and color black if == 1


main()

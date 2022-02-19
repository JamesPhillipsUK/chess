"""chess.py

A game of chess.

Authors: Jesse Phillips <james@jamesphillipsuk.com>
"""
import PySimpleGUI as psg
from board import *


class Chess:

    def __init__(self):
        """Constructor for Chess.  Creates an instance of the game.
        """
        pass

    def main(self):
        """Entrypoint for the script.  Runs the game.
        """
        board = Board()
        board.loadAssets()
        board.setInitialLayout()
        board.buildBoard(psg.Window(title="Chess",
                                    layout=board.getLayout(),
                                    margins=(0, 0),
                                    element_padding=0))
        board.launchGameLoop()
        psg.Print("ran successfully!")


if __name__ == "__main__":
    chess = Chess()
    chess.main()

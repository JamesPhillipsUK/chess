import PySimpleGUI as psg
from board import *


class Chess:
    def __init__(self):
        pass

    def main(self):
        board = Board()
        board.loadAssets()
        board.setInitialLayout()
        board.buildBoard(psg.Window(title="Chess",
                                    layout=board.getLayout(),
                                    margins=(0, 0)))
        board.launchGameLoop()
        print("ran successfully!")

if __name__ == "__main__":
    chess = Chess()
    chess.main()

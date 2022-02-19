import PySimpleGUI as psg
from board import *
from square import *


class Chess:
    def __init__(self):
        pass

    def main(self):
        board = Board()
        board.loadAssets()
        layout = []
        for cnt in range(8, 0, -1):
            layout += [
                       [Square("a" + str(cnt),
                        image_data=board.getSquareColour("a" + str(cnt)))] +
                       [Square("b" + str(cnt),
                        image_data=board.getSquareColour("b" + str(cnt)))] +
                       [Square("c" + str(cnt),
                        image_data=board.getSquareColour("c" + str(cnt)))] +
                       [Square("d" + str(cnt),
                        image_data=board.getSquareColour("d" + str(cnt)))] +
                       [Square("e" + str(cnt),
                        image_data=board.getSquareColour("e" + str(cnt)))] +
                       [Square("f" + str(cnt),
                        image_data=board.getSquareColour("f" + str(cnt)))] +
                       [Square("g" + str(cnt),
                        image_data=board.getSquareColour("g" + str(cnt)))] +
                       [Square("h" + str(cnt),
                        image_data=board.getSquareColour("h" + str(cnt)))]]
        board.buildBoard(psg.Window(title="Chess",
                                    layout=layout,
                                    margins=(0, 0)))
        board.launchGameLoop()
        print("ran successfully!")

if __name__ == "__main__":
    chess = Chess()
    chess.main()

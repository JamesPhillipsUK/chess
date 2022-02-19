import PySimpleGUI as psg
from board import *
from square import *


class Chess:
    def main():
        board = Board()
        layout = []
        for cnt in range(8, 0, -1):
            layout += [
                       [Square("a" + str(cnt))] +
                       [Square("b" + str(cnt))] +
                       [Square("c" + str(cnt))] +
                       [Square("d" + str(cnt))] +
                       [Square("e" + str(cnt))] +
                       [Square("f" + str(cnt))] +
                       [Square("g" + str(cnt))] +
                       [Square("h" + str(cnt))]]
        board.buildBoard(psg.Window(title="Chess",
                                    layout=layout,
                                    margins=(296, 296)))
        board.launchGameLoop()
        print("ran successfully!")

    if __name__ == "__main__":
        main()

import PySimpleGUI as psg
from square import *
import base64


class Board:
    window = psg.Window(title="Chess")
    whiteSquare = b''
    blackSquare = b''
    layout = [[], [], [], [], [], [], [], []]

    def setInitialLayout(self):
        for cnt in range(8, 0, -1):
            for col in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
                self.layout[cnt-1] += [Square(key=col + str(cnt),
                                              image_data=self.getSquareColour(
                                                  col + str(cnt)))]

    def getLayout(self):
        return self.layout

    def getSquareColour(self, squareName: str):
        squareNameSpec = [char for char in squareName]
        if squareNameSpec[0] in ['a', 'c', 'e', 'g']:
            if int(squareNameSpec[1]) % 2 == 0:
                return self.whiteSquare
        else:
            if int(squareNameSpec[1]) % 2 != 0:
                return self.whiteSquare
        return self.blackSquare

    def convertImageToB64(self, filename: str):
        with open(filename, 'rb') as imageFile:
            image = imageFile.read()
            return base64.b64encode(image)

    def loadAssets(self):
        self.whiteSquare = self.convertImageToB64("img/w_square.png")
        self.blackSquare = self.convertImageToB64("img/b_square.png")

    def buildBoard(self, win):
        self.window = win
        return True

    def killBoard(self):
        self.window.close()
        return True

    def launchGameLoop(self):
        while True:
            event, values = self.window.read()
            if event == psg.WIN_CLOSED:
                break
        self.killBoard()

import PySimpleGUI as psg
import base64


class Board:
    window = psg.Window(title="Chess")
    whiteSquare = b''
    blackSquare = b''

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

"""board.py

The board for a game of chess.

Authors: Jesse Phillips <james@jamesphillipsuk.com>
"""
import PySimpleGUI as psg
from square import *
from piece import *
import base64


class Board:

    window = psg.Window(title="Chess")
    whiteSquare = b''
    blackSquare = b''
    layout = [[], [], [], [], [], [], [], []]

    def setInitialLayout(self):
        """Sets the initial (blank) layout of the board.
        """
        for cnt in range(8, 0, -1):
            for col in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
                self.layout[cnt-1] += [Square(key=col + str(cnt),
                                              image_data=self.getSquareColour(
                                                  col + str(cnt)))]
        self.layout.reverse()

    def getLayout(self):
        """ Gets the current board layout

        Returns:
            List: The board layout
        """
        return self.layout

    def getSquareColour(self, squareName: str):
        """ Gets the colour of a given square on the board.

        Args:
            squareName (string): the name of the square.  IE: "a1", "c8", etc.

        Returns:
            Bytes: The coloured square as a b64 encoded PNG.
        """
        squareNameSpec = [char for char in squareName]
        if squareNameSpec[0] in ['a', 'c', 'e', 'g']:
            if int(squareNameSpec[1]) % 2 == 0:
                return self.whiteSquare
        else:
            if int(squareNameSpec[1]) % 2 != 0:
                return self.whiteSquare
        return self.blackSquare

    def convertImageToB64(self, filename: str):
        """ Coverts an image to Base64 endoded bytes.

        Args:
            filename (string): the filename of the image.

        Returns:
            Bytes: The encoded image.
        """
        with open(filename, 'rb') as imageFile:
            image = imageFile.read()
            return base64.b64encode(image)

    def loadAssets(self):
        """Loads assets needed for the board.
        """
        self.whiteSquare = self.convertImageToB64("img/w_square.png")
        self.blackSquare = self.convertImageToB64("img/b_square.png")

    def buildBoard(self, win: psg.Window):
        """Builds the board window.

        Args:
            win (psg.Window): the board's PySimpleGUI window.

        Returns:
            Bool: True if successful.
        """
        self.window = win
        return True

    def killBoard(self):
        """Kills the current board window.

        Returns:
            Bool: True if successful.
        """
        self.window.close()
        return True

    def setUpPieces(self):
        self.window["a1"].setCurrentPiece(Piece("rook", "white", "a1"))
        self.window["b1"].setCurrentPiece(Piece("knight", "white", "b1"))
        self.window["c1"].setCurrentPiece(Piece("bishop", "white", "c1"))
        self.window["d1"].setCurrentPiece(Piece("queen", "white", "d1"))
        self.window["e1"].setCurrentPiece(Piece("king", "white", "e1"))
        self.window["f1"].setCurrentPiece(Piece("bishop", "white", "f1"))
        self.window["g1"].setCurrentPiece(Piece("knight", "white", "g1"))
        self.window["h1"].setCurrentPiece(Piece("rook", "white", "h1"))

    def updateBoardView(self):
        squares = [self.window["a1"], self.window["b1"], self.window["c1"],
                   self.window["d1"], self.window["e1"], self.window["f1"],
                   self.window["g1"], self.window["h1"]]
        for item in squares:
            imageLocation = "img/"
            image = item.getCurrentImage()
            if image[5:10] == "white": imageLocation += "w_"
            else: imageLocation += "b_"
            if image[10:] == "bishop": imageLocation += "b_"
            elif image[10:] == "knight": imageLocation += "n_"
            elif image[10:] == "rook": imageLocation += "r_"
            elif image[10:] == "queen": imageLocation += "q_"
            elif image[10:] == "king": imageLocation += "k_"
            elif image[10:] == "pawn": imageLocation += "p_"
            if image[:5] == "white": imageLocation += "w.png"
            else: imageLocation += "b.png"
            item.update(image_data=self.convertImageToB64(imageLocation))

    def launchGameLoop(self):
        """Launches and runs the game loop.
        """
        isInitialising = True
        while True:
            event, values = self.window.read(timeout=100)
            if isInitialising:
                self.setUpPieces()
                self.updateBoardView()
                isInitialising = False
            if event !=psg.WIN_CLOSED:
                if event != psg.TIMEOUT_EVENT:
                    psg.Print(self.window[event].getCurrentImage())
                self.updateBoardView()
            if event == psg.WIN_CLOSED:
                break
        self.killBoard()

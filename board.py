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
    clickCount = 0
    selectedSquare = Square
    layout = [[], [], [], [], [], [], [], []]
    pGN = []

    def setInitialLayout(self):
        """Sets the initial (blank) layout of the board.
        """
        # Build an 8x8 grid of Squares a1 - h8, with chequered square pattern.
        for cnt in range(8, 0, -1):
            for col in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
                self.layout[cnt-1] += [Square(key=col + str(cnt),
                                              image_data=self.getSquareColour(
                                                  col + str(cnt)))]
        self.layout.reverse()  # Flip it - a1 goes at the bottom-left.

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
        """ Sets up the pieces on the board.
        """
        # White back rank:
        self.window["a1"].setCurrentPiece(Piece("rook", "white", "a1"))
        self.window["b1"].setCurrentPiece(Piece("knight", "white", "b1"))
        self.window["c1"].setCurrentPiece(Piece("bishop", "white", "c1"))
        self.window["d1"].setCurrentPiece(Piece("queen", "white", "d1"))
        self.window["e1"].setCurrentPiece(Piece("king", "white", "e1"))
        self.window["f1"].setCurrentPiece(Piece("bishop", "white", "f1"))
        self.window["g1"].setCurrentPiece(Piece("knight", "white", "g1"))
        self.window["h1"].setCurrentPiece(Piece("rook", "white", "h1"))

        # 2nd and 7th rank pawns:
        for col in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
            self.window[col+"2"].setCurrentPiece(Piece(
                                                 "pawn", "white", col+"2"))
            self.window[col+"7"].setCurrentPiece(Piece(
                                                 "pawn", "black", col+"7"))

        # Black back rank:
        self.window["a8"].setCurrentPiece(Piece("rook", "black", "a8"))
        self.window["b8"].setCurrentPiece(Piece("knight", "black", "b8"))
        self.window["c8"].setCurrentPiece(Piece("bishop", "black", "c8"))
        self.window["d8"].setCurrentPiece(Piece("queen", "black", "d8"))
        self.window["e8"].setCurrentPiece(Piece("king", "black", "e8"))
        self.window["f8"].setCurrentPiece(Piece("bishop", "black", "f8"))
        self.window["g8"].setCurrentPiece(Piece("knight", "black", "g8"))
        self.window["h8"].setCurrentPiece(Piece("rook", "black", "h8"))

    def updateBoardView(self):
        """Updates the view of the board.
        """
        # Generate a list of all squares on the board.
        squares = []
        for file in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
            for rank in range(8, 0, -1):
                squares.append(self.window[file+str(rank)])

        # Find the right image asset for each square.
        for item in squares:
            imageLocation = "img/"
            image = item.getCurrentImage()
            if image[5:10] == "white":
                imageLocation += "w_"
            else:
                imageLocation += "b_"
            if image[10:] == "knight":
                imageLocation += "n_"
            elif len(image) >= 10:
                imageLocation += image[10] + "_"
            if image[:5] == "white":
                imageLocation += "w.png"
            else:
                imageLocation += "b.png"
            if len(imageLocation) < 12:
                if image[:5] == "black":
                    imageLocation = "img/b_square.png"
                else:
                    imageLocation = "img/w_square.png"
            item.update(image_data=self.convertImageToB64(imageLocation))

    def isTurn(self, square: Square):
        """ Checks if it is a players turn when they select a piece.

        Args:
            square (Square): the square the player has clicked on.

        Returns:
            Boolean: True if it is that player's turn.
        """
        if self.clickCount % 4 == 0:  # White's turn
            if square.getCurrentPiece().pieceColour == "black":
                return False  # White selected a black piece.
        elif square.getCurrentPiece().pieceColour == "white":
            return False  # Black selected a white piece.
        return True

    def handleMove(self, square: Square):
        """Handles moving a piece

        Args:
            square (Square): the currently selected square.
        """
        if self.clickCount % 2 == 0:  # Piece selected to be moved.
            if square.getCurrentPiece().pieceType == "":  # Piece must exist.
                return
            if self.isTurn(square) is False:
                return
            self.selectedSquare = square
            square.update(disabled=True)
        else:  # Place to move the piece to.
            if self.isMoveLegal(self.selectedSquare, square) is False:
                self.clickCount -= 1
                self.selectedSquare.update(disabled=False)
                psg.Print(self.clickCount)
                return
            self.selectedSquare.getCurrentPiece().moveTo(square.Key)
            square.setCurrentPiece(self.selectedSquare.getCurrentPiece())
            self.selectedSquare.setCurrentPiece(Piece("", "", ""))
            self.selectedSquare.update(disabled=False)
            psg.Print(self.pGN[len(self.pGN) - 1])
        self.clickCount += 1

    def isPawnMoveLegal(self, currentPosition: Square, targetPosition: Square):
        """Checks if a pawn move is legal.

        Args:
            currentPosition (Square): The current piece position.
            targetPosition (Square): The target piece position.

        Returns:
            Boolean: True if the move is legal.
        """
        colour = currentPosition.getCurrentPiece().pieceColour
        currentKey = currentPosition.Key
        targetKey = targetPosition.Key
        if colour == "white":
            if (int(targetKey[1]) - int(currentKey[1]) == 1 and
               targetKey[0] == currentKey[0] and
               targetPosition.getCurrentPiece().pieceType == ""):
                self.pGN.append(targetKey)
                return True  # Standard white move.
            elif (int(targetKey[1]) - int(currentKey[1]) == 1 and
                  (ord(targetKey[0]) - ord(currentKey[0]) == 1 or
                   ord(targetKey[0]) - ord(currentKey[0]) == -1) and
                  targetPosition.getCurrentPiece().pieceColour == "black"):
                self.pGN.append(currentKey[0] + "x" + targetKey)
                return True  # White takes.
            elif (int(targetKey[1]) - int(currentKey[1]) == 1 and
                  (ord(targetKey[0]) - ord(currentKey[0]) == 1 or
                   ord(targetKey[0]) - ord(currentKey[0]) == -1) and
                  self.window[targetKey[0]+currentKey[1]].getCurrentPiece()
                      .pieceColour == "black" and
                  self.pGN[len(self.pGN) - 1] == targetKey[0] + currentKey[1]):
                for move in self.pGN:
                    if move == targetKey[0] + "6":
                        return False
                self.window[targetKey[0] + currentKey[1]].setCurrentPiece(
                    Piece("", "", ""))
                self.pGN.append(currentKey[0] + "x" + targetKey)
                return True  # White takes en passant.
            elif (int(currentKey[1]) == 2 and
                  int(targetKey[1]) - int(currentKey[1]) == 2 and
                  targetKey[0] == currentKey[0] and
                  targetPosition.getCurrentPiece().pieceType == ""):
                self.pGN.append(targetKey)
                return True   # Initial white move.
        else:
            if (int(currentKey[1]) - int(targetKey[1]) == 1 and
               targetKey[0] == currentKey[0] and
               targetPosition.getCurrentPiece().pieceType == ""):
                self.pGN.append(targetKey)
                return True  # Standard black move.
            elif (int(currentKey[1]) - int(targetKey[1]) == 1 and
                  (ord(targetKey[0]) - ord(currentKey[0]) == 1 or
                   ord(targetKey[0]) - ord(currentKey[0]) == -1) and
                  targetPosition.getCurrentPiece().pieceColour == "white"):
                self.pGN.append(currentKey[0] + "x" + targetKey)
                return True  # Black takes.
            elif (int(currentKey[1]) - int(targetKey[1]) == 1 and
                  (ord(targetKey[0]) - ord(currentKey[0]) == 1 or
                   ord(targetKey[0]) - ord(currentKey[0]) == -1) and
                  self.window[targetKey[0]+currentKey[1]].getCurrentPiece()
                      .pieceColour == "white" and
                  self.pGN[len(self.pGN) - 1] == targetKey[0] + currentKey[1]):
                for move in self.pGN:
                    if move == targetKey[0] + "3":
                        return False
                self.window[targetKey[0] + currentKey[1]].setCurrentPiece(
                    Piece("", "", ""))
                self.pGN.append(currentKey[0] + "x" + targetKey)
                return True  # Black takes en passant.
            elif (int(currentKey[1]) == 7 and
                  int(currentKey[1]) - int(targetKey[1]) == 2 and
                  targetKey[0] == currentKey[0] and
                  targetPosition.getCurrentPiece().pieceType == ""):
                self.pGN.append(targetKey)
                return True  # Initial black move.
        return False

    def isKnightMoveLegal(self, currentPosition: Square,
                          targetPosition: Square):
        """Checks if a Knight move is legal.

        Args:
            currentPosition (Square): The current piece position.
            targetPosition (Square): The target piece position.

        Returns:
            Boolean: True if the move is legal.
        """
        targetKey = targetPosition.Key
        currentKey = currentPosition.Key
        if ((ord(targetKey[0]) - ord(currentKey[0]) == 1 or
             ord(currentKey[0]) - ord(targetKey[0]) == 1) and
            (int(targetKey[1]) - int(currentKey[1]) == 2 or
             int(currentKey[1]) - int(targetKey[1]) == 2)):
            if targetPosition.getCurrentPiece().pieceType == "":
                self.pGN.append("N"+targetKey)
                return True  # Move to empty square.
            elif (targetPosition.getCurrentPiece().pieceColour !=
                  currentPosition.getCurrentPiece().pieceColour):
                self.pGN.append("Nx"+targetKey)
                return True  # Knight takes.

        elif ((ord(targetKey[0]) - ord(currentKey[0]) == 2 or
               ord(currentKey[0]) - ord(targetKey[0]) == 2) and
              (int(targetKey[1]) - int(currentKey[1]) == 1 or
               int(currentKey[1]) - int(targetKey[1]) == 1)):
            if targetPosition.getCurrentPiece().pieceType == "":
                self.pGN.append("N"+targetKey)
                return True  # Move to empty square.
            elif (targetPosition.getCurrentPiece().pieceColour !=
                  currentPosition.getCurrentPiece().pieceColour):
                self.pGN.append("Nx"+targetKey)
                return True  # Knight takes.
        return False

    def isBishopMoveLegal(self, currentPosition: Square,
                          targetPosition: Square):
        """Checks if a Bishop move is legal.

        Args:
            currentPosition (Square): The current piece position.
            targetPosition (Square): The target piece position.

        Returns:
            Boolean: True if the move is legal.
        """
        targetKey = targetPosition.Key
        currentKey = currentPosition.Key
        # Check we're not jumping any pieces between here and our target.
        skipSelf = True  # When moved, don't check if it's jumping over itself.
        rankStep = 1
        fileStep = 1
        if int(currentKey[1]) > int(targetKey[1]):
            fileStep = -1
        if ord(currentKey[0]) > ord(targetKey[0]):
            rankStep = -1
        for file in range(int(currentKey[1]), int(targetKey[1]), fileStep):
            for rank in range(ord(currentKey[0]), ord(targetKey[0]), rankStep):
                if ((rank - ord(currentKey[0]) == int(currentKey[1]) - file) or
                    ((rank - 96) - file ==
                     (ord(currentKey[0]) - 96) - int(currentKey[1]))):
                    if skipSelf:
                        skipSelf = False
                    elif (self.window[chr(rank) + str(file)].getCurrentPiece()
                          .pieceColour != ""):
                        return False
        # If the attempted move is legal, make it.
        if ((ord(targetKey[0]) - ord(currentKey[0]) ==
                int(currentKey[1]) - int(targetKey[1])) or
           ((ord(targetKey[0]) - 96) - (int(targetKey[1])) ==
                (ord(currentKey[0]) - 96) - (int(currentKey[1])))):
            if (targetPosition.getCurrentPiece().pieceColour == ""):
                self.pGN.append("B" + targetKey)
                return True  # standard move
            elif (targetPosition.getCurrentPiece().pieceColour !=
                  currentPosition.getCurrentPiece().pieceColour):
                self.pGN.append("Bx" + targetKey)
                return True  # Bishop takes
        return False

    def isRookMoveLegal(self, currentPosition: Square, targetPosition: Square):
        """Checks if a Rook move is legal.

        Args:
            currentPosition (Square): The current piece position.
            targetPosition (Square): The target piece position.

        Returns:
            Boolean: True if the move is legal.
        """
        targetKey = targetPosition.Key
        currentKey = currentPosition.Key
        if ((ord(targetKey[0]) != ord(currentKey[0]) and
             int(currentKey[1]) == int(targetKey[1])) or
            (int(targetKey[1]) != int(currentKey[1]) and
             ord(currentKey[0]) == ord(targetKey[0]))):
            if targetPosition.getCurrentPiece().pieceType == "":
                self.pGN.append("R"+targetKey)
                return True  # Move to empty square.
            elif (targetPosition.getCurrentPiece().pieceColour !=
                  currentPosition.getCurrentPiece().pieceColour):
                self.pGN.append("Rx"+targetKey)
                return True  # Rook takes.
        return False

    def isMoveLegal(self, currentPosition: Square, targetPosition: Square):
        """Checks if a move is legal.

        Args:
            currentPosition (Square): The current piece position.
            targetPosition (Square): The target piece position.

        Returns:
            Boolean: True if the move is legal.
        """
        if currentPosition.getCurrentPiece().pieceType == "pawn":
            if self.isPawnMoveLegal(currentPosition, targetPosition):
                return True
        elif currentPosition.getCurrentPiece().pieceType == "knight":
            if self.isKnightMoveLegal(currentPosition, targetPosition):
                return True
        elif currentPosition.getCurrentPiece().pieceType == "bishop":
            if self.isBishopMoveLegal(currentPosition, targetPosition):
                return True
        elif currentPosition.getCurrentPiece().pieceType == "rook":
            if self.isRookMoveLegal(currentPosition, targetPosition):
                return True
        return False

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
            if event != psg.WIN_CLOSED:
                if event != psg.TIMEOUT_EVENT:
                    self.handleMove(self.window[event])
                self.updateBoardView()
            if event == psg.WIN_CLOSED:
                break
        self.killBoard()

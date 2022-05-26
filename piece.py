"""piece.py

A piece on the board for a game of chess.

Authors: Jesse Phillips <james@jamesphillipsuk.com>
"""
import PySimpleGUI as psg


class Piece:

    pieceType = ""
    pieceColour = ""
    pieceSquare = ""
    pieceHasMoved = False

    def __init__(self, pType: str,
                 colour: str,
                 square: str,
                 hasMoved: bool = False):
        """Create an instance of a chess piece.

        Args:
            pType (string): the type of piece.  IE: "king", "pawn", etc.
            colour (string): the colour of the piece.
            square (string): the name of the square the piece is on.
        """
        self.pieceType = pType
        self.pieceColour = colour
        self.pieceSquare = square
        self.pieceHasMoved = hasMoved

    def moveTo(self, square: str):
        """ Move the piece

        Args:
            square (string): the square to move the piece to.
        """
        self.pieceSquare = square

    def pieceCanPromote(self):
        """ Checks if the piece can promote.

        Returns:
            bool: True if the piece can promote.
        """
        if self.pieceType == "pawn":
            squareNameSpec = [char for char in self.pieceSquare]
            if squareNameSpec[1] == '8' and self.pieceColour == "white":
                return True
            elif squareNameSpec[1] == '1' and self.pieceColour == "black":
                return True
        return False

    def promote(self, newPiece: str):
        """ Promotes the piece to a new piece.

        Args:
            newPiece (string): the type of piece to promote to.
        """
        self.pieceType = newPiece

"""piece.py

A piece on the board for a game of chess.

Authors: Jesse Phillips <james@jamesphillipsuk.com>
"""
import PySimpleGUI as psg


class Piece:

    pieceType = ""
    pieceColour = ""
    pieceSquare = ""

    def __init__(self, pType: str, colour: str, square: str):
        """Create an instance of a chess piece.

        Args:
            pType (string): the type of piece.  IE: "king", "pawn", etc.
            colour (string): the colour of the piece.
            square (string): the name of the square the piece is on.
        """
        self.pieceType = pType
        self.pieceColour = colour
        self.pieceSquare = square

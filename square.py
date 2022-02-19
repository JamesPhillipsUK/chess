"""square.py

A square on the board for a game of chess.

Authors: Jesse Phillips <james@jamesphillipsuk.com>
"""
import PySimpleGUI as psg
from piece import *


class Square(psg.Button):

    currentPiece = Piece

    def setCurrentPiece(self, piece: Piece):
        """Sets the current piece in the suare (if applicable).

        Args:
            piece (Piece): the piece to be set in the square.
        """
        self.currentPiece = piece

    def getCurrentPiece(self):
        """Gets the piece currently on the square.

        Returns:
            Piece: the current piece.
        """
        return self.currentPiece

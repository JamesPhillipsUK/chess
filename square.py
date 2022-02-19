"""square.py

A square on the board for a game of chess.

Authors: Jesse Phillips <james@jamesphillipsuk.com>
"""
import PySimpleGUI as psg
from piece import *


class Square(psg.Button):

    currentPiece = Piece

    def setCurrentPiece(self, piece: Piece):
        """Sets the current piece in the square (if applicable).

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

    def getCurrentImage(self):
        """Gets the image which should be on the square.

        Returns:
            string: a description of the image (sq.colour+p.colour+p.type)
        """
        isWhiteSquare = False
        squareNameSpec = [char for char in self.Key]
        if squareNameSpec[0] in ['a', 'c', 'e', 'g']:
            if int(squareNameSpec[1]) % 2 == 0:
                isWhiteSquare = True
        else:
            if int(squareNameSpec[1]) % 2 != 0:
                isWhiteSquare = True
        if (self.currentPiece.pieceColour == "white" or
           self.currentPiece.pieceColour == "black"):
            if isWhiteSquare:
                return ("white" +
                        self.currentPiece.pieceColour +
                        self.currentPiece.pieceType)
            return ("black" +
                    self.currentPiece.pieceColour +
                    self.currentPiece.pieceType)
        else:
            if isWhiteSquare:
                return "white"
            return "black"

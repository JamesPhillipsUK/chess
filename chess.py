import PySimpleGUI as psg
from board import *

class Chess:
  def main():
    board = Board()
    board.buildBoard(psg.Window(title="Chess", layout=[[]], margins=(296, 296)))
    board.launchGameLoop()
    print("ran successfully!")
    
  if __name__ == "__main__":
    main()
import PySimpleGUI as psg


class Board:
    window = psg.Window(title="Chess")

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

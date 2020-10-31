board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
play = True
from random import *


class tictactoe:
    def __init__(self):
        self.checker = True
        self.board = board

    def reset(self):
        self.board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        pass

    def checkwinner(self):
        # player 1 check
        if self.board[0] == 1 and self.board[1] == 1 and self.board[2] == 1:
            self.checker = False
            return self.checker
        if self.board[3] == 1 and self.board[4] == 1 and self.board[5] == 1:
            self.checker = False
            return self.checker
        if self.board[6] == 1 and self.board[7] == 1 and self.board[8] == 1:
            self.checker = False
            return self.checker
        if self.board[0] == 1 and self.board[3] == 1 and self.board[6] == 1:
            self.checker = False
            return self.checker
        if self.board[1] == 1 and self.board[4] == 1 and self.board[7] == 1:
            self.checker = False
            return self.checker
        if self.board[2] == 1 and self.board[5] == 1 and self.board[8] == 1:
            self.checker = False
            return self.checker
        if self.board[0] == 1 and self.board[4] == 1 and self.board[8] == 1:
            self.checker = False
            return self.checker
        if self.board[2] == 1 and self.board[4] == 1 and self.board[6] == 1:
            self.checker = False
            return self.checker
        # computer check
        if self.board[0] == 2 and self.board[1] == 2 and self.board[2] == 2:
            self.checker = False
            return self.checker
        if self.board[3] == 2 and self.board[4] == 2 and self.board[5] == 2:
            self.checker = False
            return self.checker
        if self.board[6] == 2 and self.board[7] == 2 and self.board[8] == 2:
            self.checker = False
            return self.checker
        if self.board[0] == 2 and self.board[3] == 2 and self.board[6] == 2:
            self.checker = False
            return self.checker
        if self.board[1] == 2 and self.board[4] == 2 and self.board[7] == 2:
            self.checker = False
            return self.checker
        if self.board[2] == 2 and self.board[5] == 2 and self.board[8] == 2:
            self.checker = False
            return self.checker
        if self.board[0] == 2 and self.board[4] == 2 and self.board[8] == 2:
            self.checker = False
            return self.checker
        if self.board[2] == 2 and self.board[4] == 2 and self.board[6] == 2:
            self.checker = False
            return self.checker

    def printboard(self):
        print("\n", self.board[0], "|", self.board[1], "|", self.board[2], "|\n", self.board[3], "|", self.board[4],
              "|",
              self.board[5], "|\n", self.board[6], "|", self.board[7], "|", self.board[8], "|")

    def playerset(self, felder):
        print(felder)
        if felder == "1":
            if self.board[0] == 0:
                self.board[0] = 1
            else:
                print("Das Feld ist leider schon voll")
        if felder == "2":
            if self.board[1] == 0:
                self.board[1] = 1
            else:
                print("Das Feld ist leider schon voll")
        if felder == "3":
            if self.board[2] == 0:
                self.board[2] = 1
            else:
                print("Das Feld ist leider schon voll")
        if felder == "4":
            if self.board[3] == 0:
                self.board[3] = 1
            else:
                print("Das Feld ist leider schon voll")
        if felder == "5":
            if self.board[4] == 0:
                self.board[4] = 1
            else:
                print("Das Feld ist leider schon voll")
        if felder == "6":
            if self.board[5] == 0:
                self.board[5] = 1
            else:
                print("Das Feld ist leider schon voll")
        if felder == "7":
            if self.board[6] == 0:
                self.board[6] = 1
            else:
                print("Das Feld ist leider schon voll")
        if felder == "8":
            if self.board[7] == 0:
                self.board[7] = 1
            else:
                print("Das Feld ist leider schon voll")
        if felder == "9":
            if self.board[8] == 0:
                self.board[8] = 1
            else:
                print("Das Feld ist leider schon voll")
        return self.board

    def computerset(self):
        tester = True
        while tester:
            x = randint(1, 9)
            if x == 1:
                if self.board[0] == 0:
                    self.board[0] = 2
                    return self.board
            if x == 2:
                if self.board[1] == 0:
                    self.board[1] = 2
                    return self.board
            if x == 3:
                if self.board[2] == 0:
                    self.board[2] = 2
                    return self.board
            if x == 4:
                if self.board[3] == 0:
                    self.board[3] = 2
                    return self.board
            if x == 5:
                if self.board[4] == 0:
                    self.board[4] = 2
                    return self.board
            if x == 6:
                if self.board[5] == 0:
                    self.board[5] = 2
                    return self.board
            if x == 7:
                if self.board[6] == 0:
                    self.board[6] = 2
                    return self.board
            if x == 8:
                if self.board[7] == 0:
                    self.board[7] = 2
                    return self.board
            if x == 9:
                if self.board[8] == 0:
                    self.board[8] = 2
                    return self.board

    def kidestodes(self):
        pass


if __name__ == "__main__":
    wer = randint(0, 1)
    wer = 1
    print("Wilkommen zu TicTacToe")
    game = tictactoe()
    if wer == 0:
        print("Du fängst an!")
    else:
        print("Der Computer fängt an!")
    while play:
        if wer == 0:
            print("\n")
            print("Wo moechtest du setzen die Felder sind von 1-9 nummeriert")
            game.printboard()
            feld = input("\n:")
            game.playerset(feld)
            game.printboard()
            game.checkwinner()
            if not game.checker:
                print("Du hast gewonnen")
                break
            game.computerset()
            print("Der Computer hat gesetzt")
            game.printboard()
            game.checkwinner()
            if not game.checker:
                print("Der Computer hat gewonnen")
                break
        if wer == 1:
            game.computerset()
            print("Der Computer hat gesetzt")
            game.printboard()
            game.checkwinner()
            if not game.checker:
                print("Der Computer hat gewonnen")
                break
            print("\n")
            print("Wo moechtest du setzen die Felder sind von 1-9 nummeriert")
            game.printboard()
            feld = input("\n:")
            game.playerset(feld)
            game.printboard()
            game.checkwinner()
            if not game.checker:
                print("Du hast gewonnen")
                break

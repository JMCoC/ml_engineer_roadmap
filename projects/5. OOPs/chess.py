from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, color, position):
        self.__color = color
        self.__position = position
        
    @abstractmethod
    def validMoves(self):
        pass

    def getColor(self):
        return self.__color
    
    def getPosition(self):
        return self.__position

    def setPosition(self, position):
        self.__position = position

class Pawn(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
    
    def validMoves(self, board):
        print("Valid")

class Rook(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
    
    def validMoves(self):
        print("Valid")

class Knight(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
    
    def validMoves(self):
        print("Valid")

class Bishop(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
    
    def validMoves(self):
        print("Valid")

class Queen(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
    
    def validMoves(self):
        print("Valid")
    
class King(Piece):


    def __init__(self, color, position):
        super().__init__(color, position)
    
    def validMoves(self):
        print("Valid")

class Board:

    def __init__(self):
        self.grid = [[" " for _ in range(8)] for _ in range(8)]
        self.initializeBoard()
    
    def initializeBoard(self):
        self.grid[0][0] = Rook("white", (0, 0))
        self.grid[0][7] = Rook("white", (0, 7))
        self.grid[7][0] = Rook("black", (0, 0))
        self.grid[7][7] = Rook("black", (0, 0))

        self.grid[0][1] = Knight("white", (0, 1))
        self.grid[0][6] = Knight("white", (0, 6))
        self.grid[7][1] = Knight("black", (7, 1))
        self.grid[7][6] = Knight("black", (7, 6))

        self.grid[0][2] = Bishop("white", (0, 2))
        self.grid[0][5] = Bishop("white", (0, 5))
        self.grid[7][2] = Bishop("black", (7, 2))
        self.grid[7][5] = Bishop("black", (7, 5))
        
        self.grid[0][3] = Queen("white", (0, 3))
        self.grid[7][3] = Queen("black", (7, 3))
        
        self.grid[0][4] = King("white", (0, 4))
        self.grid[7][4] = King("black", (7, 4))

        for i in range(8):
            self.grid[1][i] = Pawn("white", (1, i))
            self.grid[6][i] = Pawn("black", (1, i))

    def movePiece():
        pass

    def display(self):
        for row in self.grid:
            print(" | ".join([piece.__class__.__name__[0] if piece != " " else " " for piece in row]))
            print("-" * 31)



class Game:
    def __init__(self):
        self.board = Board()
        self.turn = "white"

    def switchTurn(self):
        self.turn = "black" if self.turn == "white" else "white"

board = Board()
board.display()
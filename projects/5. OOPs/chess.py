from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, color, position):
        self.__color = color
        self.__position = position
        
    @abstractmethod
    def validMoves(self, board):
        pass

    def getColor(self):
        return self.__color
    
    def getPosition(self):
        return self.__position

    def setPosition(self, position):
        if isinstance(position, tuple) and len(position) == 2:
            self.__position = position
        else:
            raise ValueError("Position must be a tuple of (row, column)")

class SlidingPiece(Piece):
    def validMoves(self, board):
        moves = []
        x, y = self.getPosition()

        for dx, dy in self.directions:
            nx, ny = x, y
            while True:
                nx += dx
                ny += dy
                if 0 <= nx < 8 and 0 <= ny < 8:
                    if board.grid[nx][ny] == " ":
                        moves.append((nx, ny))
                    elif isinstance(board.grid[nx][ny], Piece) and board.grid[nx][ny].getColor() != self.getColor():
                        moves.append((nx, ny))
                        break
                    else:
                        break
                else:
                    break
        return moves

class Pawn(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
    
    def validMoves(self, board):
        moves = []
        x, y = self.getPosition()
        direction = 1 if self.getColor() == "white" else -1
        try:
            if board.grid[x + direction][y] == " ":
                moves.append((x + direction, y))
                if board.grid[x + direction * 2][y] == " " and (self.getPosition()[0] == 1 and self.getColor() == "white") or (self.getPosition()[0] == 6 and self.getColor() == "black"):
                    moves.append((x + direction * 2, y))
            if y > 0 and isinstance(board.grid[x + direction][y - 1], Piece) and board.grid[x + direction][y - 1].getColor() != self.getColor():
                moves.append((x + direction, y - 1))
            if y < 7 and isinstance(board.grid[x + direction][y + 1], Piece) and board.grid[x + direction][y + 1].getColor() != self.getColor():
                moves.append((x + direction, y + 1))
        except IndexError:
            return moves
        
        return moves
    
    def promotion(self, color, position, board):
        while True:
            print("1. Rook")
            print("2. Knight")
            print("3. Bishop")
            print("4. Queen")
            try:
                option = int(input("Promote to: "))
                break
            except ValueError:
                print("Please enter a valid number.")
                continue
        if option == 1:
            rook = Rook(color, position)
            board.grid[rook.getPosition()[0]][rook.getPosition()[1]] = rook
        elif  option == 2:
            knight = Knight(color, position)
            board.grid[knight.getPosition()[0]][knight.getPosition()[1]] = knight
        elif  option == 3:
            bishop = Bishop(color, position)
            board.grid[bishop.getPosition()[0]][bishop.getPosition()[1]] = bishop
        elif option == 4:
            queen = Queen(color, position)
            board.grid[queen.getPosition()[0]][queen.getPosition()[1]] = queen
        else:
            print("Invalid option")

class Rook(SlidingPiece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  

class Knight(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
    
    def validMoves(self, board):
        moves = []
        x, y = self.getPosition()

        jumps = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]

        for dx, dy in jumps:
            nx, ny = x, y
            while True:
                nx += dx
                ny += dy
                if 0 <= nx < 8 and 0 <= ny < 8:
                    if board.grid[nx][ny] == " ":
                        moves.append((nx, ny))
                        break
                    elif isinstance(board.grid[nx][ny], Piece) and board.grid[nx][ny].getColor() != self.getColor():
                        moves.append((nx, ny))
                        break
                    else:
                        break
                else:
                    break
        return moves

class Bishop(SlidingPiece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.directions = [(1, 1), (-1, -1), (1, -1), (-1, 1)]  

class Queen(SlidingPiece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]  
    
class King(Piece):
    def __init__(self, color, position): #Add check attribute after
        # self.__check = check
        super().__init__(color, position)
        
    # def getCheck(self):
    #     return self.__check
    
    # def setCheck(self, check):
    #     self.__check = check
    
    # def inCheck(self, board, nextMoves):
    #     moves = self.validMoves(board)
    #     if self.getCheck() == True:
    #         for move in nextMoves:
    #             if move in moves:
    #                 moves.remove(move)
    #         print(moves)
    #         return moves

    def validMoves(self, board):
        moves = []
        x, y = self.getPosition()

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]

        for dx, dy in directions:
            nx, ny = x, y
            while True:
                nx += dx
                ny += dy
                if 0 <= nx < 8 and 0 <= ny < 8:
                    if board.grid[nx][ny] == " ":
                        moves.append((nx, ny))
                        break
                    elif isinstance(board.grid[nx][ny], Piece) and board.grid[nx][ny].getColor() != self.getColor():
                        moves.append((nx, ny))
                        break
                    else:
                        break
                else:
                    break
        return moves

class Board:

    def __init__(self):
        self.grid = [[" " for _ in range(8)] for _ in range(8)]
        self.initializeBoard()
    
    def initializeBoard(self):
        self.grid[0][0] = Rook("white", (0, 0))
        self.grid[0][7] = Rook("white", (0, 7))
        self.grid[7][0] = Rook("black", (7, 0))
        self.grid[7][7] = Rook("black", (7, 7))

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
        
        self.grid[0][4] = King("white", (0, 4)) #check attribute (False)
        self.grid[7][4] = King("black", (7, 4)) #check attribute (False)

        for i in range(8):
            self.grid[1][i] = Pawn("white", (1, i)) #1, i
            self.grid[6][i] = Pawn("black", (6, i)) #6, i
        #pass
        #TEST
        #self.grid[3][0] = Pawn("white", (3, 0))
        #self.grid[2][0] = Pawn("black", (2, 0))
        #self.grid[2][2] = Pawn("black", (2, 2))

    def movePiece(self, start, end):
        piece = self.grid[start[0]][start[1]]
        if piece == " " or piece.getColor() != game.getTurn():
            return False

        valid_moves = piece.validMoves(self)
        if end not in valid_moves:
            return False

        self.grid[end[0]][end[1]] = piece
        self.grid[start[0]][start[1]] = " "
        piece.setPosition(end)
        # nextValidMoves = piece.validMoves(self)
        # for x, y in nextValidMoves:
        #     if isinstance(self.grid[x][y], King) and self.grid[x][y].getColor() != piece.getColor():
        #         print("Atacando rey enemigo")
        #         self.grid[x][y].setCheck(True)
        #         self.grid[x][y].inCheck(self, nextValidMoves)
        #         break
        if isinstance(piece, Pawn) and ((piece.getPosition()[0] == 7 and piece.getColor() == "white") or (piece.getPosition()[0] == 0 and piece.getColor() == "black")):
            piece.promotion(piece.getColor(), piece.getPosition(), self)

        game.switchTurn()
        return True

    def display(self):
        for row in self.grid:
            print(" | ".join([piece.__class__.__name__[0] if piece != " " else " " for piece in row]))
            print("-" * 31)

class Game:
    def __init__(self):
        self.board = Board()
        self.turn = "white"

    def play(self):
        while True:
            self.board.display()
            try:
                s1, s2 = map(int, input("Enter start position (x y): ").split())
                e1, e2 = map(int, input("Enter end position (x y): ").split())
                start = (s1, s2)
                end = (e1, e2)
                if not self.board.movePiece(start, end):
                    print("Invalid move")
            except ValueError:
                print("Invalid input. Please enter numbers separated by space.")
            except IndexError:
                print("Invalid input. Coordinates out of bounds.")

    def switchTurn(self):
        self.turn = "black" if self.turn == "white" else "white"
    
    def getTurn(self):
        return self.turn

#TEST
# board = Board()
# pawn = Pawn("white", (1,0))
# rook = Rook("black", (3,3))
# knight = Knight("white", (3,3))
# bishop = Bishop("white", (3,3))
# queen = Queen("white", (3,3))
# king = King("white", (3,3))
# print(pawn.validMoves(board))
# print(rook.validMoves(board))
# print(knight.validMoves(board))
# print(bishop.validMoves(board))
# print(queen.validMoves(board))
# print(king.validMoves(board))
game = Game()
game.play()
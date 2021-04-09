#CPSC 231
#Name: Daniel Jin
#Tutorial: Shauvik Shadman
#ID: 30107081
#Date: 2019-12-06
#Description: This program will be used with another module, tictactoe.py, which will handle the inputs, draws the game and handle the AI that the user will play against
#this program will code for a game of Tic Tac Toe. Where if there is row, column or diagonal of three consecutives of either X or O will result in a win.
#There will also be functions where you can change the dimensions of the board (max 5 rows and columns) and will also be able to hint out to the user the best spot to play.


#Constants for piece types
EMPTY = 0
X = 1
O = 2
class Board:
    board = None
    #this function passes a two-dimensional list to the variable "board"
    #the function first adds "EMPTY" to the first list "col", for the amount of times inputed in the second parameter
    #then it adds the list, "col". into another list called, "row" for the amount of times inputed in the first parameter
    #therefore, the length of board = the amount of rows, and the length of board[0] = the amount of columns
    #if nothing is inputted for the two parameters, then rows is has a default value of 3 and same for the columns
    #this function will not return anything
    def __init__(self,rows=3,cols=3):
        row = []
        for number in range (rows):
            col = []
            for number in range (cols):
                col.append(EMPTY)
            row.append(col)
        self.board = row
    #this function returns the amount of rows by returning the length of "board"
    def rows(self):
        return (len(self.board))
    #this function returns the amount of columns by returning the length of "board[0]"
    def cols(self):
        return (len(self.board[0]))
    #this function checks the entity in the given row and column and checks if it has "EMPTY" or  not, if it contains "EMPTY" reutrns true, if not returns false
    #row is the first parameter, not including self
    #column is the second parameter, not including self
    def canPlay(self,row,column):
        if self.board[row][column] == EMPTY:
            return True
        else:
            return False
    #this function will change the value("EMPTY") of the given row and column entity into the value of the piece
    #this function will not return a value
    #row is the first parameter, not including self
    #column is the second parameter, not including self
    #piece is the third parameter, not including self
    def play(self,row,column,piece):
        self.board[row][column] = piece
    #this function will check each row in board and check if it contains "EMPTY" in the columns. If there is "EMPTY", it will return False, if not it returns True.
    #this function basically checks if the board is full of pieces other than "EMPTY"
    def full(self):
        for row in self.board:
            if EMPTY in row:
                return False
        return True
    #this function looks at the given row (first parameter) and then checks if in the row, there consists 3 consecutive "pieces" side by side
    #if it does include 3 consecutive pieces it will return True, else it will return false
    #row is the first parameter, not including self
    #piece is the second parameter, not including self
    def winInRow(self,row,piece):
        board = self.board[row]
        colLength = len(board)
        column = 0
        #column+2 because, if the column+2 is greater than the length, it will result in an error due to it not existing.
        while column+2 < colLength:
            if board[column] == piece and board[column+1] == piece and board[column+2] == piece:
                return True
            else:
                column += 1
        return False
    #this function looks at the given column (first parameter) and then checks if in the column, there consists 3 consecutive "pieces" side by side(vertically)
    #if is does include 3 consecutive pieces it will return True, else it will return False
    #column is the first parameter, not including self
    #piece is the second parameter, not including self
    def winInCol(self,col,piece):
        board = self.board
        rowLength = len(board)
        row = 0
        #row+2 because, if the row+2 is greater than the length, it will result in an error due to it not existing.
        while row+2 < rowLength:
            if board[row][col] == piece and board[row+1][col] == piece and board[row+2][col] == piece:
                return True
            else:
                row += 1
        return False
    #this function will look at all the diagonals ("\" and "/") and check if it contains 3 consecutive "pieces" side by side (diagonally)
    #if it does include 3 consecutive pieces, it will return True, else it will return False
    def winInDiag(self,piece):
        board = self.board
        #this is to check top-left corner to bottom-right corner "\"
        #"-2" for the row and col because the two bottom rows will never have enough space in the diagonal to make three consecutive pieces
        #"+1" or "+2" for row and col because then it will check the other piece in the next spot of the diagonal
        for row in range (len(board)-2):
            for col in range (len(board[0])-2):
                if board[row][col] == piece and board[row+1][col+1] == piece and board[row+2][col+2] == piece:
                    return True
        #this is to check top-right corner to bottom-left corner "/"
        for row in range (len(board)-2):
            for col in range (len(board[0])-2):
                if board[row][col+2] == piece and board[row+1][col+1] == piece and board[row+2][col] == piece:
                    return True
        return False
    #this function will check if there is a win in each row, column and diagonal.
    #if there is a win it will return True, if not it will return false
    #piece is the first parameter, not including self
    def won(self, piece):
        for row in range (len(self.board)):
            if self.winInRow(row,piece) == True:
                return True
        for col in range (len(self.board[0])):
            if self.winInCol(col,piece) == True:
                return True
        if self.winInDiag(piece) == True:
            return True
        return False
            
    #this function will temporarily place a piece on each spot on the board and sees what spot results in a win.
    #if there is a win, it will return the following row and column that resulted in a win
    #if it is impossible to get a win, it will return "-1,-1"
    #piece is the first parameter, not including self
    def hint(self, piece):
        for row in range (len(self.board)):
            for col in range(len(self.board[row])):
                if self.canPlay(row,col):
                    self.play(row,col,piece)
                    if self.won(piece):
                        self.play(row,col,EMPTY)
                        return row, col
                    else:
                        self.play(row,col,EMPTY)
        return -1, -1
    
    def gameover(self):
        if self.won(X) or self.won(O) or self.full():
            return True
        return False


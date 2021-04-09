    def winInDiag(self,piece):
        board = self.board
        col = len(board[0])-3
        while col >= 0:
            row = len(board) - 3
            while row >= 0:
                if board[row][col] == piece and board[row+1][col+1] == piece and board[row+2][col+2] == piece:
                    return True
                else:
                    row -= 1
            col -= 1
        col = len(board[0])-3
        while col <= len(board[0])-1:
            row = len(board) - 3
            while row >= 0:
                if (board[row])[col] == piece and (board[row+1])[col-1] == piece and (board[row+2])[col-2] == piece:
                    return True
                else:
                    row -= 1
            col += 1
        return False

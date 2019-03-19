def numRockCaptures(board):
    """
    :type board: List[List(str)]
    :reype: int
    """
    for i in range(8):
        for j in range(8):
            if board[i][j] == 'R':
                x0, y0 = i, j
    
    res = 0
    for i, j in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        x, y = x0 + i, y0 + j
        while 0 <= x < 8 and 0 <= y < 8:
            if board[x][y] == 'p':
                res += 1
                break
            if board[x][y] != '.':
                break
            x, y = x + i, y + j
    return res

if __name__ == '__main__':
    """
    先找到车R的位置
    然后依次从四个方向去遍历
    """
    # test case
    board = [[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
    print(numRockCaptures(board))
def numRockCaptures(board):
    """
    :type board: List[List[str]]
    :rtype: int
    """
    result = 0
    index = 0
    for i in board:
        if 'R' in i:
            row = ''.join(z for z in i if z != '.')
            if 'Rp' in row:
                result += 1
            if 'pR' in row:
                result += 1
            index = i.index("R")
            break
    col = ''.join(board[i][index] for i in range(8) if board[i][index] != '.')
    if 'Rp' in col:
        result += 1
    if 'pR' in col: 
        result += 1

    return result

if __name__ == '__main__':
    """
    找到车的位置，然后将车所在的list转为str
    判断str中是否存在'Rp'和'pR'
    然后再获取车所在列的list，将它转为str
    判断str中是否存在'Rp'和'pR'
    """
    # test case
    board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
    result = numRockCaptures(board)
    print(result)
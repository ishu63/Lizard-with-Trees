def input_board(inputfile, board, n):
    for i in xrange(n):
        lst = [char for char in inputfile.readline().rstrip('\n')]
        board.append(lst)


def failCase(outputfile):
    outputfile.write('FAIL')


def passCase(outputfile, board):
    outputfile.write('OK\n')
    # write_board
    lst1 = []
    for lst in board:
        string1 = ''.join(lst)
        lst1.append(string1)
    string = '\n'.join(lst1)
    outputfile.write(string)


def Check_col_diagonal(board, row, col, n):
    # check for column attacks
    flag = '0'
    for i in range(row - 1, -1, -1):
        if board[i][col] == '2':
            break
        if board[i][col] == '1':
            flag = '-1'
            break
    if flag == '-1':
        return False
    for i in range(row + 1, n, 1):
        if board[i][col] == '2':
            break
        if board[i][col] == '1':
            flag = '-1'
            break
    if flag == '-1':
        return False

    # check for diagonal (quadrant I)
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i][j] == '2':
            break
        if board[i][j] == '1':
            flag = '-1'
            break
    if flag == '-1':
        return False
    # check for diagonal (quadrant II)
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, n, 1)):
        if board[i][j] == '2':
            break
        if board[i][j] == '1':
            flag = '-1'
            break
    if flag == '-1':
        return False
    # check for diagonal (quadrant III)
    for i, j in zip(range(row + 1, n, 1), range(col + 1, n, 1)):
        if board[i][j] == '2':
            break
        if board[i][j] == '1':
            flag = '-1'
            break
    if flag == '-1':
        return False
    # check for diagonal (quadrant IV)
    for i, j in zip(range(row + 1, n, 1), range(col - 1, -1, -1)):
        if board[i][j] == '2':
            break
        if board[i][j] == '1':
            flag = '-1'
            break
    if flag == '-1':
        return False

    # if everything if ok return true
    return True


def Safe(board, n):
    flag = '0'
    for row in range(n):
        if sum(x.count('0') for x in board[row]) <= 0:
            continue
        if '1' in board[row]:
            if '2' not in board[row]:
                continue
            # tree and lizard both are present
            for col in range(n):
                if board[row][col] == '2' or board[row][col] == '1':
                    continue
                for i in range(col - 1, -1, -1):
                    if board[row][i] == '2':
                        break
                    if board[row][i] == '1':
                        flag = '-1'
                        break
                if flag == '-1':
                    continue
                for j in range(col + 1, n, 1):
                    if board[row][i] == '2':
                        break
                    if board[row][i] == '1':
                        flag = '-1'
                        break
                if flag == '-1':
                    continue
                # ------------add checking for column and diagonal for this board[row][col]------------------#
                if Check_col_diagonal(board, row, col, n):
                    return row, col
                    #	else:
                    #		continue

        # no lizard in this row
        for col in range(n):
            if board[row][col] == '2':
                continue
            # this row col position is correct based row checking
            # ------------add checking for column and diagonal for this board[row][col]------------------#
            if Check_col_diagonal(board, row, col, n):
                return row, col
                # else:
                #	continue

    return -1, -1


def DFS(board, placed_liz, total_liz, t, n):
    if placed_liz >= total_liz:
        return True

    for i in range(total_liz):
        row, col = -1, -1
        row, col = Safe(board, n)
        if row != -1:
            board[row][col] = '1'
            if DFS(board, placed_liz + 1, total_liz, t, n):
                return True
            board[row][col] = '0'

    return False


inputfile = open("input.txt", "r")
outputfile = open("output.txt", "w")

algorithm_name = inputfile.readline()
n = int(inputfile.readline())  # n is height-width of square zoo
total_liz = int(inputfile.readline())  # total_liz is no. of baby lizard
# create 2D array for zoo
board = []
input_board(inputfile, board, n)
t = sum(x.count('2') for x in board)  # t is number_of_trees

if algorithm_name == 'BFS\n':
    pass
elif algorithm_name == 'DFS\n':
    if total_liz > (n + t):
        outputfile.write('FAIL')
    elif DFS(board, 0, total_liz, t, n):
        passCase(outputfile, board)
    else:
        outputfile.write('FAIL')
else:  # for Simulated annealing (SA)
    pass

inputfile.close()
outputfile.close()
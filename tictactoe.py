theBoard = {'7':'','8':'','9':'','4':'','5':'','6':'','1':'','2':'','3':''}
boardkeys = []
for key in theBoard:
    boardkeys.append(key)

turn = 'X'
count = 0

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|'+ board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
def checkWin(board, player):
    # Check rows
    if (board['7'] == player and board['8'] == player and board['9'] == player):
        return True
    if (board['4'] == player and board['5'] == player and board['6'] == player):
        return True
    if (board['1'] == player and board['2'] == player and board['3'] == player):
        return True
    
    # Check columns
    if (board['7'] == player and board['4'] == player and board['1'] == player):
        return True
    if (board['8'] == player and board['5'] == player and board['2'] == player):
        return True
    if (board['9'] == player and board['6'] == player and board['3'] == player):
        return True
    
    # Check diagonals
    if (board['7'] == player and board['5'] == player and board['3'] == player):
        return True
    if (board['9'] == player and board['5'] == player and board['1'] == player):
        return True
    
    return False

gameOver = False
for i in range(10):
    printBoard(theBoard)
    print("Its your turn," + turn + ".Move to which place?")
    move = input()
    if move in theBoard and theBoard[move]=='':
        theBoard[move]= turn
        count +=1
    else:
        print('That place is already filled. \nMove to which place? 9 top right and 1 bottom left')
        move = input()
        if move in theBoard and theBoard[move]=='':
            theBoard[move]= turn
            count +=1
        else:
            continue
    
    # Check if current player won
    if checkWin(theBoard, turn):
        printBoard(theBoard)
        print("Player " + turn + " won this game!")
        gameOver = True
        break
    
    # Check for draw
    if count == 9:
        printBoard(theBoard)
        print("This is a tie!")
        gameOver = True
        break
    
    # Switch turns
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
# Print out a board
print('   |   |')
print(' ' + board[2][0] + ' | ' + board[2][1] + ' | ' + board[2][2])
print('   |   |')
print('-----------')
print('   |   |')
print(' ' + board[1][0] + ' | ' + board[1][1] + ' | ' + board[1][2])
print('   |   |')
print('-----------')
print('   |   |')
print(' ' + board[0][0] + ' | ' + board[0][1] + ' | ' + board[0][2])
print('   |   |')

# Win conditions
(board[2][0] == letter and board[2][1] == letter and board[2][2] == letter) or # across the top
(board[1][0] == letter and board[1][1] == letter and board[1][2] == letter) or # across the middle
(board[0][0] == letter and board[0][1] == letter and board[0][2] == letter) or # across the bottom
(board[0][0] == letter and board[1][0] == letter and board[2][0] == letter) or # down the left side
(board[0][1] == letter and board[1][1] == letter and board[2][1] == letter) or # down the middle
(board[0][2] == letter and board[1][2] == letter and board[2][2] == letter) or # down the right side
(board[2][0] == letter and board[1][1] == letter and board[0][2] == letter) or # diagonal
(board[2][2] == letter and board[1][1] == letter and board[0][0] == letter) # diagonal
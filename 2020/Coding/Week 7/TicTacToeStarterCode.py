# Print out a board
print('   |   |')
print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
print('   |   |')
print('-----------')
print('   |   |')
print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
print('   |   |')
print('-----------')
print('   |   |')
print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
print('   |   |')

# Win conditions
(board[6] == letter and board[7] == letter and board[8] == letter) or # across the top
(board[3] == letter and board[4] == letter and board[5] == letter) or # across the middle
(board[0] == letter and board[1] == letter and board[2] == letter) or # across the bottom
(board[6] == letter and board[3] == letter and board[0] == letter) or # down the left side
(board[7] == letter and board[4] == letter and board[1] == letter) or # down the middle
(board[8] == letter and board[5] == letter and board[2] == letter) or # down the right side
(board[6] == letter and board[4] == letter and board[2] == letter) or # diagonal
(board[8] == letter and board[4] == letter and board[0] == letter) # diagonal

import random 

# Draw the board 
def draw_board(board): 
	print("  "+board[7]+" | "+board[8]+" | "+board[9]+" ")
	print("--------------")
	print("  "+board[4]+" | "+board[5]+" | "+board[6]+" ")
	print("--------------")
	print("  "+board[1]+" | "+board[2]+" | "+board[3]+" ")

# Select a marker of either X or O
def player_marker(): 
	marker = " "
	while marker != "X" and marker != "O":
		marker = input("Player 1 choose X or O: ").upper()
	if marker == "X": 
		return ("X", "O")
	else: 
		return ("O", "X")

# Place the marker on the board
def place_marker(board, marker, position):
	board[position] = marker

# Check if the position has already been taken
def check_position(board, position):
	return board[position] == " "

# Check if the board is full
def check_full_board(board):
	for i in range(1,10):
		if check_position(board, i):
			return False
	return True

# Check if a player has won
def check_win(board, mark):
	# Check rows, columns and diagonals
	return ((board[1] == board[2] == board[3] == mark) or
	(board[4] == board[5] == board[6] == mark) or
	(board[7] == board[8] == board[9] == mark) or
	(board[1] == board[4] == board[7] == mark) or
	(board[2] == board[5] == board[8] == mark) or
	(board[3] == board[6] == board[9] == mark) or
	(board[1] == board[5] == board[9] == mark) or
	(board[3] == board[5] == board[7] == mark))

# Select a position
def player_position(board): 
	position = 0
	while position not in range(1,10) or not check_position(board, position): 
		position = int(input("Choose a position (1-9): "))
	return position

# Mini AI function
def mini_ai(board, ai_marker): 
	# Check if AI can win
	for i in range(1,10):
		if check_position(board, i):
			place_marker(board, ai_marker, i)
			if check_win(board, ai_marker):
				return i 
			place_marker(board, " ", i)
	# Check if player can win
	for i in range(1,10):
		if check_position(board, i):
			place_marker(board, player_marker, i)
			if check_win(board, player_marker):
				return i 
			place_marker(board, " ", i) 
	# Try to take a corner
	positions = [1,3,7,9]
	for i in positions:
		if check_position(board, i):
			return i 
	# Try to take center
	if check_position(board, 5):
		return 5
	# Take any other position
	for i in range(1,10):
		if check_position(board, i):
			return i

# Play game
play_game = input("Do you want to play the game? (Y/N): ").lower()
if play_game == "y":
	# Set up the game
	board = [" "] * 10
	player_marker, ai_marker = player_marker()
	turn = random.randint(0, 1) 
	game_on = True

	while game_on: 
		if turn == 0:
			# Player turn
			draw_board(board)
			position = player_position(board)
			place_marker(board, player_marker, position)
			if check_win(board, player_marker):
				draw_board(board)
				print("Player has won!")
				game_on = False
			else: 
				if check_full_board(board):
					draw_board(board)
					print("It's a draw!")
					break
				else:
					turn = 1
		else: 
			# AI turn
			position = mini_ai(board, ai_marker)
			place_marker(board, ai_marker, position)
			if check_win(board, ai_marker):
				draw_board(board)
				print("AI has won!")
				game_on = False
			else:
				if check_full_board(board):
					draw_board(board)
					print("It's a draw!")
					break
				else:
					turn = 0
else:
	print("Goodbye!")
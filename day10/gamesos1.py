import os

play_board = [[7, 8, 9], [4, 5, 6], [1, 2, 3]]

clear = lambda: os.system('cls')
clear()

print("Welcome to Tic Tac Toe\n")

for row in play_board:
	print("-" * 13)
	for index in row:
		print("|", index, end=" ")
	print("|")
print("-" * 13)


print("\nUse your keypad to mark your position")
print("\nPlayer 1 - X\nPlayer 2 - O")


def check_board():
	if play_board[0][0] == "O" and play_board[0][1] == "O" and play_board[0][2] == "O" or play_board[0][0] == "X" and play_board[0][1] == "X" and play_board[0][2] == "X":
		return True
	elif play_board[1][0] == "O" and play_board[1][1] == "O" and play_board[1][2] == "O" or play_board[1][0] == "X" and play_board[1][1] == "X" and play_board[1][2] == "X":
		return True
	elif play_board[2][0] == "O" and play_board[2][1] == "O" and play_board[2][2] == "O" or play_board[2][0] == "X" and play_board[2][1] == "X" and play_board[2][2] == "X":
		return True
	elif play_board[0][0] == "O" and play_board[1][0] == "O" and play_board[2][0] == "O" or play_board[0][0] == "X" and play_board[1][0] == "X" and play_board[2][0] == "X":
		return True
	elif play_board[0][1] == "O" and play_board[1][1] == "O" and play_board[2][1] == "O" or play_board[0][1] == "X" and play_board[1][1] == "X" and play_board[2][1] == "X":
		return True
	elif play_board[0][2] == "O" and play_board[1][2] == "O" and play_board[2][2] == "O" or play_board[0][2] == "X" and play_board[1][2] == "X" and play_board[2][2] == "X":
		return True
	elif play_board[0][0] == "O" and play_board[1][1] == "O" and play_board[2][2] == "O" or play_board[0][0] == "X" and play_board[1][1] == "X" and play_board[2][2] == "X":
		return True
	elif play_board[0][2] == "O" and play_board[1][1] == "O" and play_board[2][0] == "O" or play_board[0][2] == "X" and play_board[1][1] == "X" and play_board[2][0] == "X":
		return True
	else:
		return False

prompting = True

while prompting:
	prev_mark = ""
	rounds = 0
	while (rounds < 9):
		mark_position = int(input("\nMark at: "))

		if 0 < mark_position < 10:

			current_mark = "X" if (prev_mark == "O" or prev_mark == "") else "O"

			i, j = 0, 0

			clear()

			for row in play_board:
				for index in row:
					if index == mark_position:
						play_board[i][j] = current_mark
						prev_mark = current_mark
						rounds += 1
					j += 1

				j = 0
				i += 1

			turn = "X" if (prev_mark == "O") else "O"
			print("Turn for", turn)
			for row in play_board:
				print("-" * 13)
				for index in row:
					# index = " " if str(index).isdigit() else index
					print("|", index, end=" ")
				print("|")
			print("-" * 13)

			status = check_board()
			if status:
				print("Congratulations!!!")
				break
			elif (status == False) and (rounds == 9):
				print("Its a tie!!!")

		else:
			print("Enter the correct position")



	choice = input("\nDo you want to play again? (y/n): ")
	if choice.lower() == 'y':
		clear()
		play_board = [[7, 8, 9], [4, 5, 6], [1, 2, 3]]
		print("Turn for X")
		for row in play_board:
			print("-" * 13)
			for index in row:
				index = " " if str(index).isdigit() else index
				print("|", index, end=" ")
			print("|")
		print("-" * 13)
	else:
		prompting = False
		clear()
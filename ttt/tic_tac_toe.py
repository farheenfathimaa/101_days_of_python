import os
import random

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def print_board(board):
    print("  1 | 2 | 3 ")
    print(" -----------")
    for i in range(3):
        print(f"{i+1} {board[i][0]} | {board[i][1]} | {board[i][2]} ")
        if i < 2:
            print("   ---------")

def check_win(board, player):
    for i in range(3):
        if sum(board[i]) == 15 or sum([board[j][i] for j in range(3)]) == 15:
            return True
    if sum([board[i][i] for i in range(3)]) == 15 or sum([board[i][2 - i] for i in range(3)]) == 15:
        return True
    return False

def is_full(board):
    for row in board:
        if 0 in row:
            return False
    return True

def main():
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    players = ["HUMAN", "COMPUTER"]
    symbols = {players[0]: 'X', players[1]: 'O'}
    choice = input("Choose odd (O) or even (X): ").upper()
    
    if choice not in ['O', 'X']:
        print("Invalid choice. Please choose 'O' or 'X'.")
        return
    
    if choice == 'X':
        players[0], players[1] = players[1], players[0]
    
    while True:
        clear_screen()
        print_board(board)
        
        for turn in range(9):
            print(f"{players[turn % 2]}'s turn:")
            if players[turn % 2] == "HUMAN":
                while True:
                    try:
                        row = int(input("Enter row (1, 2, or 3): ") ) - 1
                        col = int(input("Enter column (1, 2, or 3): ") ) - 1
                        if row in [0, 1, 2] and col in [0, 1, 2] and board[row][col] == 0:
                            board[row][col] = 2 * (turn % 2) + 1
                            break
                        else:
                            print("Invalid move. Try again.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")
            else: # COMPUTER's turn
                empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == 0]
                row, col = random.choice(empty_cells)
                board[row][col] = 2 * (turn % 2) + 1
            
            clear_screen()
            print_board(board)
            
            if check_win(board, players[turn % 2]):
                print(f"{players[turn % 2]} wins!")
                break
            elif is_full(board):
                print("It's a draw!")
                break
        
        play_again = input("Play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

if __name__ == "__main__":
    main()

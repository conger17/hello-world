import random

def make_board():
    return [' '] * 9

def print_board(board):
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()

def print_positions():
    print("\n Position reference:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")
    print()

WINS = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6),
]

def check_winner(board):
    for a, b, c in WINS:
        if board[a] == board[b] == board[c] != ' ':
            return board[a]
    return None

def is_full(board):
    return ' ' not in board

def get_human_move(board):
    while True:
        try:
            move = int(input(" Your move (1-9): ")) - 1
            if 0 <= move <= 8 and board[move] == ' ':
                return move
            print(" Invalid move. Try again.")
        except (ValueError, KeyboardInterrupt):
            print(" Please enter a number 1-9.")

def ai_move(board, ai='O', human='X'):
    # Try to win
    for a, b, c in WINS:
        for i, j, k in [(a, b, c), (b, a, c), (c, a, b)]:
            if board[i] == ' ' and board[j] == board[k] == ai:
                return i
    # Block human
    for a, b, c in WINS:
        for i, j, k in [(a, b, c), (b, a, c), (c, a, b)]:
            if board[i] == ' ' and board[j] == board[k] == human:
                return i
    # Take center
    if board[4] == ' ':
        return 4
    # Take corner
    corners = [i for i in [0, 2, 6, 8] if board[i] == ' ']
    if corners:
        return random.choice(corners)
    # Take any open
    return random.choice([i for i, v in enumerate(board) if v == ' '])

def play_game():
    print("\n=== TIC-TAC-TOE ===")
    print(" You are X  |  AI is O")
    print_positions()

    board = make_board()
    current = 'X'

    while True:
        print_board(board)

        if current == 'X':
            move = get_human_move(board)
        else:
            print(" AI is thinking...")
            move = ai_move(board, ai='O', human='X')
            print(f" AI played position {move + 1}")

        board[move] = current
        winner = check_winner(board)

        if winner:
            print_board(board)
            if winner == 'X':
                print(" You win! Congratulations!")
            else:
                print(" AI wins! Better luck next time.")
            return

        if is_full(board):
            print_board(board)
            print(" It's a draw!")
            return

        current = 'O' if current == 'X' else 'X'

def main():
    while True:
        play_game()
        again = input("\n Play again? (y/n): ").strip().lower()
        if again != 'y':
            print(" Thanks for playing!")
            break

if __name__ == '__main__':
    main()

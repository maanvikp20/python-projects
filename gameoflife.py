import random
import time

def dead_state(width, height):
    return [[0 for _ in range(width)] for _ in range(height)]

def random_state(width, height):
    state = dead_state(width, height)
    for i in range(height):
        for j in range(width):
            state[i][j] = 1 if random.random() < 0.5 else 0
    return state

def render(board):
    print("-" * (len(board[0]) + 2))
    for row in board:
        print("|", end="")
        for cell in row:
            if cell == 0:
                print(" ", end="")
            elif cell == 1:
                print("#", end="")
        print("|")
    print("-" * (len(board[0]) + 2))

def count_neighbors(board, x, y):
    directions = [(-1, -1), (-1, 0), (-1, 1), 
                  (0, -1),         (0, 1), 
                  (1, -1), (1, 0), (1, 1)]
    count = 0
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
            count += board[nx][ny]
    return count

def next_board_state(board):
    new_board = dead_state(len(board[0]), len(board))
    for x in range(len(board)):
        for y in range(len(board[x])):
            live_neighbors = count_neighbors(board, x, y)
            if board[x][y] == 1:
                if live_neighbors < 2 or live_neighbors > 3:
                    new_board[x][y] = 0
                else:
                    new_board[x][y] = 1
            else:
                if live_neighbors == 3:
                    new_board[x][y] = 1
    return new_board

def load_board_state(filename):
    board = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                row = [int(char) for char in line.strip()]  # Convert each character to an integer
                board.append(row)
        if not board:  # Handle empty file case
            return None
        return board
    except FileNotFoundError:
        return None

def main():
    board = load_board_state('toad.txt')
    if board is None:
        board = random_state(10, 10)

    for _ in range(10):
        render(board)
        board = next_board_state(board)
        time.sleep(0.5)  # Add delay to observe changes

main()

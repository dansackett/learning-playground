#!bin/python
import sys
import time
import random

from patterns import patterns


class Cell(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.state = False
        self.neighbors = []

    def __str__(self):
        return 'X' if self.state else ' '

    def set_state(self, state):
        self.state = state

    def get_coords(self):
        return (self.x, self.y)

    def set_neighbors(self, board):
        self.neighbors = []
        x, y = self.get_coords()

        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                conditions = all([
                    self.in_board(board, x, y), # Coords in board
                    self.in_board(board, i, j), # Neighbor in board
                    x != i or y != j,           # Not duplicate of x or y
                ])

                if conditions and board[i][j].state:
                    self.neighbors.append((i, j))

    def in_board(self, board, x, y):
        return len(board[0]) > x > -1 and len(board[0]) > y > -1

    def update(self):
        if self.state:
            self.state = True if len(self.neighbors) in [2, 3] else False
        else:
            self.state = True if len(self.neighbors) == 3 else False


class Board(object):
    def __init__(self, board_size, initial=None):
        self.board_size = board_size
        self.board = [[None] * board_size for x in xrange(board_size)]
        self.build(initial)

    def build(self, initial):
        for row in xrange(self.board_size):
            for col in xrange(self.board_size):
                self.board[row][col] = Cell(row, col)

                if (row, col) in initial:
                    self.board[row][col].set_state(True)

        self.set_neighbors()

    def set_neighbors(self):
        for row in self.board:
            for col in row:
                self.board[col.x][col.y].set_neighbors(self.board)

    def display(self):
        for row in self.board:
            print ''.join(str(i) for i in row)

    def update(self):
        for row in self.board:
            for col in row:
                self.board[col.x][col.y].update()

        return [y.get_coords() for x in self.board for y in x if y.state]


def clear_screen():
    sys.stdout.write('\033[H')
    sys.stdout.write('\033[J')


def main(seed, size=30, iterations=75):
    board = Board(size, initial=seed)
    board.display()

    for x in xrange(iterations):
        clear_screen()
        board.display()
        board = Board(size, initial=board.update())
        time.sleep(0.1)


if __name__ == '__main__':
    pattern = patterns[random.choice(patterns.keys())]
    main(pattern)

import re

class Board:
    SIZE = 5

    def __init__(self, board_input):
        board_line_regex = "\s*(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)"
        self.board = [re.match(board_line_regex, row).groups() for row in board_input.split('\n') if row != '']
        self.called = [[False]*5 for _ in range(5)]

    def call_number(self, number):
        for r in range(Board.SIZE):
            for c in range(Board.SIZE):
                if self.board[r][c] == number: self.called[r][c] = True

    def is_won(self):
        # check rows
        for row in self.called: 
            if row.count(True) == Board.SIZE: return True
        # check columns
        for i in range(Board.SIZE):
            column = [row[i] for row in self.called]
            if column.count(True) == Board.SIZE: return True
        return False

    def sum_of_uncalled(self):
        total = 0
        for r in range(Board.SIZE):
            for c in range(Board.SIZE):
                if not self.called[r][c]: total += int(self.board[r][c])
        return total


with open('input.txt') as f:
    lines = [x for x in f.read().split('\n\n') if x != '']
    called_numbers = lines[0].split(',')
    board_inputs = lines[1:]
    boards = [Board(i) for i in board_inputs]


def part_1():
    print("--- PART 1 ---")
    for num in called_numbers:
        for board in boards:
            board.call_number(num)
            if board.is_won():
                print(int(num) * board.sum_of_uncalled())
                return

def part_2():
    print("--- PART 2 ---")
    current_boards = boards
    for num in called_numbers:
        unwon_boards = []
        for board in current_boards:
            board.call_number(num)
            if board.is_won(): last_won = int(num) * board.sum_of_uncalled()
            else: unwon_boards.append(board)
        current_boards = unwon_boards
    print(last_won)


part_1()
part_2()


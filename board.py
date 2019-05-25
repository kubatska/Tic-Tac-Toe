from binary_search_tree import *


def generate_winning_combinations():
    ### this function was written by Oles Dobosevych
    combinations = []
    for i in range(3):
        combination1 = []
        combination2 = []
        for j in range(3):
            combination1.append((i, j))
            combination2.append((j, i))
        combinations.append(combination1)
        combinations.append(combination2)

    combinations.append([(0, 0), (1, 1), (2, 2)])
    combinations.append([(0, 2), (1, 1), (2, 0)])
    return combinations


class Board:
    """Class for board representation in game Tic-Tac-Toe"""
    def __init__(self):
        self.field = [ [None] * 3 ] * 3
        self.last_move = [None] * 3


    def if_won(self):
        """Determine if there are win combonations on field."""
        win_comb = generate_winning_combinations()
        for coord in win_comb:
            lst_0 = []
            lst_x = []
            for coo in coord:
                point = self.field[coo[0]][coo[1]]
                if point != None:
                    if point == "0":
                        lst_0.append(point)
                    if point == "x":
                        lst_x.append(point)
            if len(lst_0) == 3:
                return -1
            if len(lst_x) == 3:
                return 1
        return 0

    def __str__(self):
        all_string = ""
        for i in range(3):
            for j in range(3):
                p = self.field[i][j]
                if p == None:
                    all_string += "_ "
                else:
                    all_string += p + " "
            all_string += "\n"
        return all_string

    
    def empty_list(self):
        """Return a list with empty coordinates."""
        lst = []
        for i in range(3):
            for j in range(3):
                if self.field[i][j] == None:
                    lst.append([i, j])
        return lst

    def set_null(self, new_move):
        """Set a "0" in field."""
        self.field[new_move[0]][new_move[0]] = "0"

    def set_cross(self, new_move):
        """Set a "x" in field."""
        self.field[new_move[0]][new_move[0]] = "x"

    def count_wins(self):
        win_x = 0
        win_0 = 0
        if self.if_won() == "x":
            win_x += 1
        if self.if_won() == "0":
            win_0 += 1
        return [win_x, win_0]



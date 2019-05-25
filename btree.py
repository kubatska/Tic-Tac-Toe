from linked_binary_tree import LinkedBinaryTree
from board import Board
import random
import copy

def make_tree(previous):
    """Сonstructing a game tree, by extending 
    (by adding two child vertices) from the root of a tree """
    # previous it is Board()
    if previous.if_won() == -1 or previous.if_won() == 1:
        return None
    
    new_move_left = random.choice(previous.empty_list())
    tree = LinkedBinaryTree(previous)

    if len(previous.empty_list()) == 0:
        return None
    new_previous = copy.deepcopy(previous)
    new_previous.set_null(new_move_left)

    tree.left_child = LinkedBinaryTree(new_previous)
    make_tree(new_previous)
    
    if len(new_previous.empty_list()) == 0:
        return None
    new_move_right = random.choice(new_previous.empty_list())
    n_new_previous = copy.deepcopy(new_previous)
    n_new_previous.set_null(new_move_right)

    tree.right_child = LinkedBinaryTree(n_new_previous)
    make_tree(n_new_previous)










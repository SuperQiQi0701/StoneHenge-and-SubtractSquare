"""
A module for strategies.

NOTE: Make sure this file adheres to python-ta.
Adjust the type annotations as needed, and implement both a recursive
and an iterative version of minimax.
"""
from typing import Any
from typing import List
from game_state import GameState
from stack import Stack
from IterativeMinimax import IterativeMinimax

# TODO: Adjust the type annotation as needed.


def interactive_strategy(game: Any) -> Any:
    """
    Return a move for game through interactively asking the user for input.
    """
    move = input("Enter a move: ")
    return game.str_to_move(move)


def rough_outcome_strategy(game: Any) -> Any:
    """
    Return a move for game by picking a move which results in a state with
    the lowest rough_outcome() for the opponent.

    NOTE: game.rough_outcome() should do the following:
        - For a state that's over, it returns the score for the current
          player of that state.
        - For a state that's not over:
            - If there is a move that results in the current player winning,
              return 1.
            - If all moves result in states where the other player can
              immediately win, return -1.
            - Otherwise; return a number between -1 and 1 corresponding to how
              'likely' the current player will win from the current state.

        In essence: rough_outcome() will only look 1 or 2 states ahead to
        'guess' the outcome of the game, but no further. It's better than
        random, but worse than minimax.
    """
    current_state = game.current_state
    best_move = None
    best_outcome = -2  # Temporarily -- just so we can replace this easily later

    # Get the move that results in the lowest rough_outcome for the opponent
    for move in current_state.get_possible_moves():
        new_state = current_state.make_move(move)

        # We multiply the below by -1 since a state that's bad for the opponent
        # is good for us.
        guessed_score = new_state.rough_outcome() * -1
        if guessed_score > best_outcome:
            best_outcome = guessed_score
            best_move = move

    # Return the move that resulted in the best rough_outcome
    return best_move


# TODO: Implement a recursive version of the minimax strategy.

def minimax_recursive_strategy(game: Any) -> Any:
    """
    Return a move that minimizes the possible loss for a player, use recursion.
    """
    state = game.current_state
    next_score = [helper_mr(game, state.make_move(c)) * -1
                  for c in state.get_possible_moves()]
    highest_score = max(next_score)
    best_move_index = next_score.index(highest_score)
    return game.current_state.get_possible_moves()[best_move_index]


def helper_mr(game: Any, state: GameState)-> int:
    """
    Return the maximum score of state's next states.
    """
    old_state = game.current_state
    if game.is_over(state):
        game.current_state = state
        if game.is_winner(state.get_current_player_name()):
            game.current_state = old_state
            return 1
        elif game.is_winner('p1') or game.is_winner('p2'):
            game.current_state = old_state
            return -1
        game.current_state = old_state
        return 0
    else:
        result = []
        moves = state.get_possible_moves()
        for move in moves:
            new_state = state.make_move(move)
            result.append(helper_mr(game, new_state) * -1)
        return max(result)

# TODO: Implement an iterative version of the minimax strategy.


def helper_mi_add(s: Stack, lst: list) -> None:
    """
    A helper function for minimax_iterative_strategy. Help to add items from lst
    to stack s.
    """
    for item in lst:
        s.add(item)


def helper_mi_score(current_item: IterativeMinimax,
                    old_items: List[IterativeMinimax]) -> None:
    """
    A helper function for minimax_iterative_strategy. Help to update the score
    of self by it's children's score.
    """
    next_score = []
    for child in current_item.children:
        for item in old_items:
            if child == item:
                next_score.append(item.score)
    current_item.score = max([scores * -1 for scores in next_score])


def minimax_iterative_strategy(game: Any) -> Any:
    """
    Return a move that minimizes the possible loss for a player, iteratively.
    """
    current_state = IterativeMinimax(game.current_state)
    s = Stack()
    s.add(current_state)
    old_items = []

    while not s.is_empty():
        current_item = s.remove()
        if current_item.state.get_possible_moves() != []:
            if not current_item.is_visited():
                movement = current_item.state.get_possible_moves()
                new_states = [IterativeMinimax
                              (current_item.state.make_move(move))
                              for move in movement]

                current_item.children = [child for child in new_states]
                s.add(current_item)
                helper_mi_add(s, new_states)

            elif current_item.is_visited():
                helper_mi_score(current_item, old_items)
                old_items.append(current_item)

        if current_item.state.get_possible_moves() == []:
            old_state = game.current_state
            game.current_state = current_item.state
            if game.is_winner(game.current_state.get_current_player_name()):
                current_item.score = 1
            if game.is_winner('p1') or game.is_winner('p2'):
                current_item.score = -1
            else:
                current_item.score = 0
            old_items.append(current_item)
            game.current_state = old_state

    choices = [child.score * -1 for child in current_state.children]
    best_move = choices.index(max(choices))
    return game.current_state.get_possible_moves()[best_move]


if __name__ == "__main__":
    from python_ta import check_all

    check_all(config="a2_pyta.txt")

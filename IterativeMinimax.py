"""
A module for a class named IterativeMinimax.
"""
from typing import Any
from game_state import GameState


class IterativeMinimax:
    """
    The state of the IterativeMinimax state at a certain point in game.

    === Attributes ===
    state: the current state of IterativeMinimax
    children: the children of IterativeMinimax, in other words, a list of
    new states for the current state's next states.
    score: the score of IterativeMinimax, can only be -1, 0, or 1.
    """
    state: GameState
    children: list
    score: int

    def __init__(self, state: Any, children=None, score=None):
        """
        Initialize a IterativeMinimax.
        """
        self.state = state
        self.children = children
        self.score = score

    def is_visited(self) -> None:
        """
        Return True if the current IterativeMinimax is visited, False if not.

        :rtype: bool
        """
        if self.children is None:
            return False
        return True

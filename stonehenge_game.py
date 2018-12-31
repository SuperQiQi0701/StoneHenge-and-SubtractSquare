"""
A module for StonehengeGame.
"""

from game import Game
from stonehenge_state import StonehengeState

LETTER = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
          'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def calculate_num(length: int) -> int:
    """
    Calculate the number of cells for a Stonghenge with side length length.
    :type length: int
    :rtype: int
    """
    acc = 0
    for i in range(length):
        acc += i + 2
    acc += length
    return acc


class StonehengeGame(Game):
    """
    Abstract class for a game called Stonehenge, to be played with two players.

     === Attributes ===
    is_p1_turn - whether it is p1's turn, if not, then it is p2's turn.
    current_state - the current state of the game StonehengeGame.
    """

    def __init__(self, p1_starts: bool) -> None:
        """
        Initialize this StonehengeGame, using p1_starts to find who the first
        player is.

        :type p1_starts: bool
        :rtype: None
        """
        self.p1_starts = p1_starts
        side_length = input("Enter the side length of the board: ")
        while not (side_length.isdigit() and 0 < int(side_length) <= 5):
            side_length = input("Enter the side length of the board: ")

        cells = LETTER[0: calculate_num(int(side_length))]
        self.current_state = StonehengeState(p1_starts, int(side_length), cells)

    def get_instructions(self) -> str:
        """
        Return the instructions for this StonehengeGame.

        :rtype: str
        """
        return " Players take turns claiming cells (in the diagram: circles " \
               "labelled with a capital letter). When a player captures at " \
               "least half of the cells in a ley-line (in the diagram: " \
               "hexagons with a line connecting it to cells), then the player" \
               "captures that ley-line. The  rst player to capture at least " \
               "half of the ley-lines is the winner. A ley-line, once " \
               "claimed cannot be taken by the other player."

    def is_over(self, state: StonehengeState) -> bool:
        """
        Return whether or not this StonehengeGame is over at state.

        :type state: StonehengeState
        :rtype: bool
        """
        return state.game_over()

    def is_winner(self, player: str) -> bool:
        """
        Return whether player has won the game.

        Precondition: player is 'p1' or 'p2'.

        :type player:str
        :rtype:bool
        """

        if self.is_over(self.current_state):
            if self.current_state.p1_turn:
                return player == 'p2'
            return player == 'p1'
        return False

    def str_to_move(self, move_to_make: str) -> str:
        """
        Return the move that string represents, in this game, want to
        return capitalized letter of move_to_make. If move_to_make is not a
        move, return some invalid move.

        """
        if move_to_make in self.current_state.get_possible_moves():
            return move_to_make.upper()

        return "Invalid move."


if __name__ == "__main__":
    from python_ta import check_all
    check_all(config="a2_pyta.txt")

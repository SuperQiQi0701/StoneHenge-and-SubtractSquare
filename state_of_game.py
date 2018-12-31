"""
State of game module.
classes State, SubstractSquareState and ChopsticsState.
"""

from typing import Any
from typing import List


class State:
    """
    To keep track of the game state, or a snapshot of the current
    situation in the game.

    === Attributes ===
    is_p1_turn - whether it is p1's turn, if not, then it is p2's turn
    valid_moves - all valid moves
    """
    is_p1_turn: bool
    valid_moves: List[int]

    def __init__(self, is_p1_turn: bool) -> None:
        """
        Initilaize a new state, setting up whose turn with is_p1_turn
        and valid moves with an empty valid_moves list.

        :type is_p1_turn: bool
        :rtype: None

        >>> a = State(True)
        >>> a.is_p1_turn
        True
        >>> a.get_current_player_name()
        'p1'
        """
        self.is_p1_turn = is_p1_turn
        self.valid_moves = []

    def __eq__(self, other: Any) -> bool:
        """
        Return whether self is equivalent to other.
        :type other: Any
        :rtype: bool

        >>> a = State(True)
        >>> b = State(True)
        >>> a == b
        True
        """
        return isinstance(self, State) and isinstance(other, State) \
               and type(self) == type(other) \
               and self.valid_moves == other.valid_moves

    def __str__(self) -> str:
        """
        Return a string representation of self.
        :rtype: str

        """
        raise NotImplementedError

    def get_possible_moves(self) -> list:
        """
        Return the possible moves in the current state.
        :rtype: list
        """
        raise NotImplementedError

    def is_valid_move(self, move_to_make: str) -> bool:
        """
        Determine if move, move_to_make, is valid to move in the current state.
        If move_to_make is valid to move, return True; otherwise, return False.

        :type move_to_make: str
        :rtype: bool

        >>> a = State(True)
        >>> a.is_valid_move("bhuh")
        False
        """
        return move_to_make in self.valid_moves

    def get_current_player_name(self) -> str:
        """
        Return the name of the current player. If the current player is
        player 1, return 'p1', otherwise, return 'p2'.

        :type: str
        >>> a = State(True)
        >>> a.get_current_player_name()
        'p1'
        """
        if self.is_p1_turn:
            return "p1"
        return "p2"

    def make_move(self, move_to_make: str):
        """
        Make a move, move_to_make on the game, and return the new state of the
        game.

        :type move_to_make: str
        :rtype: State
        """
        raise NotImplementedError


class SubstractSquareState(State):
    """
    Represents the current state of the game: Substract Square.

     === Attributes ===
    is_p1_turn - whether it is player 1's turn or not
    number - the current number for Substract Square game's state.
    """
    is_p1_turn: bool
    number: int

    def __init__(self, is_p1_turn: bool, number: int) -> None:
        """
        Initialize new SubstractSquareState self, setting up whose turn with
        is_p1_turn and current number with number.

        :type is_p1_turn: bool
        :type number: int

        >>> a = SubstractSquareState(True, 30)
        >>> a.is_p1_turn
        True
        >>> a.number
        30
        >>> a.valid_moves
        [1, 4, 9, 16, 25]
        """
        super().__init__(is_p1_turn)
        self.number = int(number)
        self.valid_moves = []
        for i in range(1, int(self.number ** 0.5) + 1):
            self.valid_moves.append(i ** 2)

    def __eq__(self, other: Any) -> bool:
        """
        Return whether self is equivalent to other.

        :param other: Any
        :rtype: bool
        >>> a = SubstractSquareState(True, 30)
        >>> b = SubstractSquareState(True, 30)
        >>> c = SubstractSquareState(True, 10)
        >>> a == b
        True
        >>> a == c
        False
        """
        return self.is_p1_turn == other.is_p1_turn \
            and self.number == other.number

    def __str__(self) -> str:
        """
        Return a string representation of SubstractSquareState self.

        :rtype: str

        >>> print(SubstractSquareState(True, 30))
        The current value is: 30
        """
        return "The current value is: " + str(self.number)

    def get_possible_moves(self) -> list:
        """
        Return a list of possible moves for the Substract Square game.

        :rtype:list

        >>> a = SubstractSquareState(True, 4)
        >>> a.get_possible_moves()
        [1, 4]
        """
        return self.valid_moves

    def is_valid_move(self, move_to_make: int) -> bool:
        """

        Determine if move, move_to_make, is valid to move in the current state.
        If move_to_make is valid to move, return True; otherwise, return False.
        :type move_to_make: int
        :rtype: bool

        >>> a = SubstractSquareState(True, 4)
        >>> a.is_valid_move(1)
        True
        >>> a.is_valid_move(9)
        False
        """
        return move_to_make in self.valid_moves

    def make_move(self, move_to_make: int) -> State:
        """
        Make a move, move_to_make on the game Substract Square,
        and return the new state of the game.

        :type move_to_make: int
        :rtype: State

        >>> a = SubstractSquareState(True, 4)
        >>> b = a.make_move(4)
        >>> b.get_current_player_name()
        'p2'
        >>> b.number
        0
        """
        new_state = SubstractSquareState(not self.is_p1_turn,
                                         self.number - move_to_make)
        return new_state

    def game_over(self) -> bool:
        """
        To help determine if the game is over.
        If the game is over, return True; otherwise, return false.
        :rtype: bool

        >>> a = SubstractSquareState(True, 30)
        >>> a.game_over()
        False
        >>> b = SubstractSquareState(True, 0)
        >>> b.game_over()
        True
        """
        return self.number == 0


class ChopsticsState(State):
    """
    Represents the current state of the game: Chopsticks.

    === Attributes ===
    is_p1_turn - whether it is p1's turn, if not, then it is p2's turn
    p1 - represent the number of fingers pointing up on player1's left and right
    hand.
    p2 - represent the number of fingers pointing up on player2's left and right
    hand.
    """
    is_p1_turn: bool
    p1: List[int]
    p2: List[int]

    def __init__(self, is_p1_turn: bool) -> None:
        """
        Initialize new ChopsticsState self, setting up whose turn with
        is_p1_turn, and setting the hands of both players with [1, 1].

        :type is_p1_turn: bool
        :rtype: None

        >>> a = ChopsticsState(True)
        >>> a.is_p1_turn
        True
        >>> a.p1
        [1, 1]
        >>> a.p2
        [1, 1]
        """
        super().__init__(is_p1_turn)
        self.p1 = [1, 1]
        self.p2 = [1, 1]

    def __eq__(self, other: Any) -> bool:
        """
        Return whether self is equivalent to other.

        :type other: Any
        :rtype: bool

        >>> a = ChopsticsState(True)
        >>> b = ChopsticsState(False)
        >>> c = ChopsticsState(True)
        >>> a == c
        True
        >>> a == b
        False
        """
        return self.is_p1_turn == other.is_p1_turn and \
               type(self) == type(other) and self.p1 == self.p1 \
               and self.p2 == self.p2

    def __str__(self) -> str:
        """
        Return a string representation of ChopsticksState self.
        :rtype: str

        >>> print(ChopsticsState(True))
        Player 1: 1 - 1 ; Player 2: 1 - 1.
        """
        template = "Player 1: {} - {} ; Player 2: {} - {}."
        return template.format(self.p1[0], self.p1[1],
                               self.p2[0], self.p2[1])

    def get_possible_moves(self) -> list:
        """
        Return a list of possible moves for the Chopsticks game.
        :rtype: list

        >>> a = ChopsticsState(True)
        >>> a.get_possible_moves()
        ['ll', 'lr', 'rl', 'rr']
        """
        result = []
        if self.is_p1_turn:
            if self.p1[0] != 0:
                if self.p2[0] != 0:
                    result.append("ll")
                if self.p2[1] != 0:
                    result.append("lr")
            if self.p1[1] != 0:
                if self.p2[0] != 0:
                    result.append("rl")
                if self.p2[1] != 0:
                    result.append("rr")
        if not self.is_p1_turn:
            if self.p2[0] != 0:
                if self.p1[0] != 0:
                    result.append("ll")
                if self.p1[1] != 0:
                    result.append("lr")
            if self.p2[1] != 0:
                if self.p1[0] != 0:
                    result.append("rl")
                if self.p1[1] != 0:
                    result.append("rr")
        return result

    def is_valid_move(self, move_to_make) -> bool:
        """
        Determine if move, move_to_make, is valid to move in the current state.
        If move_to_make is valid to move, return True; otherwise,
        return False.
        :type move_to_make:
        :rtype:bool

        >>> a = ChopsticsState(True)
        >>> a.is_valid_move('ll')
        True
        """
        return move_to_make in self.get_possible_moves()

    def make_move(self, move_to_make: str) -> State:
        """
        Make a move, move_to_make on the game Chopsticks,
        and return the new state of the game.
        :type move_to_make:str
        :rtype: State

        >>> a = ChopsticsState(True)
        >>> b = a.make_move('ll')
        >>> b.get_current_player_name()
        'p2'
        >>> b.p2
        [2, 1]
        """
        new_state = ChopsticsState(not self.is_p1_turn)
        new_state.p1[0] = self.p1[0]
        new_state.p1[1] = self.p1[1]
        new_state.p2[0] = self.p2[0]
        new_state.p2[1] = self.p2[1]
        if self.is_p1_turn:
            if move_to_make == "ll":
                new_state.p2[0] = self.p1[0] + self.p2[0]
            if move_to_make == "lr":
                new_state.p2[1] = self.p1[0] + self.p2[1]
            if move_to_make == "rl":
                new_state.p2[0] = self.p1[1] + self.p2[0]
            if move_to_make == "rr":
                new_state.p2[1] = self.p1[1] + self.p2[1]
        else:
            if move_to_make == "ll":
                new_state.p1[0] = self.p1[0] + self.p2[0]
            if move_to_make == "lr":
                new_state.p1[1] = self.p1[1] + self.p2[0]
            if move_to_make == "rl":
                new_state.p1[0] = self.p1[0] + self.p2[1]
            if move_to_make == "rr":
                new_state.p1[1] = self.p1[1] + self.p2[1]

        if new_state.p1[0] >= 5:
            new_state.p1[0] -= 5
        if new_state.p1[1] >= 5:
            new_state.p1[1] -= 5
        if new_state.p2[0] >= 5:
            new_state.p2[0] -= 5
        if new_state.p2[1] >= 5:
            new_state.p2[1] -= 5
        return new_state


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    import python_ta
    python_ta.check_all(config="a1_pyta.txt")

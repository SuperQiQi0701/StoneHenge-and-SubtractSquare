"""
Game module
classes Game, SubstractSquareGame, and Chopsticks.
"""
from typing import Any
from state_of_game import State, ChopsticsState, SubstractSquareState


class Game:
    """
    Represents a game.

    === Attributes ===
    is_p1_turn - whether it is p1's turn, if not, then it is p2's turn.
    current_state - the current state of the game.
    """
    is_p1_turn: bool
    current_state: State

    def __init__(self, is_p1_turn: bool) -> None:
        """
        Initialize a new game self, setting whether player 1 plays first
        to is_p1_turn. If is_p1_turn is True, then player 1 plays the game
        first; otherwise,player 2 plays first.

        :type self: Game
        :type is_p1_turn: bool
        :rtype: None

        >>> a = Game(True)
        >>> a.is_p1_turn
        True
        """
        self.is_p1_turn = is_p1_turn
        self.current_state = State(is_p1_turn)

    def __eq__(self, other: Any) -> bool:
        """
        Return whether Game self is equivalent to other.

        :type self: Game
        :type other: Any
        :rtype: bool

        >>> a = Game(True)
        >>> b = Game(True)
        >>> c = Game(False)
        >>> a == b
        True
        >>> a == c
        False
        """
        return type(self) == Game and type(other) == Game and \
               type(self) == type(other) \
               and self.is_p1_turn == other.is_p1_turn \
               and self.current_state == other.current_state

    def __str__(self) -> str:
        """
        Return a string representation of Game self.

        :rtype:str
        """
        raise NotImplementedError

    def is_over(self, state: State) -> bool:
        """
        Return if the game is over in state.

        :type state: State
        :rtype:bool

        >>> a = Game(True)
        >>> b = State(True)
        >>> a.is_over(b)
        True
        """
        return len(state.valid_moves) == 0

    def str_to_move(self, move_to_make: Any) -> Any:
        """
        Convert a move, move_to_make, into any format.

        :rtype: str
        """
        raise NotImplementedError

    def get_instructions(self) -> str:
        """
        Return a string of instructions of the rules of the game.

        :rtype:str
        """
        raise NotImplementedError

    def is_winner(self, player: str) -> bool:
        """

        Return whether player is the winner. If the game is not over yet,
        return False. When the game is over, if player is the winner, return
        True; otherwise, return False.
        :type self:Game
        :type player:str
        :rtype:bool

        >>> a = Game(True)
        >>> b = SubstractSquareState(True, 0)
        >>> a.state = b
        >>> a.is_winner('p1')
        True
        """
        if self.is_over(self.current_state):
            if self.current_state.is_p1_turn:
                return player == 'p2'
            return player == 'p1'
        return False


class SubstractSquareGame(Game):
    """
    A game called Substract Square.

    === Attributes ===
    is_p1_turn - whether it is p1's turn, if not, then it is p2's turn.
    current_state - the current state of the game Substract Square.
    """
    is_p1_turn: bool
    current_state: SubstractSquareState

    def __init__(self, is_p1_turn: bool) -> None:
        """
        Initialize a Substract State game self.
        :type is_p1_turn: bool
        :rtype: none
        """
        self.is_p1_turn = is_p1_turn
        number = int(input('Give me a number:'))
        self.current_state = SubstractSquareState(self.is_p1_turn, number)

    def __eq__(self, other: Any) -> bool:
        """
        Return whether SubstractSquareGame self is equivalent to other.
        :type other: Any
        :rtype: bool
        """
        return super().__eq__(other) and self.current_state.number \
               == other.current_state.number and \
               self.current_state == other.current_state

    def __str__(self) -> str:
        """
        Return a string representation of SubstractSquareGame self.
        :rtype: str

        """
        return "This game is Substract Square."

    def get_instructions(self) -> str:
        """
        Return a string of instructions of Substract Square game.
        :rtype:str
        """

        return "Players take turns subtracting square numbers from " \
               "the starting number. The winner is the person who " \
               "subtracts to 0."

    def is_over(self, state: SubstractSquareState) -> bool:
        """
        Return whether state is over. If state is over, return True; otherwise,
        return False.
        :type state: SubstractSquareState
        :rtype: bool
        """
        return state.game_over()

    def str_to_move(self, move_to_make: int) -> int:
        """
        Convert a move, move_to_make, into int format.
        Return an int form of move_to_make.

        :type move_to_make: int
        :rtype:int
        """
        return int(move_to_make)

"""
a module for StonehengeState.
"""

from typing import Any
import math
from game_state import GameState


LETTER = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
          'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


class StonehengeState(GameState):
    """
    The state of a game called StonehengeGame at a certain point in time.

    WIN - score if player is in a winning position
    LOSE - score if player is in a losing position
    DRAW - score if player is in a tied position
    p1_turn - whether it is p1's turn or not
    cells - a list of cells in current Stonehenge.
    row_layline: a list of all the row laylines in current Stonehenge state
    left_layline: a list of all the left laylines in current Stonehenge
    right_layline: a list of all the right laylines in current Stonehenge
    pre_marker: a list of all the markers from the previous state,
    if this is the original state, then pre_marker is None.
    marker: a list of markers of current state.
    """
    WIN: int = 1
    LOSE: int = -1
    DRAW: int = 0
    p1_turn: bool
    cells: list
    row_layline: list
    left_layline: list
    right_layline: list
    pre_marker: list
    marker: list

    def __init__(self, is_p1_turn: bool, side_length: int,
                 cells: list, pre_marker=None) -> None:
        """
        Initialize this stonehenge game state and set the current player based
        on is_p1_turn, side_length, cells, and premarker. The default pre_marker
        is None.

        :type is_p1_turn: bool
        :type side_length: int
        :type cells: list
        :type pre_marker: Any
        :rtype None

        >>> a = StonehengeState(True, 1, ['A', 'B', 'C'], None)
        >>> a.p1_turn
        True
        >>> a.side_length
        1
        >>> a.cells
        ['A', 'B', 'C']
        >>> a.pre_marker
        """

        super().__init__(is_p1_turn)
        self.side_length = side_length
        self.cells = cells
        self.row_layline = []
        self.left_layline = []
        self.right_layline = []
        self.load_hori_line()
        self.load_left_line()
        self.load_right_line()
        self.pre_marker = pre_marker
        self.marker = []
        self.get_marker()
        self.help_check_initial_marker()
        self.get_marker()

    def help_check_initial_marker(self) -> None:
        """
        A helper function for __init__ method. To check if the initial marker
        should change from '@' to claimed.
        """
        for i in range(len(self.row_layline)):
            if self.row_layline[i].count('1') >= \
                    math.ceil((len(self.row_layline[i]) - 1) / 2):
                if self.row_layline[i][0] == "@":
                    self.row_layline[i][0] = 1

        for i in range(len(self.left_layline)):
            if self.left_layline[i].count('1') >= \
                    math.ceil((len(self.left_layline[i]) - 1) / 2):
                if self.left_layline[i][0] == "@":
                    self.left_layline[i][0] = 1

        for i in range(len(self.right_layline)):
            if self.right_layline[i].count('1') >= \
                    math.ceil((len(self.right_layline[i]) - 1) / 2):
                if self.right_layline[i][0] == "@":
                    self.right_layline[i][0] = 1

        for i in range(len(self.row_layline)):
            if self.row_layline[i].count('2') >= \
                    math.ceil((len(self.row_layline[i]) - 1) / 2):
                if self.row_layline[i][0] == "@":
                    self.row_layline[i][0] = 2

        for i in range(len(self.left_layline)):
            if self.left_layline[i].count('2') >= \
                    math.ceil((len(self.left_layline[i]) - 1) / 2):
                if self.left_layline[i][0] == "@":
                    self.left_layline[i][0] = 2

        for i in range(len(self.right_layline)):
            if self.right_layline[i].count('2') >= \
                    math.ceil((len(self.right_layline[i]) - 1) / 2):
                if self.right_layline[i][0] == "@":
                    self.right_layline[i][0] = 2

    def load_hori_line(self) -> None:
        """
        Set up row laylines of current stonehenge state.

        :rtype: None

        >>> a = StonehengeState(True, 1, ['A', 'B', 'C'], None)
        >>> a.row_layline
        [['@', 'A', 'B'], ['@', 'C']]
        """
        number = 0
        for i in range(self.side_length + 1):
            self.row_layline.append(['@'])
        for i in range(self.side_length):
            for _ in range(i + 2):
                self.row_layline[i].append(self.cells[number])
                number += 1
        for i in range(self.side_length):
            self.row_layline[-1].append(self.cells[number])
            number += 1

    def helper_right_one(self) -> None:
        """
        A helper function for load_right_line when side_length is 1.

        """
        self.right_layline[0].append(self.cells[2])
        self.right_layline[0].append(self.cells[0])
        self.right_layline[1].append(self.cells[1])

    def helper_right_two(self) -> None:
        """
        A helper function for load_right_line when side_length is 2.
        """
        self.right_layline[0].append(self.cells[5])
        self.right_layline[0].append(self.cells[2])
        self.right_layline[1].append(self.cells[6])
        self.right_layline[1].append(self.cells[3])
        self.right_layline[1].append(self.cells[0])
        self.right_layline[2].append(self.cells[4])
        self.right_layline[2].append(self.cells[1])

    def helper_right_three(self) -> None:
        """
        A helper function for load_right_line when side_length is 3.
        """
        self.right_layline[0].append(self.cells[9])
        self.right_layline[0].append(self.cells[5])
        self.right_layline[1].append(self.cells[10])
        self.right_layline[1].append(self.cells[6])
        self.right_layline[1].append(self.cells[2])
        self.right_layline[2].append(self.cells[11])
        self.right_layline[2].append(self.cells[7])
        self.right_layline[2].append(self.cells[3])
        self.right_layline[2].append(self.cells[0])
        self.right_layline[3].append(self.cells[8])
        self.right_layline[3].append(self.cells[4])
        self.right_layline[3].append(self.cells[1])

    def helper_right_four(self) -> None:
        """
        A helper function for load_right_line when side_length is 4.
        """
        self.right_layline[0].append(self.cells[14])
        self.right_layline[0].append(self.cells[9])
        self.right_layline[1].append(self.cells[15])
        self.right_layline[1].append(self.cells[10])
        self.right_layline[1].append(self.cells[5])
        self.right_layline[2].append(self.cells[16])
        self.right_layline[2].append(self.cells[11])
        self.right_layline[2].append(self.cells[6])
        self.right_layline[2].append(self.cells[2])
        self.right_layline[3].append(self.cells[17])
        self.right_layline[3].append(self.cells[12])
        self.right_layline[3].append(self.cells[7])
        self.right_layline[3].append(self.cells[3])
        self.right_layline[3].append(self.cells[0])
        self.right_layline[4].append(self.cells[13])
        self.right_layline[4].append(self.cells[8])
        self.right_layline[4].append(self.cells[4])
        self.right_layline[4].append(self.cells[1])

    def load_right_line(self) -> None:
        """
        Set up right laylines of current stonehenge state.

        :rtype: None

        >>> a = StonehengeState(True, 1, ['A', 'B', 'C'], None)
        >>> a.right_layline
        [['@', 'C', 'A'], ['@', 'B']]
        """

        for _ in range(self.side_length + 1):
            self.right_layline.append(['@'])
        if self.side_length == 1:
            self.helper_right_one()
        if self.side_length == 2:
            self.helper_right_two()
        if self.side_length == 3:
            self.helper_right_three()
        if self.side_length == 4:
            self.helper_right_four()
        if self.side_length == 5:
            self.right_layline[0].append(self.cells[20])
            self.right_layline[0].append(self.cells[14])
            self.right_layline[1].append(self.cells[21])
            self.right_layline[1].append(self.cells[15])
            self.right_layline[1].append(self.cells[9])
            self.right_layline[2].append(self.cells[22])
            self.right_layline[2].append(self.cells[16])
            self.right_layline[2].append(self.cells[10])
            self.right_layline[2].append(self.cells[5])
            self.right_layline[3].append(self.cells[23])
            self.right_layline[3].append(self.cells[17])
            self.right_layline[3].append(self.cells[11])
            self.right_layline[3].append(self.cells[6])
            self.right_layline[3].append(self.cells[2])
            self.right_layline[4].append(self.cells[24])
            self.right_layline[4].append(self.cells[18])
            self.right_layline[4].append(self.cells[12])
            self.right_layline[4].append(self.cells[7])
            self.right_layline[4].append(self.cells[3])
            self.right_layline[4].append(self.cells[0])
            self.right_layline[5].append(self.cells[19])
            self.right_layline[5].append(self.cells[13])
            self.right_layline[5].append(self.cells[8])
            self.right_layline[5].append(self.cells[4])
            self.right_layline[5].append(self.cells[1])

    def helper_left_two(self) -> None:
        """
        A helper function for load_left_line when side_length is 2.
        """
        self.left_layline[0].append(self.cells[0])
        self.left_layline[0].append(self.cells[2])
        self.left_layline[1].append(self.cells[1])
        self.left_layline[1].append(self.cells[3])
        self.left_layline[1].append(self.cells[5])
        self.left_layline[2].append(self.cells[4])
        self.left_layline[2].append(self.cells[6])

    def helper_left_three(self) -> None:
        """
        A helper function for load_left_line when side_length is 3.
        """
        self.left_layline[0].append(self.cells[0])
        self.left_layline[0].append(self.cells[2])
        self.left_layline[0].append(self.cells[5])
        self.left_layline[1].append(self.cells[1])
        self.left_layline[1].append(self.cells[3])
        self.left_layline[1].append(self.cells[6])
        self.left_layline[1].append(self.cells[9])
        self.left_layline[2].append(self.cells[4])
        self.left_layline[2].append(self.cells[7])
        self.left_layline[2].append(self.cells[10])
        self.left_layline[3].append(self.cells[8])
        self.left_layline[3].append(self.cells[11])

    def helper_left_four(self) -> None:
        """
        A helper function for load_left_line when side_length is 4.
        """
        self.left_layline[0].append(self.cells[0])
        self.left_layline[0].append(self.cells[2])
        self.left_layline[0].append(self.cells[5])
        self.left_layline[0].append(self.cells[9])
        self.left_layline[1].append(self.cells[1])
        self.left_layline[1].append(self.cells[3])
        self.left_layline[1].append(self.cells[6])
        self.left_layline[1].append(self.cells[10])
        self.left_layline[1].append(self.cells[14])
        self.left_layline[2].append(self.cells[4])
        self.left_layline[2].append(self.cells[7])
        self.left_layline[2].append(self.cells[11])
        self.left_layline[2].append(self.cells[15])
        self.left_layline[3].append(self.cells[8])
        self.left_layline[3].append(self.cells[12])
        self.left_layline[3].append(self.cells[16])
        self.left_layline[4].append(self.cells[13])
        self.left_layline[4].append(self.cells[17])

    def load_left_line(self) -> None:
        """
        Set up row laylines of current stonehenge state.

        :rtype: None
        >>> a = StonehengeState(True, 1, ['A', 'B', 'C'], None)
        >>> a.left_layline
        [['@', 'A'], ['@', 'B', 'C']]
        """
        for _ in range(self.side_length + 1):
            self.left_layline.append(['@'])
        if self.side_length == 1:
            self.left_layline[0].append(self.cells[0])
            self.left_layline[1].append(self.cells[1])
            self.left_layline[1].append(self.cells[2])
        if self.side_length == 2:
            self.helper_left_two()
        if self.side_length == 3:
            self.helper_left_three()
        if self.side_length == 4:
            self.helper_left_four()
        if self.side_length == 5:
            self.left_layline[0].append(self.cells[0])
            self.left_layline[0].append(self.cells[2])
            self.left_layline[0].append(self.cells[5])
            self.left_layline[0].append(self.cells[9])
            self.left_layline[0].append(self.cells[14])
            self.left_layline[1].append(self.cells[1])
            self.left_layline[1].append(self.cells[3])
            self.left_layline[1].append(self.cells[6])
            self.left_layline[1].append(self.cells[10])
            self.left_layline[1].append(self.cells[15])
            self.left_layline[1].append(self.cells[20])
            self.left_layline[2].append(self.cells[4])
            self.left_layline[2].append(self.cells[7])
            self.left_layline[2].append(self.cells[11])
            self.left_layline[2].append(self.cells[16])
            self.left_layline[2].append(self.cells[21])
            self.left_layline[3].append(self.cells[8])
            self.left_layline[3].append(self.cells[12])
            self.left_layline[3].append(self.cells[17])
            self.left_layline[3].append(self.cells[22])
            self.left_layline[4].append(self.cells[13])
            self.left_layline[4].append(self.cells[18])
            self.left_layline[4].append(self.cells[23])
            self.left_layline[5].append(self.cells[19])
            self.left_layline[5].append(self.cells[24])

    def help_marker_one(self) -> None:
        """
        A helper function for get_marker when side_length is 1.
        """
        self.marker[0] = self.left_layline[0][0]
        self.marker[1] = self.left_layline[1][0]
        self.marker[2] = self.row_layline[0][0]
        self.marker[3] = self.row_layline[1][0]
        self.marker[4] = self.right_layline[1][0]
        self.marker[5] = self.right_layline[0][0]

    def help_marker_two(self) -> None:
        """
        A helper function for get_marker when side_length is 2.
        """
        self.marker[0] = self.left_layline[0][0]
        self.marker[1] = self.left_layline[1][0]
        self.marker[2] = self.row_layline[0][0]
        self.marker[3] = self.left_layline[2][0]
        self.marker[4] = self.row_layline[1][0]
        self.marker[5] = self.row_layline[2][0]
        self.marker[6] = self.right_layline[2][0]
        self.marker[7] = self.right_layline[0][0]
        self.marker[8] = self.right_layline[1][0]

    def help_marker_three(self) -> None:
        """
        A helper function for get_marker when side_length is 3.
        """
        self.marker[0] = self.left_layline[0][0]
        self.marker[1] = self.left_layline[1][0]
        self.marker[2] = self.row_layline[0][0]
        self.marker[3] = self.left_layline[2][0]
        self.marker[4] = self.row_layline[1][0]
        self.marker[5] = self.left_layline[3][0]
        self.marker[6] = self.row_layline[2][0]
        self.marker[7] = self.row_layline[3][0]
        self.marker[8] = self.right_layline[3][0]
        self.marker[9] = self.right_layline[0][0]
        self.marker[10] = self.right_layline[1][0]
        self.marker[11] = self.right_layline[2][0]

    def help_marker_four(self) -> None:
        """
        A helper function for get_marker when side_length is 3.
        """
        self.marker[0] = self.left_layline[0][0]
        self.marker[1] = self.left_layline[1][0]
        self.marker[2] = self.row_layline[0][0]
        self.marker[3] = self.left_layline[2][0]
        self.marker[4] = self.row_layline[1][0]
        self.marker[5] = self.left_layline[3][0]
        self.marker[6] = self.row_layline[2][0]
        self.marker[7] = self.left_layline[4][0]
        self.marker[8] = self.row_layline[3][0]
        self.marker[9] = self.row_layline[4][0]
        self.marker[10] = self.right_layline[4][0]
        self.marker[11] = self.right_layline[0][0]
        self.marker[12] = self.right_layline[1][0]
        self.marker[13] = self.right_layline[2][0]
        self.marker[14] = self.right_layline[3][0]

    def help_marker_five(self) -> None:
        """
        A helper function for get_marker when side_length is 3.
        """
        self.marker[0] = self.left_layline[0][0]
        self.marker[1] = self.left_layline[1][0]
        self.marker[2] = self.row_layline[0][0]
        self.marker[3] = self.left_layline[2][0]
        self.marker[4] = self.row_layline[1][0]
        self.marker[5] = self.left_layline[3][0]
        self.marker[6] = self.row_layline[2][0]
        self.marker[7] = self.left_layline[4][0]
        self.marker[8] = self.row_layline[3][0]
        self.marker[9] = self.left_layline[5][0]
        self.marker[10] = self.row_layline[4][0]
        self.marker[11] = self.row_layline[5][0]
        self.marker[12] = self.right_layline[5][0]
        self.marker[13] = self.right_layline[0][0]
        self.marker[14] = self.right_layline[1][0]
        self.marker[15] = self.right_layline[2][0]
        self.marker[16] = self.right_layline[3][0]
        self.marker[17] = self.right_layline[4][0]

    def get_marker(self) -> None:
        """
        Get all the markers from the current StonehengeState.

        :rtype None

        >>> a = StonehengeState(True, 1, ['A', 'B', 'C'], None)
        >>> a.get_marker()
        >>> a.marker
        ['@', '@', '@', '@', '@', '@']
        >>> new_state = a.make_move('A')
        >>> new_state.marker
        [1, '@', 1, '@', '@', 1]
        """

        self.marker = ['@'] * ((self.side_length + 1) * 3)
        if self.side_length == 1:
            self.help_marker_one()
        if self.side_length == 2:
            self.help_marker_two()
        if self.side_length == 3:
            self.help_marker_three()
        if self.side_length == 4:
            self.help_marker_four()
        if self.side_length == 5:
            self.help_marker_five()
        if self.pre_marker is not None:
            for i in range(len(self.marker)):
                if self.pre_marker[i] != '@':
                    self.marker[i] = self.pre_marker[i]

    def helper_str_one(self) -> str:
        """
        A helper function for __str__ method when side length is 1.
        """
        row1 = "      {}   {}\n"
        row2 = "     /   / \n"
        row3 = "{} - {} - {}  \n"
        row4 = "     \\ / \\ \n"
        row5 = "  {} - {}   {}\n"
        row6 = "       \\   \n"
        row7 = "        {}  "
        template1 = row1 + row2 + row3 + row4 + row5 + row6 + row7
        result = template1.format(self.marker[0],
                                  self.marker[1],
                                  self.marker[2],
                                  self.cells[0],
                                  self.cells[1], self.marker[3],
                                  self.cells[2],
                                  self.marker[4],
                                  self.marker[5])
        return result

    def helper_str_two(self) -> str:
        """
        A helper function for __str__ method when side length is 2.
        """
        row1 = "        {}   {}  \n"
        row2 = "       /   /   \n"
        row3 = "  {} - {} - {}   {}\n"
        row4 = "     / \\ / \\ / \n"
        row5 = "{} - {} - {} - {}  \n"
        row6 = "     \\ / \\ / \\ \n"
        row7 = "  {} - {} - {}   {}\n"
        row8 = "       \\   \\   \n"
        row9 = "        {}   {}  \n"
        template2 = row1 + row2 + row3 + row4 + row5 + row6 + row7 + row8 \
            + row9
        result = template2.format(self.marker[0],
                                  self.marker[1], self.marker[2],
                                  self.cells[0], self.cells[1],
                                  self.marker[3], self.marker[4],
                                  self.cells[2], self.cells[3],
                                  self.cells[4], self.marker[5],
                                  self.cells[5], self.cells[6],
                                  self.marker[6], self.marker[7],
                                  self.marker[8])
        return result

    def helper_str_three(self) -> str:
        """
        A helper function for __str__ method when side length is 3.
        """
        row1 = "          {}   {}    \n"
        row2 = "         /   /     \n"
        row3 = "    {} - {} - {}   {}  \n"
        row4 = "       / \\ / \\ /   \n"
        row5 = "  {} - {} - {} - {}   {}\n"
        row6 = "     / \\ / \\ / \\ / \n"
        row7 = "{} - {} - {} - {} - {}  \n"
        row8 = "     \\ / \\ / \\ / \\ \n"
        row9 = "  {} - {} - {} - {}   {}\n"
        row10 = "       \\   \\   \\   \n"
        row11 = "        {}   {}   {}  "
        template3 = row1 + row2 + row3 + row4 + row5 + row6 + row7 + row8 \
            + row9 + row10 + row11
        result = template3.format(self.marker[0],
                                  self.marker[1],
                                  self.marker[2],
                                  self.cells[0], self.cells[1],
                                  self.marker[3],
                                  self.marker[4], self.cells[2],
                                  self.cells[3], self.cells[4],
                                  self.marker[5],
                                  self.marker[6], self.cells[5],
                                  self.cells[6], self.cells[7],
                                  self.cells[8],
                                  self.marker[7], self.cells[9],
                                  self.cells[10],
                                  self.cells[11], self.marker[8],
                                  self.marker[9],
                                  self.marker[10],
                                  self.marker[11])
        return result

    def helper_str_four1(self) -> str:
        """
        A helper function for __str__ method when side length is 4.
        """
        row1 = "            {}   {}      \n"
        row2 = "           /  /        \n"
        row3 = "      {} - {} - {}   {}    \n"
        row4 = "         / \\ / \\ /     \n"
        row5 = "    {} - {} - {} - {}   {}  \n"
        row6 = "       / \\ / \\ / \\ /   \n"
        row7 = "  {} - {} - {} - {} - {}   {}\n"
        row8 = "     / \\ / \\ / \\ / \\ / \n"
        template4 = row1 + row2 + row3 + row4 + row5 + row6 + row7 + row8
        result = template4.format(self.marker[0],
                                  self.marker[1],
                                  self.marker[2],
                                  self.cells[0], self.cells[1],
                                  self.marker[3],
                                  self.marker[4], self.cells[2],
                                  self.cells[3],
                                  self.cells[4], self.marker[5],
                                  self.marker[6], self.cells[5],
                                  self.cells[6], self.cells[7],
                                  self.cells[8],
                                  self.marker[7])
        return result

    def helper_str_four2(self) -> str:
        """
        A helper function for __str__ method when side length is 4.
        """

        row9 = "{} - {} - {} - {} - {} - {}  \n"
        row10 = "     \\ / \\ / \\ / \\ / \\ \n"
        row11 = "  {} - {} - {} - {} - {}   {}\n"
        row12 = "       \\   \\   \\   \\   \n"
        row13 = "        {}   {}   {}   {}  \n"
        template = row9 + row10 + row11 + row12 + row13
        result = template.format(self.marker[8], self.cells[9],
                                 self.cells[10],
                                 self.cells[11], self.cells[12],
                                 self.cells[13], self.marker[9],
                                 self.cells[14],
                                 self.cells[15], self.cells[16],
                                 self.cells[17], self.marker[10],
                                 self.marker[11],
                                 self.marker[12],
                                 self.marker[13],
                                 self.marker[14])
        return result

    def helper_str_five1(self) -> str:
        """
        A helper function for __str__ method when side length is 4.
        """
        row1 = "              {}   {}        \n"
        row2 = "             /   /         \n"
        row3 = "        {} - {} - {}   {}      \n"
        row4 = "           / \\ / \\ /       \n"
        row5 = "      {} - {} - {} - {}   {}    \n"
        row6 = "         / \\ / \\ / \\ /     \n"
        row7 = "    {} - {} - {} - {} - {}   {}  \n"
        row8 = "       / \\ / \\ / \\ / \\ /   \n"
        row9 = "  {} - {} - {} - {} - {} - {}   {}\n"
        row10 = "     / \\ / \\ / \\ / \\ / \\ / \n"
        # row11 = "{} - {} - {} - {} - {} - {} - {}  \n"
        # row12 = "     \\ / \\ / \\ / \\ / \\ / \\ \n"
        # row13 = "  {} - {} - {} - {} - {} - {}   {}\n"
        # row14 = "       \\   \\   \\   \\   \\   \n"
        # row15 = "        {}   {}   {}   {}   {}  "
        template5 = row1 + row2 + row3 + row4 + row5 + row6 + row7 + row8 \
            + row9 + row10
        result = template5.format(self.marker[0],
                                  self.marker[1],
                                  self.marker[2],
                                  self.cells[0], self.cells[1],
                                  self.marker[3],
                                  self.marker[4], self.cells[2],
                                  self.cells[3], self.cells[4],
                                  self.marker[5],
                                  self.marker[6], self.cells[5],
                                  self.cells[6], self.cells[7],
                                  self.cells[8],
                                  self.marker[7],
                                  self.marker[8],
                                  self.cells[9],
                                  self.cells[10],
                                  self.cells[11], self.cells[12],
                                  self.cells[13], self.marker[9])
        return result

    def helper_str_five2(self) -> str:
        """
        A helper function for __str__ method when side length is 4.
        """
        row11 = "{} - {} - {} - {} - {} - {} - {}  \n"
        row12 = "     \\ / \\ / \\ / \\ / \\ / \\ \n"
        row13 = "  {} - {} - {} - {} - {} - {}   {}\n"
        row14 = "       \\   \\   \\   \\   \\   \n"
        row15 = "        {}   {}   {}   {}   {}  "
        template = row11 + row12 + row13 + row14 + row15
        result = template.format(self.marker[10], self.cells[14],
                                 self.cells[15], self.cells[16],
                                 self.cells[17], self.cells[18],
                                 self.cells[19], self.marker[11],
                                 self.cells[20], self.cells[21],
                                 self.cells[22], self.cells[23],
                                 self.cells[24], self.marker[12],
                                 self.marker[13],
                                 self.marker[14],
                                 self.marker[15],
                                 self.marker[16],
                                 self.marker[17])
        return result

    def __str__(self) -> str:
        """
        Return a string representation of the current state of the stonehenge
        game.

        :rtype str

        >>> state1 = StonehengeState(False, 1, ['A', 'B', 'C'])
        >>> state2 = StonehengeState(True, 1, ['A', 'B', 'C'])
        >>> state3 = StonehengeState(True, 1, [1, 'B', 'C'])
        >>> str(state1) == str(state2)
        True
        >>> str(state1) == str(state3)
        False
        """
        if self.side_length == 1:
            return self.helper_str_one()
        if self.side_length == 2:
            return self.helper_str_two()
        if self.side_length == 3:
            return self.helper_str_three()
        if self.side_length == 4:
            return self.helper_str_four1() + self.helper_str_four2()
        return self.helper_str_five1() + self.helper_str_five2()

    def get_possible_moves(self) -> list:
        """
        Return all possible moves that can be applied to this state.

        :rtype list

        >>> a = StonehengeState(True, 1, ['A', 'B', 'C'], None)
        >>> a.get_possible_moves()
        ['A', 'B', 'C']
        >>> new_state = a.make_move('A')
        >>> new_state.get_possible_moves()
        []
        """
        if not self.game_over():
            result = []
            for cell in self.cells:
                if not cell.isdigit():
                    result.append(cell)
            return result
        return []

    def game_over(self) -> bool:
        """
        Return True if the game is over in current state, otherwise,
        return False.

        :rtype: bool
        >>> a = StonehengeState(True, 1, ['A', 'B', 'C'], None)
        >>> a.game_over()
        False
        >>> new_state = a.make_move('A')
        >>> new_state.game_over()
        True
        """
        temp = self.marker[:]
        if temp.count(1) >= math.ceil((len(temp) / 2)) \
                or temp.count(2) >= math.ceil((len(temp) / 2)):
            return True
        return False

    def get_current_player_name(self) -> str:
        """
        Return 'p1' if the current player is Player 1, and 'p2' if the current
        player is Player 2.

        :rtype str

        >>> a = StonehengeState(True, 1, ['A', 'B', 'C'], None)
        >>> a.get_current_player_name()
        'p1'
        >>> new_state = a.make_move('A')
        >>> new_state.get_current_player_name()
        'p2'
        """
        if self.p1_turn:
            return 'p1'
        return 'p2'

    def check_marker(self) -> None:
        """
        A helper function for make_move function.
        To update markers, if a player captures at least half of the cells in
        a layline, then update the marker to 1 if it is p1, or 2 if it is p2.
        This is a helper function of make_move.

        :rtype: None
        """

        for i in range(len(self.row_layline)):
            if self.row_layline[i].count('1') >= \
                    math.ceil((len(self.row_layline[i]) - 1) / 2):
                if self.row_layline[i][0] == "@":
                    self.row_layline[i][0] = 1

        for i in range(len(self.left_layline)):
            if self.left_layline[i].count('1') >= \
                    math.ceil((len(self.left_layline[i]) - 1) / 2):
                if self.left_layline[i][0] == "@":
                    self.left_layline[i][0] = 1

        for i in range(len(self.right_layline)):
            if self.right_layline[i].count('1') >= \
                    math.ceil((len(self.right_layline[i]) - 1) / 2):
                if self.right_layline[i][0] == "@":
                    self.right_layline[i][0] = 1

        for i in range(len(self.row_layline)):
            if self.row_layline[i].count('2') >= \
                    math.ceil((len(self.row_layline[i]) - 1) / 2):
                if self.row_layline[i][0] == "@":
                    self.row_layline[i][0] = 2

        for i in range(len(self.left_layline)):
            if self.left_layline[i].count('2') >= \
                    math.ceil((len(self.left_layline[i]) - 1) / 2):
                if self.left_layline[i][0] == "@":
                    self.left_layline[i][0] = 2

        for i in range(len(self.right_layline)):
            if self.right_layline[i].count('2') >= \
                    math.ceil((len(self.right_layline[i]) - 1) / 2):
                if self.right_layline[i][0] == "@":
                    self.right_layline[i][0] = 2
        self.get_marker()

    def make_move(self, move: Any) -> 'StonehengeState':
        """
        Return the StonehengeState that results from applying move to this
        StonehengeState.

        :rtype StonehengeState
        >>> state1 = StonehengeState(True, 1, ['A', 'B', 'C'])
        >>> state3 = StonehengeState(False, 1, ['1', 'B', 'C'])
        >>> state2 = state1.make_move('A')
        >>> state3.__repr__() == state2.__repr__()
        True
        """
        cells = self.cells[:]
        # moves = self.get_possible_moves()
        cells[cells.index(move)] = '1' if self.p1_turn else '2'
        new_state = StonehengeState(not self.p1_turn, self.side_length, cells,
                                    self.marker)
        new_state.check_marker()
        return new_state

    def is_valid_move(self, move: Any) -> bool:
        """
        Return whether move is a valid move for this StonehengeState.

        :type move: Any
        :rtype bool
        >>> state1 = StonehengeState(True, 1, ['A', 'B', 'C'])
        >>> state1.is_valid_move('A')
        True
        >>> state1.is_valid_move('D')
        False
        """
        return move in self.get_possible_moves()

    def __repr__(self) -> Any:
        """
        Return a representation of this StonehengeState (which can be used for
        equality testing).

        :rtype: Any
        >>> state1 = StonehengeState(True, 1, ['A', 'B', 'C'])
        >>> state3 = StonehengeState(False, 1, ['1', 'B', 'C'])
        >>> state2 = state1.make_move('A')
        >>> state3.__repr__() == state2.__repr__()
        True
        """
        template = "Markers:{}. Side length: {}. Row Layline: {}." \
                   "Cells: {}. Left layline: {}. Right layline: {}. " \
                   "P1 turn: {}."

        return template.format(self.marker, self.side_length,
                               self.row_layline, self.cells, self.left_layline,
                               self.right_layline, self.p1_turn)

    def rough_outcome(self) -> int:
        """
        Return an estimate in interval [LOSE, WIN] of best outcome the current
        player can guarantee from StongehengeState self.

        >>> a = StonehengeState(False, 1, ['A', 'B', 'C'])
        >>> a.rough_outcome() == float(a.WIN)
        True
        >>> b = StonehengeState(True, 1, ['2', 'B', 'C'])
        >>> b.rough_outcome() == float(b.LOSE)
        True
        """
        movement = self.get_possible_moves()
        next_states = []
        for move in movement:
            new_state = self.make_move(move)
            if new_state.get_possible_moves() == []:
                return self.WIN
            next_states.append(new_state)
        results = []
        for state in next_states:
            score = []
            for move in state.get_possible_moves():
                next_state = state.make_move(move)
                if next_state.get_possible_moves() == []:
                    score.append(self.LOSE)
            results.append(score)
        lst = []
        for result in results:
            if -1 in result:
                lst.append(True)
        if all(lst):
            return self.LOSE
        return 0


if __name__ == "__main__":
    from python_ta import check_all
    check_all(config="a2_pyta.txt")
    import doctest
    doctest.testmod()

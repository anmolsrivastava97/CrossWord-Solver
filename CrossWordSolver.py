"""
Apple Assessment Code - CrossWord Solver
----------------------------------------

Author: Anmol Srivastava
Northeastern University

Created on:- 02/16/2022
"""


from termcolor import colored

class CrossWordSolver:

    def __init__(self, crossword_puzzle, dictionary):

        """
        This class is responsible for reading the puzzle and finding all the words of
        dictionary that are present in it.

        :param crossword_puzzle: a crossword_puzzle of M x N matrix
        :param dictionary: a list of words present in the dictionary
        """

        self.crossword_puzzle = crossword_puzzle
        self.word_dictionary = dictionary
        self.foundWords = []
        self.highlight_word = []

        # Dimensions of the puzzle
        self.ROW = len(self.crossword_puzzle)
        self.COL = len(self.crossword_puzzle[0])

        # 8 possible directions from any cell in the puzzle
        self.directions = [[-1, 0], [1, 0], [1, 1],
                    [1, -1], [-1, -1], [-1, 1],
                    [0, 1], [0, -1]]

    def findWord(self, x, y, word):

        """
        This function finds whether the given word is present in the puzzle or not
        after exploring all possible directions.

        :param x: x-coordinate of the cell
        :param y: y-corrdinate of the cell
        :param word: word that is to be searched in the grid
        :return: boolena status if the word has been found or not
        """

        # If the starting letter of word does not coincide with starting point
        if self.crossword_puzzle[x][y] != word[0]:
            return False

        for dx, dy in self.directions:

            # Starting co-ordinates for the word search
            newx = x + dx
            newy = y + dy

            matchFlag = True
            coord_list = [(x, y)]
            for i in range(1, len(word)):

                # Check for valid co-oridnates
                if newx < 0 or newx >= self.ROW or newy < 0 or newy >= self.COL or self.crossword_puzzle[newx][newy] != word[i]:
                    matchFlag = False
                    coord_list.clear()
                    break

                else:

                    coord_list.append((newx, newy))
                    # Proceed in the same direction
                    newx += dx
                    newy += dy

            # If matchFlag is still true then the word has been found in crrent direction
            if matchFlag:
                self.highlight_word.extend(coord_list)
                return matchFlag

        # Word is not found after exploring all 8 directions
        return False

    def wordsearch(self, word):

        """
        This function explores the cross word puzzle to find the words from list of word of dictionary
        and writes them to the result set.

        :param word: a word to be found
        """

        for row in range(self.ROW):
            for col in range(self.COL):
                if self.findWord(row, col, word):
                    result = (''.join(word), row, col)
                    self.foundWords.append(result)

    def solve(self):

        """
        This function runs all the step to find words and prints their location in the puzzle
        """

        for word in self.word_dictionary:

            if len(word) >= 3:
                self.wordsearch(word)

        self._printResult()

    def _printResult(self):

        """
        An helper function to print the result of word search in crossword on console
        """

        for row in range(self.ROW):
            for col in range(self.COL):

                letter = self.crossword_puzzle[row][col]

                if (row, col) in self.highlight_word:
                    print(colored("{}".format(letter), 'red'), end="\t")
                else:
                    print(colored("{}".format(letter), 'blue'), end="\t")

            print('\n')

        for result in self.foundWords:
            print("Word: {} found at location : ({}, {}) in puzzle".format(result[0], result[1], result[2]))


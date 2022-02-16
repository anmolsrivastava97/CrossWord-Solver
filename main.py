"""
Apple Assessment Code - CrossWord Solver
----------------------------------------

Author: Anmol Srivastava
Northeastern University

Created on:- 02/16/2022
"""

import argparse
from CrossWordSolver import CrossWordSolver


def readFile(filepath) -> list:
    """
    This function reads the content of the file from provided
    file path.

    :param filepath: path of the file
    :return: list of data
    """

    content = []

    with open(filepath, 'r') as file:
        for line in file:

            if line == "\n":
                raise Exception("Blank Line Encountered. Edit the file to make sure no empty line in between.")
            else:
                # Remove space if present
                line = line.replace(" ", "")
                content.append(list(line.upper().strip()))

    return content


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('puzzle_path', type=str, help="Path of the crossword puzzle file")
    parser.add_argument('word_dictionary_path', type=str, help='Path of the word dictionary file')

    args = parser.parse_args()

    try:
        crossword = readFile(args.puzzle_path)
        word_dictionary = readFile(args.word_dictionary_path)

    except Exception as err:
        print('Error while loading files: {}'.format(err))

    crosswordSolver = CrossWordSolver(crossword, word_dictionary)
    crosswordSolver.solve()

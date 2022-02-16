# Cross Word Solver
### Apple Coding Assignment

<p>
This program is responsible to find the word from given list 
in the cross word puzzle in all possible 8 directions. The structure
of the project is as follows:

1. **input:** A directory consists of various crossword puzzle `.txt` files 
with respective word dictionaries in `.txt` format which serves as an input
   to the driver class.
   

2. **CrossWordSolver.py:** It is a `python script` which consist of the class 
by the same name which responsible for setting up the crossword puzzle and search
   for words present in the word dictionary. The results are shown to the user as 
   a console output.
   

3. **main.py:** A python script which consist of the mail function which reads 
the puzzle and word dictionary file provided by the input and create an object
   of `CrossWordSolver` class to execute the word search.
</p>

<hr>

### ASSUMPTIONS

<p>
Following are the assumptions that are taken into account while developing
a project:

* Crossword puzzles and word dictionary would be read from the `.txt` files
fo simplicity of input operation of the program.
  

* Each row of the crossword puzzle should be present in the single row without any
space between the characters.
  

* Similarly, in word dictionary file only single words should be written in 
each line.
 
 
* The program can read crossword puzzle of various sizes.


* Words with `length < 3` would be ignored by the program as per the given
requirement.
</p>

<hr>

### INSTRUCTIONS TO RUN THE DRIVER CLASS

1. On the local machine clone the github repository using command:
`git clone https://github.com/anmolsrivastava97/CrossWord-Solver.git`


2.  `main.py` is the driver class which requires two input arguments i.e.
`-puzzle_path` and `-word_dictionary_path`
    

3. After choosing the appropriate crossword puzzle and word dictionary file
pass the command : `python3 main.py input/puzzle_1.txt input/words.txt`
 
  
4. In the above command path arguments can be changed based on local path
of crossword puzzle text and word test file.
   
<hr>

### CROSSWORD PUZZLE AND WORD DICTIONARY PAIRS

All the text files are available in `input` folder

* `bigPuzzle.txt` and `bigWords.txt`

* `exceptionPuzzle.txt` and `words_1.txt` (For testing exception while reading file)

* `puzzle_1.txt` and `words_1.txt`

* `puzzle_2.txt` and `words_2.txt`

* `puzzle_3.txt` and `words_3.txt`

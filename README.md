<<<<<<< HEAD
# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A: *Student should provide answer here*constraint propagation is used to solved naked twins problem in this way;firstly we identify the boxes that can take two values or more.Secondly,we check the boxes that have thesame values and when we see thesame values in different boxes the they are pairs of twin naked twin.After we use elimination method to eliminate any possibility of its peers or units having thesame value as the values contain by the naked twins.Here we use the fact that a naked twin means that those two spaces are the only spaces in a peer group that can contain those values

# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: *Student should provide answer here*A diagonal Sudoku has the additional constraint that the two diagonals of the puzzle must also contain all of the digits from 1 to 9.First we use a technique called Elimination which looks at the solve positions and determine the possible answers for unsolved positions.Then the only choice method is applied that is only one possible choice for a particular Sudoku square where there are eight squares allocated leaving only one remaining choice available; so the remaining number must go in that empty square.Thirdly the naked twin strategy is used, if two cells in a group contain an identical pair of candidates and only those two candidates, then no other cell in that group can contain those values,and the process of enforcing a constraint to reduce the search space to enforce more constraints to find a solution which continues untill we meet the solution.

### Install

This project requires **Python 3**.

We recommend students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project. 
Please try using the environment we provided in the Anaconda lesson of the Nanodegree.

##### Optional: Pygame

Optionally, you can also install pygame if you want to see your visualization. If you've followed our instructions for setting up our conda environment, you should be all set.

If not, please see how to download pygame [here](http://www.pygame.org/download.shtml).

### Code

* `solution.py` - You'll fill this in as part of your solution.
* `solution_test.py` - Do not modify this. You can test your solution by running `python solution_test.py`.
* `PySudoku.py` - Do not modify this. This is code for visualizing your solution.
* `visualize.py` - Do not modify this. This is code for visualizing your solution.

### Visualizing

To visualize your solution, please only assign values to the values_dict using the ```assign_values``` function provided in solution.py

### Submission
Before submitting your solution to a reviewer, you are required to submit your project to Udacity's Project Assistant, which will provide some initial feedback.  

The setup is simple.  If you have not installed the client tool already, then you may do so with the command `pip install udacity-pa`.  

To submit your code to the project assistant, run `udacity submit` from within the top-level directory of this project.  You will be prompted for a username and password.  If you login using google or facebook, visit [this link](https://project-assistant.udacity.com/auth_tokens/jwt_login for alternate login instructions.

This process will create a zipfile in your top-level directory named sudoku-<id>.zip.  This is the file that you should submit to the Udacity reviews system.

=======
# aindproject
>>>>>>> b6098a3f1f5b97aca0432b0dfcffca8ad6adc418

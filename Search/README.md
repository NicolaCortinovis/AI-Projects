### Readme for the search project

For this project all the questions in _project_outline.pdf_ were solved obtaining the following grades using the _autograder_:

<div align="center">

| Question | Grade |
|----------|-------|
|q1 | 3/3|
|q2 | 3/3|
|q3 | 3/3|
|q4 | 3/3|
|q5 | 3/3|
|q6 | 2/3|
|q7 | 3/4|
|q8 | 3/3|

</div>

- For Q1 I implemented the __DFS__ algorithm, the main quirk for this algorithm is that the frontier is saved using a _stack_
- For Q2 I implemented the __BFS__ algorithm, the main difference from __DFS__ is how the nodes are saved in the frontier, here I used a _queue_
- For Q3 I implemented the __UCS__ algorithm, here the frontier used is a _priority queue_
- For Q4 I implemented the __A*__ algorithm, here the frontier still is a _priority queue_, but we also take into account a heuristic function when choosing which node to expand
- For Q5 I implemented the `CornersProblem`, the key idea is that the game will end when the list `self.eaten_food` will all be set to `True` so when it will sum to 4
- For Q6 I implemented the `CornersProblemHeuristic`, the heuristic uses the max of the Manhattan Distance computed for all the corners where there still is food. While it will always find a solution (it is admissible) the number of states expanded may be too many 
- For Q7 I implemented the `FoodHeuristic` the heuristic uses the max of the Manhattan Distance computed for all the food still present in the world. Again it is consistent, but the number of states expanded may be too many 
- For Q8 I implemented `findPathToClosestDot`, I thought that a good candidate for always choosing the nearest food pellet could be __BFS__ 
# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    
    # We start by checking if the starting node is the solution (trivial case)
    
    if(problem.isGoalState(problem.getStartState()) == True):
        return [] # no actions needed
    
        
    # Data structures for the algorithm:
    # - A stack for saving the frontier, given by util.py
    # - A set for saving the expanded nodes, given by python
    
    DFS_frontier = util.Stack()
    expanded_set = set()
    
    # By default the starting state will be considered explored
    
    expanded_set.add(problem.getStartState())
    
    # Start by pushing the successors to the start state into the frontier
    
    for successors in problem.getSuccessors(problem.getStartState()):
        DFS_frontier.push((successors[0], successors[1] + " ", successors[2]))

    
    while(DFS_frontier.isEmpty() == False):
        # An element in the frontier is composed by its coordinates (x,y), the action needed to reach it from the predecessor (N,W,S,E) and the cost
        # From the frontier pop the coordinates and the action needed to reach the node from the predecessor
        state, direction, cost = DFS_frontier.pop()
        
        if(problem.isGoalState(state) == True):
            direction = list(direction.split(" "))
            direction.remove("")
            return direction
        
        if(state not in expanded_set):      # If we are visiting a node for the first time
            expanded_set.add(state)         # Add it to the set
            
            # We add the successors of the node currently being examined to the frontier
            for successors in problem.getSuccessors(state):
                DFS_frontier.push((successors[0], direction + " " + successors[1], cost + successors[2]))
            
    # If the while has terminated it means no goal exists therefore we return an empty list 
    return []

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    
    # We start by checking if the starting node is the solution (trivial case)
    
    if(problem.isGoalState(problem.getStartState()) == True):
        return [] # no actions needed
    
        
    # Data structures for the algorithm:
    # - A queue for saving the frontier, given by util.py
    # - A set for saving the expanded nodes, given by python
    
    BFS_frontier = util.Queue()
    expanded_set = set()
    
    # By default the starting state will be considered explored
    
    expanded_set.add(problem.getStartState())
    
    # Start by pushing the successors to the start state into the frontier
    
    for successors in problem.getSuccessors(problem.getStartState()):
        BFS_frontier.push((successors[0], successors[1] + " ", successors[2]))

    
    while(BFS_frontier.isEmpty() == False):
        
        state, direction, cost = BFS_frontier.pop()
        
        if(problem.isGoalState(state) == True):
            direction = list(direction.split(" "))
            direction.remove("")
            return direction
        
        if(state not in expanded_set):      # If we are visiting a node for the first time
            expanded_set.add(state)         # Add it to the set
            
            # We add the successors of the node currently being examined to the frontier
            for successors in problem.getSuccessors(state):
                BFS_frontier.push((successors[0], direction + " " + successors[1], cost + successors[2]))
            
    # If the while has terminated it means no goal exists therefore we return an empty list 
    return []
    

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # We start by checking if the starting node is the solution (trivial case)
    
    if(problem.isGoalState(problem.getStartState()) == True):
        return [] # no actions needed
    
        
    # Data structures for the algorithm:
    # - A priority queue for saving the frontier, given by util.py
    # - A set for saving the expanded nodes, given by python
    
    UCS_frontier = util.PriorityQueue()
    expanded_set = set()
    
    # By default the starting state will be considered explored
    
    expanded_set.add(problem.getStartState())
    
    # Start by pushing the successors to the start state into the frontier
    
    for successors in problem.getSuccessors(problem.getStartState()):
        UCS_frontier.push((successors[0], successors[1] + " ", successors[2]), successors[2])

    
    while(UCS_frontier.isEmpty() == False):
        
        state, direction, cost = UCS_frontier.pop()
        
        if(problem.isGoalState(state) == True):
            direction = list(direction.split(" "))
            direction.remove("")
            return direction
        
        if(state not in expanded_set):      # If we are visiting a node for the first time
            expanded_set.add(state)         # Add it to the set
            
            # We add the successors of the node currently being examined to the frontier
            for successors in problem.getSuccessors(state):
                UCS_frontier.push((successors[0], direction + " " + successors[1], cost + successors[2]), cost + successors[2])
            
    # If the while has terminated it means no goal exists therefore we return an empty list 
    return []
    

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def evaluation_func(real_cost, heuristic_func):
    return real_cost + heuristic_func

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    
    if(problem.isGoalState(problem.getStartState()) == True):
        return [] # no actions needed
    
        
    # Data structures for the algorithm:
    # - A priority queue with a function to detected the order, given by util.py
    # - A set for saving the expanded nodes, given by python
    
    # Given the frontier in A* the node to expand is given by f(n) = g(n) + h(n)
    # this will be the function for the ProprityQueueWithfunction
    
    
    
    aStar_frontier = util.PriorityQueue()
    expanded_set = set()
    
    # By default the starting state will be considered explored
    
    expanded_set.add(problem.getStartState())
    
    # Start by pushing the successors to the start state into the frontier
    
    for successors in problem.getSuccessors(problem.getStartState()):
        aStar_frontier.push((successors[0], successors[1] + " ", successors[2]), evaluation_func(successors[2], heuristic(successors[0], problem)))

    
    while(aStar_frontier.isEmpty() == False):
        
        state, direction, cost = aStar_frontier.pop()
        
        if(problem.isGoalState(state) == True):
            direction = list(direction.split(" "))
            direction.remove("")
            return direction
        
        if(state not in expanded_set):      # If we are visiting a node for the first time
            expanded_set.add(state)         # Add it to the set
            
            # We add the successors of the node currently being examined to the frontier
            for successors in problem.getSuccessors(state):
                aStar_frontier.push((successors[0], direction + " " + successors[1], cost + successors[2]), evaluation_func(cost + successors[2], heuristic(successors[0], problem)))
            
    # If the while has terminated it means no goal exists therefore we return an empty list 
    return []

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

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

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    stack=util.Stack()
    visited=[]
    startNode=(problem.getStartState(),[])        #Here we are pushing the start state
    stack.push(startNode)
    while not stack.isEmpty():
        popped=stack.pop()
        location=popped[0]
        path=popped[1]
        if location not in visited:               #In each node we see if it is visited,if it's not then we are getting the successors and push
            visited.append(location)              #its elements to the stack and we are building the path in depth-first logic and way
            if problem.isGoalState(location):
                return path
            successors=problem.getSuccessors(location)
            for suc in list(successors):
                if suc[0] not in visited:
                    stack.push((suc[0],path+[suc[1]]))
    return []
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    queue=util.Queue()
    visited=[]                                                       #We are doing the same thing like DFS with the difference that here we are using
    startNode=(problem.getStartState(),[])                           #queue instead of stack to build the path according to breadth-first logic
    queue.push(startNode)
    while not queue.isEmpty():
        popped=queue.pop()
        location=popped[0]
        path=popped[1]
        if location not in visited:
            visited.append(location)
            if problem.isGoalState(location):
                return path
            successors=problem.getSuccessors(location)
            for suc in list(successors):
                if suc[0] not in visited:
                    queue.push((suc[0],path + [suc[1]]))
    return []
    util.raiseNotDefined()

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # Initialize the priority queue
    priorityQueue = util.PriorityQueue()
    # Initialize the visited set
    visited = set()
    # Push the start state onto the priority queue
    priorityQueue.push((problem.getStartState(), []), 0)
    # While the priority queue is not empty
    while not priorityQueue.isEmpty():
        # Pop the current state and the path to it
        state, path = priorityQueue.pop()
        # If the state is the goal state, return the path
        if problem.isGoalState(state):
            return path
        # If the state has not been visited
        if state not in visited:
            # Add the state to the visited set
            visited.add(state)
            # For each successor of the state
            for successor, action, cost in problem.getSuccessors(state):
                # Push the successor and the path to it onto the priority queue
                priorityQueue.push((successor, path + [action]), problem.getCostOfActions(path + [action]))
    # Return an empty list if no path is found
    return []
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # Initialize the priority queue
    priorityQueue = util.PriorityQueue()
    # Initialize the visited set
    visited = set()
    # Push the start state onto the priority queue
    priorityQueue.push((problem.getStartState(), []), 0)
    # While the priority queue is not empty
    while not priorityQueue.isEmpty():
        # Pop the current state and the path to it
        state, path = priorityQueue.pop()
        # If the state is the goal state, return the path
        if problem.isGoalState(state):
            return path
        # If the state has not been visited
        if state not in visited:
            # Add the state to the visited set
            visited.add(state)
            # For each successor of the state
            for successor, action, cost in problem.getSuccessors(state):
                # Push the successor and the path to it onto the priority queue
                priorityQueue.push((successor, path + [action]), problem.getCostOfActions(path + [action]) + heuristic(successor, problem))
    # Return an empty list if no path is found
    return []
    
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
    
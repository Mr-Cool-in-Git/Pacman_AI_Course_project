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

    dfs_stack = util.Stack() # stack for DFS implementation
    start = problem.getStartState()
    current_state = start
    visited = set()
    actions_list = []
    while problem.isGoalState(current_state) is False:
        successors_list = problem.getSuccessors(current_state)
        while check_if_all_successors_been_visited(successors_list, visited):
            # this happens when we are going up in the tree because we did not find the solution anywhere below,
            # meaning these actions are not relevant for the solution, therefor deleted from actions list.
            # need to figure out how to delete all of the nodes that has got us there, not just the last step...
            actions_list.pop()
            if len(actions_list) is not 0:
                current_state = actions_list[-1][0]
            else:
                current_state = start
                break
            successors_list = problem.getSuccessors(current_state)
        visited.add(current_state)
        for item in successors_list:  # adding the successors to the stack
            if item[0] not in visited:
                dfs_stack.push(item)
        current_node = dfs_stack.pop()
        current_state = current_node[0]
        actions_list.append(current_node)
    actions_list = [item[1] for item in actions_list]
    return actions_list


def check_if_all_successors_been_visited(lst, set_1):
    for item in lst:
        if item not in set_1:
            return False
    return True

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    startState = problem.getStartState()
    queue = util.PriorityQueue()
    queue.push((startState, []), 0)
    alreadyVisitedStates = []

    while queue.isEmpty() is False:
        currItem = queue.pop()
        currState = currItem[0]
        currPath = currItem[1]
        if problem.isGoalState(currState) is True:
            return currPath

        if currState not in alreadyVisitedStates:
            alreadyVisitedStates.append(currState)

            # expand current state
            successors = problem.getSuccessors(currState)
            for successor in successors:
                if successor[0] not in alreadyVisitedStates:
                    newPath = currPath + [successor[1]]
                    queue.push((successor[0], newPath), problem.getCostOfActions(newPath))

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

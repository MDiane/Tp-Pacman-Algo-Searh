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
    #Start of my code 
    #Code Mamadi DIANE
    
    print "Stack ....:", util.Stack()
    print "Start......:", problem.getStartState()
    print "Is the start a goal?....:", problem.isGoalState(problem.getStartState())
    print "Start's successors....:", problem.getSuccessors(problem.getStartState())
   
    surround = util.Stack()
    visited = util.Stack()
    p1 = util.Stack()
    ac = util.Queue()

    surround.push([problem.getStartState()])

    while True:

        if problem.isGoalState(surround.list[-1][0]) == True:
            break
        
        successors = problem.getSuccessors(surround.list[-1][0])
        visited.push(surround.list[-1][0])
        p = surround.list[-1][0]
        surround.pop()
        for index in reversed(xrange(len(successors))):
            if successors[index][0] not in visited.list:
                surround.push([successors[index][0], p, successors[index][1]])
        p1.push(surround.list[-1])
    state = surround.list[-1][0]
    while state != problem.getStartState():
        for index in xrange(len(p1.list)):
            if state == p1.list[index][0]:
                 ac.push(p1.list[index][2])
                 state = p1.list[index][1]
    return ac.list
        
        
   



def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** MY CODE HERE:MAMADI DIANE ***"
    surround = util.Queue()
    visited = util.Stack()
    
    
    surround.push([problem.getStartState(), []])

    while True:
        
        if surround.isEmpty() == True:
            break

        state, actions = surround.pop()
        
        if problem.isGoalState(state):
            return actions

        successors = problem.getSuccessors(state)

        visited.push(state)

        for index in reversed(range(0, len(successors))):
            if successors[index][0] not in visited.list:
                surround.push([successors[index][0], actions + [successors[index][1]]])
                visited.push(successors[index][0])
    return []

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** MY CODE HERE:MAMADI DIANE ***"
    surround = util.PriorityQueue()
    visited = util.Stack()
    seen = util.Stack()
    
    
    surround.push([problem.getStartState(), []], 0)

    while True:
        
        if surround.isEmpty() == True:
            break

        priority, actions = surround.pop()
        
        if problem.isGoalState(priority):
            return actions
        
        successors = problem.getSuccessors(priority)

        costs = problem.getCostOfActions(actions)
        
        for index in reversed(range(0, len(successors))):

            stepcost = 0
            unseen = True
            
            for j in range(len(surround.heap)):
                if successors[index][0] == surround.heap[j][2][0]:
                    stepcost = surround.heap[j][0] - costs
                    unseen = False
            
            if successors[index][0] not in visited.list and (successors[index][2] < stepcost or unseen):
                surround.push([successors[index][0], actions + [successors[index][1]]], costs + successors[index][2])
                     
        visited.push(priority)
        
    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** MY CODE HERE: MAMADI DIANE ***"
    surround = util.PriorityQueue()
    visited = util.Stack()
    seen = util.Stack()
    
    
    surround.push([problem.getStartState(), []], 0)

    while True:
        
        if surround.isEmpty() == True:
            break

        priority, actions = surround.pop()
        
        if problem.isGoalState(priority):
            return actions
        
        successors = problem.getSuccessors(priority)

        costs = problem.getCostOfActions(actions)
        
        for index in reversed(range(0, len(successors))):

            stepcost = 0
            unseen = True
            
            for j in range(len(surround.heap)):
                if successors[index][0] == surround.heap[j][2][0]:
                    stepcost = surround.heap[j][0] - costs - heuristic(priority, problem)
                    unseen = False
            
            if successors[index][0] not in visited.list and (successors[index][2] < stepcost or unseen):
                surround.push([successors[index][0], actions + [successors[index][1]]], costs + successors[index][2] + heuristic(successors[index][0], problem))
                     
        visited.push(priority)
        
    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

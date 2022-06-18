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
    from util import Stack
    stackXY = Stack()
    visitedStates = []
    pathTraversed = []
    if problem.isGoalState(problem.getStartState()):
        return []
    stackXY.push((problem.getStartState(),[]))
    while(True):
        if stackXY.isEmpty():
            return []
        xy,pathTraversed = stackXY.pop()
        visitedStates.append(xy)
        if problem.isGoalState(xy):
            return pathTraversed
        succ = problem.getSuccessors(xy)
        if succ:
            for item in succ:
                if item[0] not in visitedStates:
                    newPath = pathTraversed + [item[1]]
                    stackXY.push((item[0],newPath))

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    queueXY = MyPriorityQueueWithFunction(problem,f)
    path = []
    visited = []
    if problem.isGoalState(problem.getStartState()):
        return []
    element = (problem.getStartState(),[])
    queueXY.push(element,heuristic)
    while(True):
        if queueXY.isEmpty():
            return []
        xy,path = queueXY.pop() # Take position and path
        if xy in visited:
            continue
        visited.append(xy)
        if problem.isGoalState(xy):
            return path
        succ = problem.getSuccessors(xy)
        if succ:
            for item in succ:
                if item[0] not in visited:
                    newPath = path + [item[1]]
                    element = (item[0],newPath)
                    queueXY.push(element,heuristic)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

# Solve a problem of Shortest path 
# given an undirected graph

from UndirectedGraph import UndirectedGraph


##################################
###########   Objects   ##########
##################################

class SNode:
    #represents a solved node
    def __init__(self, nodeName, shortest_path, distance):
        self.nodeName = nodeName
        self.shortest_path = shortest_path #list of ordered links which make the path
        self.distance = distance #minimal distance to the solved node
    def printSNode(self):
        print('Node name: ' + self.nodeName +
              ', shortest path: ' + str(self.shortest_path) + 
              ', distance: ' + str(self.distance))



##################################
##########   Functions ###########
##################################

def printSolvedNodes(listOfSolvedNodes):
    for i in listOfSolvedNodes:
        i.printSNode()

def isEndNodeReached(listOfSolvedNodes, endNodeName):
    for i in listOfSolvedNodes:
        if i.nodeName == endNodeName:
            return True  
    return False


#def findCandidates():



##################################
##########    Script    ##########
##################################

#create graph
g = UndirectedGraph('g1')
g.createGraph()

#Print graph option
proceed = input('Print graph? [y/n]: ')
if proceed == 'y':
    g.printGraph()

startNodeName = input('Enter the name of the start node: ')
endNodeName = input('Enter the name of the end node: ')

#Create a solved node object for the start node 
startNode = SNode(startNodeName, [], 0)

#Start a list of solved nodes
solved_nodes = [startNode]


while not isEndNodeReached(solved_nodes, endNodeName):
    exit()
    #find candidates:
    #each solved node provides its closest unsolved node


    #for each solved node and its candidate:
    #find the distance from origin to candidate by adding
    #solved node distance + candidate distance.
    #the candidate with the smallest distance to origin is the new solved node



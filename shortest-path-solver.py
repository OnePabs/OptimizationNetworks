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
    def printSNodePath(self):
        print(self.nodeName + ' shortest path: ')
        for link in self.shortest_path:
            print(link.name)
    def printSNode(self):
        print('Node name: ' + self.nodeName + ', distance: ' + str(self.distance))
        self.printSNodePath()



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


def findSNodeCandidate(snode, listOfSolvedNodes, graph):
    #find nodes linked to snode in graph
    snodeLinks = []
    for link in graph.links:
        if link.node1 == snode.nodeName or link.node2 == snode.nodeName:
            snodeLinks.append(link)

    #find linked nodes that are unsolved:
    unsolved_links = []
    for link in snodeLinks:
            #if link is not in listOfSolvedNodes then add it to  unsolved_linked_nodes
        isLinkedNodeSolved = False
        for solvedNode in listOfSolvedNodes:
            if link.node1 == solvedNode.nodeName and link.node1 != snode.nodeName:
                #link node 1 is a solved node
                isLinkedNodeSolved = True
            elif link.node2 == solvedNode.nodeName and link.node2 != snode.nodeName:
                isLinkedNodeSolved = True
        if isLinkedNodeSolved == False:
            #append link to unsolved_links
            unsolved_links.append(link)

    #choose link with smalles wieght
    if len(unsolved_links) > 0:
        min_weigth = unsolved_links[0].weight
        for link in unsolved_links:
            #find minimum wwight
            if link.weight < min_weigth:
                min_weigth = link.weight
        for link in unsolved_links:
            #return first link with minimum weight
            if link.weight == min_weigth:
                return link
    else:
        return '' #no unsolved candidates is represented as an empty string



##################################
##########    Script    ##########
##################################

#create graph
g = UndirectedGraph('g1')
g.createGraph()

#Print graph option
print()
proceed = input('Print graph? [y/n]: ')
if proceed == 'y':
    g.printGraph()

startNodeName = input('Enter the name of the start node: ')
endNodeName = input('Enter the name of the end node: ')

#Create a solved node object for the start node 
startNode = SNode(startNodeName, [], 0)

#Start a list of solved nodes
solved_nodes = [startNode]

iterantion_num = 0

print()
print("-------------------------------------")
print("Iterations")

while not isEndNodeReached(solved_nodes, endNodeName):

    #print iteration information
    print()
    print("Iteration: " + str(iterantion_num))
    print("Solved Nodes: ")
    for snode in solved_nodes:
        print(snode.nodeName)
    
    #find candidates and their distance to origin:
    #each solved node provides its closest unsolved node
    candidates = []
    for snode in solved_nodes:

        #print snode and its candidates
        print(snode.nodeName + " shortest unsolved node:")

        candidate_link = findSNodeCandidate(snode, solved_nodes, g)
        if candidate_link != '': #no unsolved candidates is represented as an empty string
            #find candidate name
            if candidate_link.node1 != snode.nodeName:
                candidate_name = candidate_link.node1
            else:
                candidate_name = candidate_link.node2
            #find candidate shortest path to origin
            candidate_path = snode.shortest_path + [candidate_link]
            #find candidate distance
            candidate_ds = snode.distance + int(candidate_link.weight)
            #create an snode for the candidate
            candidate = SNode(candidate_name, candidate_path, candidate_ds)
            #append candidate to candidates list
            candidates.append(candidate)

            #print candidate and its total distance
            print(candidate_name + " total distance: " + str(candidate_ds))


    #find candidate with smallest distance and add it to the solved nodes list
    min_distance = candidates[0].distance
    for candidate in candidates:
        #find smallest distance
        if candidate.distance < min_distance:
            min_distance = candidate.distance
    for candidate in candidates:
        #append first candidate with smallest distance
        if candidate.distance == min_distance:
            solved_nodes.append(candidate)
            print("-> Minimum distance candidate: " + candidate.nodeName)
            candidate.printSNodePath()


    #increase iteration number
    iterantion_num += 1

print("---------------------------------")
print()

#print smallest path to endNode
for snode in solved_nodes:
    if snode.nodeName == endNodeName:
        print("end node has been reached: ")
        snode.printSNodePath()

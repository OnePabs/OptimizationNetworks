#UndirectedGraph object
class Undirectedlink:
    def __init__(self, node1, node2, weight):
        self.name = node1 + '-' + node2
        self.node1 = node1
        self.node2 = node2
        self.weight = weight

    def is_node_in_link(self, node):
        if self.node1 == node or self.node2 == node:
            return True
        return False

    def equal(self, link2):
        if self.is_node_in_link(link2.node1) and self.is_node_in_link(link2.node2):
            return True
        return False

    def get_other_node(self, node):
        #returns the other node in the link. 
        #if node is not in the link, returns ''
        if self.node1 == node:
            return self.node2
        elif self.node2 == node:
            return self.node1
        else:
            return ''

class UndirectedGraph:
    def __init__(self, graphName):
        self.graphName = graphName

    nodes = [] #Node names as strings
    links = [] #list of Undirectedlink objects

    def askForNodes(self):
        #print('askForNodes...')
        while True:
            nodeName = input('Enter node name (enter exit if no more nodes): ')
            if nodeName != 'exit':
                self.nodes.append(nodeName)
            else:
                return

    def readNodesFromFileLines(self, fileLines):
        for line in fileLines:
            items = line.split()
            if len(items) > 0:
                if items[0] == "n":
                    #line is a node. use format "n nodename" to get information
                    self.nodes.append(items[1])

    
    def askForLinks(self):
        #print('Links...')
        while True:
            linkNode1 = input('link first node name (type exit if no more links): ')
            if linkNode1 != 'exit':
                linkNode2 = input('link second node: ')
                linkWeight = input('link weight: ')
                print()
                link = Undirectedlink(linkNode1, linkNode2, linkWeight)
                self.links.append(link)
            else:
                return

    def readLinksFromFileLines(self, fileLines):
        for line in fileLines:
            items = line.split()
            if len(items) > 0:
                if items[0] == "l":
                    # format "l node1Name node2Name linkWeight"
                    linkNode1 = items[1]
                    linkNode2 = items[2]
                    linkWeight = items[3]
                    link = Undirectedlink(linkNode1, linkNode2, linkWeight)
                    self.links.append(link)



    def createGraph(self):
        #print('creating graph...')
        use_file = input("Would you like to use a file? [y/n]: ")
        if use_file == "y":
            filename = input("Enter filepath: ")
            f = open(filename,"r")
            lines = f.readlines()
            self.readNodesFromFileLines(lines)
            self.readLinksFromFileLines(lines)
        else:
            self.askForNodes()
            print()
            print('Links...')
            self.askForLinks()
        
        print_file = input("Would you like to print " + self.graphName + " [y/n]?: ")
        if print_file == "y":
            self.printGraph()



    def printGraph(self):
        print('Graph Nodes: ')
        for i in self.nodes:
            print(i)

        print()

        print('Graph links: ')
        for i in self.links:
            print('link ' + i.name)
            print('link weight: ' + i.weight)
            print()




#test
#print('testing...')
#g1 = UndirectedGraph('g1')
#g1.createGraph()
#g1.printGraph()
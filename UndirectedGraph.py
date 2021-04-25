#UndirectedGraph object
class Undirectedlink:
    def __init__(self, node1, node2, weight):
        self.name = node1 + '-' + node2
        self.node1 = node1
        self.node2 = node2
        self.weight = weight

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
        
        print_file = input("Would you like to print " + self.graphName + " [y/n]?")
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
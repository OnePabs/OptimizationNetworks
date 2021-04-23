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
        print('askForNodes...')
        while True:
            nodeName = input('Enter node name (enter exit if no more nodes): ')
            if nodeName != 'exit':
                self.nodes.append(nodeName)
            else:
                return
    
    def askForLinks(self):
        print('askForLinks...')
        while True:
            linkNode1 = input('Enter link first node (enter exit if no more links): ')
            if linkNode1 != 'exit':
                linkNode2 = input('Enter link second node: ')
                linkWeight = input('Enter link weight: ')
                print()
                link = Undirectedlink(linkNode1, linkNode2, linkWeight)
                self.links.append(link)
            else:
                return


    def createGraph(self):
        print('creating graph...')
        self.askForNodes()
        print()
        self.askForLinks()

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
print('testing...')
g1 = UndirectedGraph('g1')
g1.createGraph()
g1.printGraph()
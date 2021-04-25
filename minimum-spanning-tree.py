#given a graph, finds the minimum spanning tree
from UndirectedGraph import UndirectedGraph
from UndirectedGraph import Undirectedlink


def findClosestUnconnectedNodeLink(connected_nodes, connected_links, undirected_graph):

    # find the closest unconnected node to the tree
    closest_links = []
    for cn in connected_nodes:
        #find the closest unconnected node to cn
        
        min_link = Undirectedlink('','',-1)

        #Find all the current node's links to unconnected nodes
        unconnected_links_to_cn = []
        for link in undirected_graph.links:
            
            #if link has cn as a node
            if link.is_node_in_link(cn):

                #find if other node in link is an unconnected node
                is_other_node_unconnected = True
                for cnj in connected_nodes:
                    if cnj == link.get_other_node(cn):
                        #other node in link is already connected
                        is_other_node_unconnected = False
                
                #if the second node in the link is unconnected
                if is_other_node_unconnected:

                    #find out if this link is the unconnected link to cn with the miinimal weight
                    if min_link.weight == -1 or link.weight < min_link.weight:
                        min_link = link

        #if cn is linked to at least one unconnected node
        if min_link.weight != -1:
            closest_links.append(min_link)

    
    #choode from closest unconnected links
    min_link = Undirectedlink('','',-1)
    for cl in closest_links:
        if min_link.weight == -1 or cl.weight < min_link.weight:
            min_link = cl
    
    return min_link


g = UndirectedGraph("Spanning Tree Initial")
g.createGraph()

start_node = input("start node: ")
n = len(g.nodes)

links_in_tree = []
connected_nodes = [start_node]

print()
print("Starting Algorithm at node: " + start_node)
#Build spanning trees until n-1 links have been placed. a minimum spanning tree will have n-1 links, where n is the number of nodes in the graph
while(len(links_in_tree) < n-1):
    #find link to the closest node
    closest_unconnected_node_link = findClosestUnconnectedNodeLink(connected_nodes, links_in_tree, g)
    links_in_tree.append(closest_unconnected_node_link)

    #print new link
    print("Next Closest Link: " + closest_unconnected_node_link.name)

    #update list of connected nodes
    is_link_node1_in_connected_nodes = False
    is_link_node2_in_connected_nodes = False
    for connectedNode in connected_nodes:
        if connectedNode == closest_unconnected_node_link.node1:
            is_link_node1_in_connected_nodes = True
        if connectedNode == closest_unconnected_node_link.node2:
            is_link_node2_in_connected_nodes = True
    if not is_link_node1_in_connected_nodes:
        connected_nodes.append(closest_unconnected_node_link.node1)
    if not is_link_node2_in_connected_nodes:
        connected_nodes.append(closest_unconnected_node_link.node2)

print()
print()
print("Final list of links: ")
for link in links_in_tree:
    print(link.name)

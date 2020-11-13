
from random import randrange

# define a function that receives number of nodes, n, numbers of edges,
def reciever():

    number_nodes = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    
# m, and a list of edges, snowy_edges

    snowy_edges = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]

# set a variable, currentPosition, equal to the starting node. Doesn't matter if you randomly pick it or a choose a starting node

    currentPosition = randrange(len(number_nodes))
    now = (number_nodes[currentPosition])
    print(now)

# set a variable, totalMinutes, equal to 0. This is where we will store the time

    # totalMinutes = 0

# set a variable, cleared_edges, equal to an empty list. This is where we will store the edges we cleared

    cleared_edges = []

# create a while loop that runs until the list, snowy_edges, is empty

    while snowy_edges:
        edges = snowy_edges.pop()
        print(edges)
    for cleared_edge in cleared_edges:
        print(cleared_edge)
    
    # create a list, current_snowy_edges, from the snowy edges that contains the current node
    Current_snowy_edges = []
    # if current_snowy_edges contains at least 1 edge
    if Current_snowy_edges == 1 < m:
        random(m)
        currentPosition = m[0],
        totalMinutes = __+ 1
        # randomly select one of the edges
        random()
        # set the currentPosition equal to the node on the other end of the edge
        # remove the edge from snowy_edges and at it to cleared_edges
        # add 1 to totalMinutes
    # else
    else:
        for
        connect = []
        random(connect)
        currentPosition =
        totalMinutes = __+ 1
        # generate a list of all the edges connected to the node
        # randomly select one of the edges
        # set the currentPosition equal to the node on the other end of edge
        # add 1 to totalMinutes


        
if __name__ == '__main__':
    reciever()
   
    

# define a function that receives number of nodes, n, numbers of edges,
# m, and a list of edges, snowy_edges

# set a variable, currentPosition, equal to the starting node. Doesn't matter if you randomly pick it or a choose a starting node
# set a variable, totalMinutes, equal to 0. This is where we will store the time
# set a variable, cleared_edges, equal to an empty list. This is where we will store the edges we cleared

# create a while loop that runs until the list, snowy_edges, is empty
    
    # create a list, current_snowy_edges, from the snowy edges that contains the current node

    # if current_snowy_edges contains at least 1 edge
        # randomly select one of the edges
        # set the currentPosition equal to the node on the other end of the edge
        # remove the edge from snowy_edges and at it to cleared_edges
        # add 1 to totalMinutes
    # else
        # generate a list of all the edges connected to the node
        # randomly select one of the edges
        # set the currentPosition equal to the node on the other end of edge
        # add 1 to totalMinutes
        

   
    

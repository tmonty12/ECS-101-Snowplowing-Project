import random

sample_edges = [(0,1),(1,2),(1,3),(1,4),(2,3),(3,4),(2,5),(3,5),(4,5)]

def find_other_node(edge, current_node):
    if(edge[0] == current_node):
        return edge[1]
    else:
        return edge[0]

def get_snowy_edges(node, snowy_edges):
    current_snowy_edges = []
    for edge in snowy_edges:
        if(edge[0] == node or edge[1] == node):
            current_snowy_edges.append(edge)
    return current_snowy_edges

def snowplow_program(num_nodes,num_edges,snowy_edges):
    current_position = random.randint(0,num_nodes-1)
    total_minutes = 0
    back_tracks = 0
    cleared_edges = []

    while(len(snowy_edges) > 0):
        current_snowy_edges = get_snowy_edges(current_position,snowy_edges)

        num_cse = len(current_snowy_edges)

        if(num_cse > 0):
            index = random.randint(0,num_cse-1)
            selected_edge = current_snowy_edges[index]
            cleared_edges.append(selected_edge)
            current_position = find_other_node(selected_edge, current_position)
            se_idx = snowy_edges.index(selected_edge)
            snowy_edges = snowy_edges[:se_idx] + snowy_edges[se_idx+1:]
            total_minutes += 1
        else:
            connected_edges = []

            for edge in cleared_edges:
                if(edge[0] == current_position or edge[1] == current_position):
                    connected_edges.append(edge)

            index = random.randint(0,len(connected_edges)-1)
            selected_edge = connected_edges[index]
            current_position = find_other_node(selected_edge, current_position)

            total_minutes +=1
            back_tracks +=1
    
    return (total_minutes, back_tracks)

if(__name__ == "__main__"):
    print(snowplow_program(6,9,sample_edges))

   

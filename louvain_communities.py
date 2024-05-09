import sys
import json
import networkx as nx
import matplotlib.pyplot as plt
from networkx import community  # Import community detection module

def create_graph_from_json(json_data):
    graph = nx.Graph()
    for key, value in json_data.items():
        node_name = value['id']
        adjacent_to = value['adjacentTo']
        graph.add_node(node_name)
        for adjacent_node in adjacent_to:
            graph.add_edge(node_name, adjacent_node)
    return graph

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py input_file.json")
        sys.exit(1)

    input_file = sys.argv[1]

    with open(input_file, 'r') as f:
        json_data = json.load(f)

    graph = create_graph_from_json(json_data)
    
    # Detect communities using the Louvain algorithm
    partition = community.louvain_communities(graph, seed=123)
    
    # Draw the graph with nodes colored by their communities
    pos = nx.spring_layout(graph)  # Position nodes using spring layout
    nx.draw(graph, pos, node_color=list(partition.values()), with_labels=True, font_weight='bold', cmap=plt.cm.get_cmap('viridis'))
    plt.show()

if __name__ == "__main__":
    main()

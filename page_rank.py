import sys
import json
import networkx as nx
import matplotlib.pyplot as plt

def create_graph_from_json(json_data):
    graph = nx.DiGraph()
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
    pr = nx.pagerank(graph, alpha=0.9)
    sorted_pr = sorted(pr.items(), key=lambda item: item[1], reverse=True)
    for node, rank in sorted_pr:
        print(f"Node: {node}, PageRank: {rank}")
    # nx.draw(graph, with_labels=True, font_weight='bold')
    # plt.show()

if __name__ == "__main__":
    main()
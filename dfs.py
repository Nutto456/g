import networkx as nx
import matplotlib.pyplot as plt

# Create the graph
G = nx.Graph()

# Define node colors based on the type of location
color_map = {
    "Nimman Day": "red",
    "Chiang Mai Zoo": "blue",
    "Wat Phra That Doi Suthep": "red",
    "Wat Phra That Doi Kham": "red",
    "Botanical Garden Queen Sirikit": "green",
    "Moncham": "green",
    "Grand Canyon Mae Jo": "green",
    "Mae Kampong": "green",
    "Tha Phae Gate": "purple",
    "Chiang Mai Municipality": "purple",
    "Warorot Market": "purple",
    "Wat Umong": "red",
    "Wat Phra Singh Woramahaviharn": "red",
    "Doi Luang Chiang Dao": "blue",
    "Maesa Elephant Camp": "blue",
}

# Add nodes and edges to the graph
G.add_nodes_from(color_map.keys())
G.add_weighted_edges_from([
    ("Chiang Mai Municipality", "Nimman Day", 3.1),
    ("Nimman Day", "Chiang Mai Zoo", 3.6),
    ("Chiang Mai Zoo", "Wat Phra That Doi Suthep", 11.6),
    ("Wat Phra That Doi Suthep", "Wat Phra That Doi Kham", 8.5),
    ("Wat Phra That Doi Kham", "Botanical Garden Queen Sirikit", 12.1),
    ("Botanical Garden Queen Sirikit", "Moncham", 11.6),
    ("Moncham", "Grand Canyon Mae Jo", 18.7),
    ("Grand Canyon Mae Jo", "Mae Kampong", 28.8),
    ("Mae Kampong", "Tha Phae Gate", 36.9),
    ("Tha Phae Gate", "Chiang Mai Municipality", 2.1),
    ("Chiang Mai Municipality", "Warorot Market", 0.9),
    ("Warorot Market", "Wat Umong", 4.7),
    ("Wat Umong", "Wat Phra Singh Woramahaviharn", 5.2),
    ("Wat Phra Singh Woramahaviharn", "Chiang Mai Zoo", 3.1),
    ("Chiang Mai Zoo", "Doi Luang Chiang Dao", 62.6),
    ("Doi Luang Chiang Dao", "Maesa Elephant Camp", 51.5),
    ("Maesa Elephant Camp", "Botanical Garden Queen Sirikit", 17.8),
])

# Define the starting node for DFS
start_node = "Chiang Mai Municipality"

# Perform DFS starting from the start node
dfs_tree = nx.dfs_tree(G, start_node)

# Draw the graph using a spring layout
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_color=[color_map[node] for node in G.nodes()])
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(dfs_tree, pos, edge_color='r', width=2)

# Show the plot
plt.show()

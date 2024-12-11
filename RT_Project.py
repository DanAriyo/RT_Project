# Distance Vector Routing Protocol Simulation
from collections import defaultdict
from Node import Node

def simulate_distance_vector(nodes):
    converged = False
    iteration = 1
    while not converged:
        print(f"Iteration {iteration}:")
        converged = True
        for node in nodes:
            for neighbor_name in node.neighbors:
                neighbor = next(n for n in nodes if n.name == neighbor_name)
                if node.update_routing_table(neighbor):
                    converged = False
        for node in nodes:
            print(node)
        print("-" * 70)
        iteration += 1

# Create nodes
node_A = Node('A')
node_B = Node('B')
node_C = Node('C')
node_D = Node('D')
node_E = Node('E')
node_F = Node('F')

# Define neighbors and costs
node_A.add_neighbor(node_B, 1)
node_A.add_neighbor(node_F, 3)

node_B.add_neighbor(node_A, 1)
node_B.add_neighbor(node_C, 3)
node_B.add_neighbor(node_E, 5)
node_B.add_neighbor(node_F, 1)

node_C.add_neighbor(node_D, 2)
node_C.add_neighbor(node_B, 3)

node_D.add_neighbor(node_E, 1)
node_D.add_neighbor(node_F, 6)
node_D.add_neighbor(node_C, 2)

node_E.add_neighbor(node_D, 1)
node_E.add_neighbor(node_F, 2)
node_E.add_neighbor(node_B, 5)

node_F.add_neighbor(node_D, 6)
node_F.add_neighbor(node_E, 2)
node_F.add_neighbor(node_B, 1)
node_F.add_neighbor(node_A, 3)



# Simulate routing
nodes = [node_A, node_B, node_C, node_D,node_E,node_F]
simulate_distance_vector(nodes)
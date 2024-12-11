from collections import defaultdict
class Node:
    def __init__(self, name):
        self.name = name
        self.routing_table = {name: 0}  # Initialize distance to itself as 0
        self.neighbors = {}  # Directly connected neighbors {neighbor: cost}

    def add_neighbor(self, neighbor, cost):
        self.neighbors[neighbor.name] = cost
        self.routing_table[neighbor.name] = cost

    def update_routing_table(self, neighbor):
        updated = False
        for dest, neighbor_cost in neighbor.routing_table.items():
            if dest == self.name:
                continue
            new_cost = self.neighbors[neighbor.name] + neighbor_cost
            if dest not in self.routing_table or new_cost < self.routing_table[dest]:
                self.routing_table[dest] = new_cost
                updated = True
        return updated

    def __str__(self):
        return f"Node {self.name}, Routing Table: {self.routing_table}"

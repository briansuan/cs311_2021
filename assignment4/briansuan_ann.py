import random
import string

class Node:

    def __init__(self):
        self.children = []
        
        for i in range(3):
            self.my_node = ''.join([random.choice(string.ascii_letters)])

        self.children_connection_weights = []

    def make_children(self, current_layer, nodes_per_layer_map):
        if current_layer == len(nodes_per_layer_map):
            return

        for i in range(nodes_per_layer_map[current_layer]):
            self.children.append(Node())
    
        first_born = self.children[0]

        first_born.make_children(current_layer + 1, nodes_per_layer_map)

        for i in range(1, len(self.children)):
            self.children[i].children = first_born.children[:]


    def adjust_child_weights(self):
        if len(self.children) == 0:
            return
        self.children_connection_weights = []

        for i in range(len(self.children)):
            self.children_connection_weights.append(random.uniform(0,1))

            self.children[i].adjust_child_weights()
    
    def OUTPUT_children(self, layer):
        indent = '    ' * layer

        if len(self.children) == 0:
            print(f"{indent}{self.my_node}")

        print(f"{indent}{self.my_node} is connected to ")
        for i in range(len(self.children)):
            self.children[i].OUTPUT_children(layer + 1)

            if i < len(self.children_connection_weights):
                print(f"{indent}with weight {self.children_connection_weights[i]} ")



nodes = []

master_node = Node()

my_first_node = Node()

NODE_COUNT_PER_LAYER = [4,3,2]

my_first_node.make_children(1, NODE_COUNT_PER_LAYER)

master_node.children.append(my_first_node)

for i in range(1, len(NODE_COUNT_PER_LAYER)):
    new_node = Node()

    new_node.children = my_first_node.children[:]

    master_node.children.append(new_node)

master_node.OUTPUT_children(0)
print("!! Set Weights !!")
master_node.adjust_child_weights()

master_node.OUTPUT_children(0)










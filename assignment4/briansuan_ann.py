import random
import string


class Node:
    
    # Constructor: creates an array for children and weights of the connection for each children
    # each node is represented as a sequence of  3 random ascii characters 
    def __init__(self):
        self.children = []
        
        self.my_node = ''.join([random.choice(string.ascii_letters) for i in range (3)])

        self.children_connection_weights = []
    
    # A recursive function to make children, break out of the recursion if the current layer is at the last layer, 
    # the last layer will be when the current_layer is the same as the length of the nodes_per_layer_map array 
    def make_children(self, current_layer, nodes_per_layer_map):
        if current_layer == len(nodes_per_layer_map):
            return

        for i in range(nodes_per_layer_map[current_layer]):
            self.children.append(Node())
    
        first_born = self.children[0]

        first_born.make_children(current_layer + 1, nodes_per_layer_map)

        for i in range(1, len(self.children)):
            self.children[i].children = first_born.children[:]

    # A function to adjust the weights of each child
    def adjust_child_weights(self):

        if len(self.children) == 0:
            return

        self.children_connection_weights = []

        for i in range(len(self.children)):
            self.children_connection_weights.append(random.uniform(0,1))

            self.children[i].adjust_child_weights()
    
    # Print out the nodes 
    def OUTPUT_children(self, layer):
        indent = '    ' * layer

        if len(self.children) == 0:
            print(f"{indent}{self.my_node}")

        print(f"{indent}{self.my_node} is connected to ")

        for i in range(len(self.children)):
            self.children[i].OUTPUT_children(layer + 1)

            if i < len(self.children_connection_weights):
                print(f"{indent}with weight {self.children_connection_weights[i]} ")


# create an array of nodes
nodes = []

# create an instance of the Node() class called master_node()
master_node = Node()

# Create another instance of the node class for my_first_node
my_first_node = Node()

# The first layer will contain 4 nodes, second will contain 3 nodes, and last layer will contain 2 nodes
NODE_COUNT_PER_LAYER = [4,3,2]

# Make the children for the first node
my_first_node.make_children(1, NODE_COUNT_PER_LAYER)

# The master node is the first node
master_node.children.append(my_first_node)

# Create the rest of the nodes
for i in range(1, len(NODE_COUNT_PER_LAYER)):
    new_node = Node()

    new_node.children = my_first_node.children[:]

    master_node.children.append(new_node)


master_node.OUTPUT_children(0)


print("!! Set Weights !!")

master_node.adjust_child_weights()

master_node.OUTPUT_children(0)










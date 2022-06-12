class Node:
    def __init__(self,value):
        self.value = value
    

    
class Edge:
    def __init__(self, node, weight = 0):
        self.node = node
        self.weight = weight


    
class Graph:
    def __init__(self):
        self.adjacency_list = {}
        


    def add_node(self, value): 
        node = Node(value)
        self.adjacency_list[node] = []
        return node



    def add_edge(self, node_1, node_2, weight = 0):

        if not (node_1 in self.adjacency_list.keys()) or not (node_2 in self.adjacency_list.keys()):
            raise KeyError("Error, node is not in graph!")
        else:
            edge = Edge(node_2, weight = weight)
            self.adjacency_list[node_1].append(edge)



    def get_node(self):
        output=[]
        for node in self.adjacency_list.keys():
            output.append(node.value)
        return output


    def get_neighbors(self, node):
        if not (node in self.adjacency_list.keys()):
            raise KeyError("The node is not in the graph")
        else:
            output=[]
            for edge in self.adjacency_list[node]:
                output.append([edge.node.value,edge.weight])
            return output
       


    def size(self):
        return len(self.adjacency_list)



    def __str__(self):
        output = ''
        for node in self.adjacency_list.keys():
            output += f"{node.value} -> "

            for edge in self.adjacency_list[node]:
                output += f' {edge.node.value} ->'
            
            output += ' Null\n'
        return output
class HashTable:
    def __init__(self, size = 1024):
        self.size = size
        self.map = [None]*size


    def hash(self, key):
        ascii_sum = 0
        ascii_char = ord(key)
        ascii_sum += ascii_char
        
        hashed = (ascii_sum * 19) % self.size
        return hashed


    def set(self, key, value):
        hashed = self.hash(key)  

        if self.map[hashed] is None:
            self.map[hashed] = [[key, value]]
        
        else: 
            self.map[hashed].append([key, value])



    def get(self, key):
        hashed = self.hash(key)
        return self.map[hashed]




    def contains(self, key):
        hashed = self.hash(key)
        if self.map[hashed]:
            return True
        else:
            return False



class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None



def trees_intersection(t1, t2):
    if t1.root is None or t2.root is None:
        raise Exception ("Tree is empty")

    hashtable = HashTable()
    result = []


    def _traverse(node):
        if hashtable.contains(str(node.value)):
            result.append(node.value)
        else:
            hashtable.set(str(node.value), True)

        if node.left:
            _traverse(node.left)
        # if node.right:
        #     _traverse(node.right)


    _traverse(t1.root)
    _traverse(t2.root)

    return result




if __name__ == '__main__':
    h = HashTable()

    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(9)
    node6 = Node(8)


    t1 = Tree()
    t1.root = node1
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.right = node6



    t2 = Tree()
    t2.root = node2
    node2.left = node1
    node2.right = node3
    node3.left = node5
    node3.right = node1

  
    # print(trees_intersection(t1,t2))
    
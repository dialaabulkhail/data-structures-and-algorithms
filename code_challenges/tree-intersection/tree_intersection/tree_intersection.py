class HashTable:
    def __init__(self, size = 1024):
        self.size = size
        self.map = [None]*size


    def hash(self, key):
        ascii_sum = 0
        for char in key:
            ascii_char = ord(char)
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
        return self.map[hashed][0][1]




    def contains(self, key):
        hashed = self.hash(key)
        if self.map[hashed][1][0] == key:
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


    def _traverse(root):
        if hashtable.contains(str(root.value)) is True:
            result.append(root.value)
        else:
            hashtable.set(str(root.value), True)

        if root.left:
            _traverse(root.left)
        if root.right:
            _traverse(root.right)


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
    t1.root = node5
    node1.left = node3
    node1.right = node2
    node2.left = node1
    node2.right = node4


    t2 = Tree()
    t2.root = node5
    node1.left = node3
    node1.right = node6
    node2.left = node5
  
    print(trees_intersection(t1,t2))
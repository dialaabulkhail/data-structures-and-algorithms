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



class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None



def trees_intersection(t1,t2):
    node1 = t1.root.value
    node2 = t2.root.value
    lst = []
    h = HashTable()

    def _t1(node1,node2):
        h.set(str(node1), node1)
        lst.append(h.get(str(node2)))

        

        return lst

    _t1(node1, node2)
    return lst

    # return h.get(str(node1))

    # def _traverse1(node1):
    #     h.set(str(node1.value), node1)

    #     if node1.left:
    #         _traverse1(node1.left)

    #     if node1.right:
    #         _traverse1(node1.rigth)

        # return

    # def _traverse2(node2):
    #     try:
    #         lst.append(hash.get(str(node2.value)))
    #     except:
    #         return None

    #     if node2.left:
    #         _traverse2(node2.left)

    #     if node2.right:
    #         _traverse2(node2.right)

    #     return

    # _traverse1(node1)
    # _traverse2(node2)
    # return lst



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
    node1.left = node1
    node1.right = node6
    node2.left = node5
  
    print(trees_intersection(t1,t2))
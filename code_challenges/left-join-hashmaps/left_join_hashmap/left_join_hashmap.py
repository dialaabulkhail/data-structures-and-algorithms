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
        return self.map[hashed]




    def contains(self, key):
        hashed = self.hash(key)
        if self.map[hashed]:
            return True
        else:
            return False


def left_join(ht1, ht2):
    
    result = []

    for pair in ht1.map:
        if pair:
            if ht2.get(pair[0][0]):
                result.append([pair[0][0],pair[0][1],ht2.get(pair[0][0])[0][1]])
                

            else:
                result.append([pair[0][0],pair[0][1],None])

    return result



if __name__ == '__main__':
    ht1 = HashTable()
    ht2 = HashTable()

    ht1.set('diligent', 'employed')
    ht1.set('fond', 'enamored')
    ht1.set('guide', 'usher')
    ht1.set('outfit', 'garb')
    ht1.set('wrath', 'anger')

    ht2.set('diligent', 'idle')
    ht2.set('fond', 'averse')
    ht2.set('guide', 'follow')
    ht2.set('flow', 'jam')
    ht2.set('wrath', 'delight')

    print(left_join(ht1, ht2))
    
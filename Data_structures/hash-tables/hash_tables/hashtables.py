

class HashTable:
    def __init__(self, size = 1024):
        self.size = size
        self.map = [None]*size

    
    """
    This method takes a stirng key as an argument and returns its hashed value according to ASCII 
    """
    def hash(self, key):
        ascii_sum = 0
        for char in key:
            ascii_char = ord(char)
            ascii_sum += ascii_char
        
        hashed = (ascii_sum * 19) % self.size
        return hashed


    """
    This method sets key-value pairs at the hashed bucket if it was empty or adds them as collisions if it wasn't. 
    ###it also updates the key value if it was passed with another value. 
    """
    def set(self, key, value):
        hashed = self.hash(key)  # return hashed value which is the index of the key

        if self.map[hashed] is None:
            self.map[hashed] = [[key, value]]
        
        else: 
            # if key in self.map:
            #     self.map[hashed][1][0] == value
            self.map[hashed].append([key, value])

            
            
    """
    This method takes a key and returns the value accociated with that key in the map
    """
    def get(self, key):
        hashed = self.hash(key)
        return self.map[hashed]



    def contains(self, key):
        if self.map[self.hash(key)]:
            return True
        
        else:
            return False



    def keys(self):
        lst = []
        for i in self.map:
            if i:
                [lst.append(index[0]) for index in i]
        return lst



if __name__ == "__main__":

    h = HashTable()
    # print(h.hash("true"))

    h.set("hello", "world")
    h.set("hello", "mom")

    x = h.set("welcome", "home")
    h.set("holle", "user")
    h.set("friday", "night")
    
    # for item in enumerate(h.map):
    #    print(item)

    # print(h.get("hello"))
    # print(h.get("friday"))
    # print(h.get("hoell"))

    # print(h.contains("hello"))
    # print(h.contains("hi"))

    print(h.keys())

    # print(h.contains('hello'))




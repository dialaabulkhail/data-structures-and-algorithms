"""
Node class is for creating a node with a value and a pointer to the next node
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

"""
Queue class is a regular class for creating a queue
"""
class Queue:
    def __init__(self):
        self.rear = None
        self.front = None


    def enqueue1(self, value):
        node = Node(value)
        if not self.front:
            self.front = node
            self.rear = node

        self.rear.next = node
        self.rear = node


    def dequeue1(self):
        if not self.front:
            raise Exception("Empty Queue")
        
        temp = self.front
        self.front = self.front.next
        temp.next = None

        return temp.value


    def peek(self):
        if not self.front:
            raise Exception("Empty Queue")
        
        return self.front.value



"""
AnimalsShelter class is used for enqueuing and dequeuing dogs and cats form a shelter 
methods of AnimalShelter class:
enqueue(): takes one arguement "animal" either cat or dog, if cat it adds it in an object of Queue --> cat_queue
                                                           if dog it adds it in an object of Queue --> dog_queue

dequeue(): takes one argument "pref" either a cat or a dog, if cat it removes it from cat_queue and returns the removed value
                                                            if dog it removes it form dog_queue and returns the removed value
"""
class AnimalShelter:
    def __init__(self):
        self.cat_queue = Queue()
        self.dog_queue = Queue()




    def enqueue(self, animal):
        try:
            if animal == "cat":
                self.cat_queue.enqueue1(animal)
            elif animal == "dog":
                self.dog_queue.enqueue1(animal)

        except:
            raise Exception("Animal is not cat nor dog")


 
    def dequeue(self, pref):
        try:
            self.pref = pref
            if self.pref == "cat":
                self.cat_queue.dequeue1()
            elif self.pref == "dog":
                self.dog_queue.dequeue1()

        except:
            return None






if __name__ == "__main__":
    q = AnimalShelter()

    q.enqueue("cat")
    q.enqueue("cat")
    print(q.cat_queue.front.value)

    q.enqueue("dog")
    q.dequeue("dog")
    print(q.dog_queue.dequeue1())

    q.dequeue("dog")
    print(q.dog_queue.dequeue1())

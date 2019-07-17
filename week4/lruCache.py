class Node:
    # doubly linked nodes
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = {} # initialize dictionary that will map key value to node
        self.head = Node(0,0) # 0 valued node as head of list
        self.end = Node(0,0) # set up 0 valued node as end of list
        self.end.previous = self.head # link end node to head node
        self.head.next = self.end # link head node to end node

    def get(self, key: int) -> int:
        # if node already exists in map
        if key in self.dict:
            # grab node
            node = self.dict[key]
            # if map has only one element, don't delete and add back, instead
            # return value of node
            if len(self.dict) == 1:
                return node.value
            # otherwise delete node and add to bottom of list, doing this ensures
            # that we know its being used
            else:
                self.deleteNode(node)
                self.addNode(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        # if node key already exists in map delete the Node
        if key in self.dict:
            node = self.dict[key]
            self.delNode(node)
        # create node for key, value
        node = Node(key, value)
        # add (link) created node to list
        self.addNode(node)
        # map key to node in dictionary
        self.dict[key] = node

        # if the length of map is larger then cache capacity then delete second
        # node in linked list, as it is the least used, most used are the
        # bottom of the list
        if len(self.dict) > self.capacity:
            node = self.head.next
            self.deleteNode(node)
            del self.dict[node.key]

    def deleteNode(self, node):
        # finding the previous and next nodes linked current node
        previ, nex = node.prev, node.next
        # link previous node current node's next node
        # link next node to current nodes's previous node
        # this un-links current node and thus deletes it
        previ.next, nex.prev = nex,previ

    # link new node to node at the end of list
    def addNode(self, node):
        # previous node linked to end node
        previous = self.end.previous

        # link previous node to input node
        previous.next = node
        # link input node to end node
        node.next = self.end
        # link end node to input node
        self.end.previous = node
        # link input node to previous node
        node.prev = previous

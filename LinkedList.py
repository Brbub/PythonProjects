class Node:
    """
    An object for storing a single node in a linked list

    Attributes:
        data: Data stored in node
        next_node: Reference to next node in linked list
    """

    def __init__(self, data, next_node = None):
        self.data = data
        self.next_node = next_node
    def __repr__(self):
        return "<Node data: %s>" % self.data

class SinglyLinkedList:
    """
    Linear data structure that stores values in nodes. The list maintains a reference to the first node, also called head. Each node points to the next node in the list

    Attributes:
        head: The head node of the list
    """

    def __init__(self):
        self.head = None
        # Maintaining a count attribute allows for len() to be implemented in
        # constant time
        self.__count = 0

    def is_empty(self):
        """
        Determines if the linked list is empty
        Takes O(1) time
        """

        return self.head is None

    def __len__(self):
        """
        Returns the length of the linked list
        Takesn O(1) time
        """

        return self.__count
    def add(self, data):
        """
        Adds a new node containing data to the head of the list at constant time {O(1)} 
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
#Linked List implementation in python

class Node:
    #creating a node
    def __init__(self, item):
        self.item = item
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None

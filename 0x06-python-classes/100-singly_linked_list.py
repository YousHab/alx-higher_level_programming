#!/usr/bin/python3

class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value
    
    @property
    def next_node(self):
        return self.__next_node
    
    @next_node.setter
    def next_node(self, value):
        if value == None or not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    def __init__(self):
        self.__head = None
    
    def __str__(self):
        
        string1 = ""
        current_node = self.__head
        while current_node and isinstance(current_node, Node):
            string1 += str(current_node.data) + '\n'
            current_node = current_node.next_node
        return string1

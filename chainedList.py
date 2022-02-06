# coding: utf-8

__author__ = 'Aimen CHERIF'

from node import Node

class ChainedList():
    """
    Chained list Object
    Parameters
    ----------
    nodes : list
        list that we want to transfert in a chained list of Node object
    """
    def __init__(self):
        self.first_node = None

    def __iter__(self):     #make the list iterable
        node = self.first_node
        while node is not None:
            yield node
            node = node.link

    def insert_node_beginning(self, new_node):
        """
        insert a new node at the beginning of the chained list.
        Parameters
        ----------
        new_node : node to insert at the beginning of the list
        """
        new_node = Node(new_node)
        new_node.link = self.first_node
        self.first_node = new_node


    def insert_node_end(self, new_node):
        """
        insert a new node at the end
        Parameters
        ----------
        new_node : node to insert at the end of the list
        """

        newnode = Node(new_node)
        if self.first_node is None :
            self.first_node = newnode
            return
        else:
            temp = self.first_node
            while temp.link is not None :
                temp = temp.link
            temp.link = newnode


    def insert_before(self, data, new_node):
        """
        insert a new node before the node with the value ==data
        Parameters
        ----------
        data : searched data
        new_node : node to insert
        """
        value = Node(new_node)
        value.link = self.first_node

        node = self.first_node
        if node is None:
            print ('No nodes to insert before!')
        else:
            found = False
                # search nodes
            while node:
                if node.link is None:
                    break
                if node.link.data == data:
                    found = True
                    value.link = node.link
                    node.link = value
                    break
                else:
                    node = node.link
            if found is not True:
                print ('Your target node of {} was not found in the list!'.format(data))


    def insert_after(self, data, new_node):
        """
        insert a new node after the node with the value ==data
        Parameters
        ----------
        data : searched data
        new_node : node to insert
        """
        node = self.first_node
        while node is not None:
            if node.data == data:
                break
            node = node.link
        if node is None:
            print ('Your target node of {} was not found in the list!'.format(data))
        else:
            new_node = Node(new_node)
            new_node.link = node.link
            node.link = new_node


    def sorted_insert(self, new_node):

        """
        insert a new node in a sorted increasing way as it'll be inserted
        just before the FIRST existing node that has a bigger value
        Parameters
        ----------
        data : searched data
        new_node : node to insert
        """
        current = None
        new_node=Node(new_node)
        if (self.first_node is None or (self.first_node.data >= new_node.data)):

            new_node.link = self.first_node
            self.first_node = new_node

        else:

            # Locate the node before the point of insertion
            current = self.first_node
            while (current.link is not None and current.link.data < new_node.data):

                current = current.link
            new_node.link = current.link
            current.link = new_node

        return self.first_node


    def delete_node(self,data):
        """
        delete the first occurrence of value in linked list
        Parameters
        ----------
        data : searched data to delete
        """
        temp = self.first_node
        if temp is not None:
            if temp.data == data:
                self.first_node = temp.link
                temp = None
                return

        while temp is not None:
            if temp.data == data:
                break
            prev = temp
            temp = temp.link

        if temp is None:
            print("Warning: no target node found at a certain position/empty list!")
            return

        prev.link = temp.link


    def print_list(self) :
        """
        prints chained list
        """
        temp = self.first_node
        temp=Node(temp)
        if temp.data is None :
            print("Chained list is empty!")
        else :
            print (temp.data)

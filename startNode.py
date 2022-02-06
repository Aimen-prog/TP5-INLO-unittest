# coding: utf-8

__author__ = 'Aimen CHERIF'

from random import randrange
from chainedList import ChainedList


if __name__=='__main__':

    ######Create a freely first chained list to test different library features#####

	# initialize an empty list
    chained_list = ChainedList()

	# Insert 6 in the first chained list
    chained_list.insert_node_beginning(6)

	# Insert 7 at the end : 6 -> 7
    chained_list.insert_node_end(7)

	# Insert 1 and the chained list becomes 6->7->1
    chained_list.insert_node_end(1)

	# Insert 9 in the beginning and the list becomes 9-> 6-> 7-> 1
    chained_list.insert_node_beginning(9)

	# Insert 50 before 7. The list becomes 9-> 6-> 50-> 7-> 1
    chained_list.insert_before(7,50)

    # Insert 50 after 7. The list becomes 9-> 6-> 50-> 7-> 50-> 1
    chained_list.insert_after(7, 50)

    #Insert 18 in a sorted way. The list will become 9-> 6-> 18 ->50-> 7-> 50-> 1

    chained_list.sorted_insert(18)

    # delete node 1. The list becomes 9-> 6-> 18 -> 50-> 7-> 50

    chained_list.delete_node(1)

    # delete multiple values if possible (50 here). The list becomes 9-> 6-> 18-> 7
    #Warnings consider that some nodes aren't concerned

    for i in iter(chained_list) :
        chained_list.delete_node(50)

    #print this first chained list to check:
    print("\nThis is an example of a manually-made chained list proposed by us: ")
    chained_list.print_list()

    ######Create a second chained list sorted from random numbers#####

	# initialize another empty list
    second_chained_list = ChainedList()


    for i in range(5) : #chained list of length 5
        second_chained_list.sorted_insert(randrange(1000)) #random values between 0 and 1000
    print("\nThis is a sorted chained list with random values: ")
    second_chained_list.print_list()

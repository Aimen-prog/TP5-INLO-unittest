#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Aimen CHERIF'


import unittest
from chainedList import ChainedList


class TestChainedList(unittest.TestCase):
    """ This class test functions of ChainedList class """

    def setUp(self):
        """ goes for initialization of two empty linked lists"""
        self.test_list = ChainedList()
        self.copy_of_test_list = ChainedList()

    def test_chainedList_is_empty(self):
        """ tests if a new linked list is empty """
        self.assertIsNone(self.test_list.first_node)

    def test_new_node(self):
        """tests if a linked list on which we've just stacked an element is
        not empty"""

        self.test_list.insert_node_beginning(8)
        self.assertIsNotNone(self.test_list.first_node)

    def test_add_delete_node_equals(self):
        """ tests if a linked list stacked then unstacked with elements is unchanged"""
        self.copy_of_test_list.insert_node_beginning(7)
        self.copy_of_test_list.delete_node(7)
        self.assertEqual(self.copy_of_test_list, self.test_list)
        #to compare the two objects i've added __eq__ method in ChainedList class


    def test_added_top_equals_top(self):
        """ Tests if the top of a linked list on which we have just stacked an element
        e is e """
        self.test_list.insert_node_beginning(1)
        self.test_list.insert_after(1,2)
        self.test_list.insert_node_end(3) #1,2,3
        self.assertEqual(self.test_list.first_node.data, 1)


if __name__ == '__main__':
    unittest.main()

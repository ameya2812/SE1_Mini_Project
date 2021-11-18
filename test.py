import unittest
from main import *


def prepare_list():
    result = LinkedList()
    result.add_in_tail(Node(42))
    result.add_in_tail(Node(33))
    result.add_in_tail(Node(11))
    result.add_in_tail(Node(22))
    result.add_in_tail(Node(15))
    result.add_in_tail(Node(42))
    result.add_in_tail(Node(10))
    result.add_in_tail(Node(32))
    result.add_in_tail(Node(42))
    result.add_in_tail(Node(60))
    result.add_in_tail(Node(70))
    result.add_in_tail(Node(66))
    return result


class LinkedListTests(unittest.TestCase):
    def test_add_first_element(self):
        test_list = LinkedList()
        node = Node(75)
        test_list.add_in_tail(node)
        print("\nTESTING: add_in_tail() function")
        print("Testing that the node added is first element of linked list(empty before)")
        try:
            self.assertEqual(test_list.len(), 2)
            print("\t--->Length condition followed.")
        except:
            print("\tERROR: Length not matched")

        try:
            self.assertEqual(test_list.head, node)
            print("\t--->Proper head pointer.")
        except:
            print("\tERROR: Bad head pointer")

        try:
            self.assertEqual(test_list.tail, node)
            print("\t--->Proper tail pointer.")
        except:
            print("\tERROR: Bad tail pointer")

    def test_delete_node_present_once(self):
        print("\n\nTESTING: delete function for the value present in list only once")
        test_list = prepare_list()
        print("Current linked list:", end=" ")
        test_list.print_all_nodes()
        test_list.delete(11)
        try:
            self.assertEqual(test_list.to_values_list(), [42, 33, 22, 15, 42, 10, 32, 42, 60, 70, 66])
            print("\n\t--->Element 11 deleted successfully.")
        except:
            print("\n\tERROR: Element not deleted, delete function failed.")

    def test_delete_node_present_multiple(self):
        print("\n\nTESTING: delete function for the value present in list for multiple times")
        test_list = prepare_list()
        print("Current linked list:", end=" ")
        test_list.print_all_nodes()
        test_list.delete(42)
        try:
            self.assertEqual(test_list.to_values_list(), [33, 11, 22, 15, 42, 10, 32, 42, 60, 70, 66])
            print("\n\t--->Element 42 deleted successfully (first occurence).")
        except:
            print("\n\tERROR: Element not deleted, delete function failed.")

    def test_delete_node_which_not_present(self):
        print("\n\nTESTING: delete function for the value NOT present in list")
        test_list = prepare_list()
        print("Current linked list:", end=" ")
        test_list.print_all_nodes()
        test_list.delete(42)
        self.assertEqual(test_list.to_values_list(), [42, 33, 11, 22, 15, 42, 10, 32, 42, 60, 70, 66])
        # print("\n\t--->Value 99 is not the element of list")
        # try:
        #     self.assertEqual(test_list.to_values_list(), [42, 33, 11, 22, 15, 42, 10, 32, 42, 60, 70, 66])
        #     print("\n\t--->Value 99 is not the element of list")
        # except:
        #     print("\n\tERROR: The deleted value was the element of list")

    def test_delete_node_at_last_position(self):
        print("\n\nTESTING: delete function for removing value from the list")
        test_list = prepare_list()
        print("Current linked list:", end=" ")
        test_list.print_all_nodes()
        test_list.delete(66)
        try:
            self.assertEqual(test_list.to_values_list(), [42, 33, 11, 22, 15, 42, 10, 32, 42, 60, 70])
            print("\n\t--->Element deleted from the tail.")
        except:
            print("\n\tERROR: Element NOT deleted from the tail.")

    def test_delete_node_at_head(self):
        print("\n\nTESTING: delete function to remove the element from head position.")
        test_list = prepare_list()
        print("Current linked list:", end=" ")
        test_list.print_all_nodes()
        test_list.delete(42)
        try:
            self.assertEqual(test_list.to_values_list(), [33, 11, 22, 15, 42, 10, 32, 42, 60, 70, 66])
            print("\n\t--->The value successfully deleted from head position.")
        except:
            print("\n\tERROR: The value NOT deleted from head position")

    def test_delete_node_from_list_with_1_element(self):
        print("\n\nTESTING: delete function for list with only one elemnt.")
        test_list = LinkedList()
        test_list.add_in_tail(Node(42))
        print("Current linked list:", end=" ")
        test_list.print_all_nodes()
        test_list.delete(42)
        try:
            self.assertEqual(test_list.to_values_list(), [])
            print("\n\t--->List is empty now.")
        except:
            print("\n\t--->ERROR: List is having more than one element.")

        try:
            self.assertIs(test_list.head, None)
            print("\t--->Head pointer pointing to NULL.")
        except:
            print("\t--->Dangling Head pointer.")

        try:
            self.assertIs(test_list.tail, None)
            print("\t--->Tail pointer pointing to NULL.")
        except:
            print("\t--->Dangling tail pointer.")

    def test_delete_node_from_empty_list(self):
        print("\n\nTESTING: delete function to delete elemnt from empty list.")
        test_list = LinkedList()
        test_list.delete(12)
        try:
            self.assertEqual(test_list.to_values_list(), [])
            self.assertIs(test_list.head, None)
            self.assertIs(test_list.tail, None)
            print("\t--->Linked list is empty, so value cant be deleted.")
        except:
            print("\t--->ERROR: List is not empty initially.")

    def test_delete_all_nodes_present_multiple(self):
        print("\n\nTESTING: delete function for all nodes having same values")
        test_list = prepare_list()
        print("Current linked list:", end=" ")
        test_list.print_all_nodes()
        test_list.delete(42, all=True)
        try:
            self.assertEqual(test_list.to_values_list(), [33, 11, 22, 15, 10, 32, 60, 70, 66])
            print("\n\t--->Deleted all occurences of the value 42 from list.")
        except:
            print("\n\tERROR: All occurences of 42 NOT deleted")


if __name__ == '__main__':
    unittest.main()
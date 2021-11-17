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
        test_list.delete(99)
        try:
            self.assertEqual(test_list.to_values_list(), [42, 33, 11, 22, 15, 42, 10, 32, 42, 60, 70, 66])
            print("\n\t--->Value 99 is not the element of list")
        except:
            print("\n\tERROR: The deleted value was the element of list")

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

    def test_delete_all_nodes_comes_one_by_one_at_last_positions(self):
        print("\n\nTESTING: deleting all occurences from list from last positions one by one")
        test_list = prepare_list()
        test_list.add_in_tail(Node(66))
        print("Current linked list:")
        test_list.print_all_nodes()
        test_list.delete(66, all=True)
        try:
            self.assertEqual(test_list.to_values_list(), [42, 33, 11, 22, 15, 42, 10, 32, 42, 60, 70])
            print("\n\t--->Deleted all the occurences of value 66 from last positions of list.")
        except:
            print("\n\tERROR: All same elements from last positions NOT deleted")

    def test_delete_all_nodes_comes_one_by_one_at_first_positions(self):
        print("\n\nTESTING: delete function to delete the same nodes comes one by one at first positions.")
        test_list = prepare_list()
        node = test_list.find(42)
        test_list.insert(node, Node(42))
        print("Current linked list:", end=" ")
        test_list.print_all_nodes()
        test_list.delete(42, all=True)
        try:
            self.assertEqual(test_list.to_values_list(), [33, 11, 22, 15, 10, 32, 60, 70, 66])
            print("\n\t--->All same nodes coming from first position in linkes list deleted.")
        except:
            print("\n\tERROR: Failed to delete all same elements come one by one in LL at first position.")

    def test_delete_all_nodes_comes_one_by_one_at_center_positions(self):
        print("\n\nTESTING: delete function to delete nodes come after one another at center")
        test_list = prepare_list()
        node = test_list.find(15)
        test_list.insert(node, Node(15))
        print("Current linked list:", end=" ")
        test_list.print_all_nodes()
        test_list.delete(15, all=True)
        try:
            self.assertEqual(test_list.to_values_list(), [42, 33, 11, 22, 42, 10, 32, 42, 60, 70, 66])
            print("\n\t--->Successfully deleted same nodes coming one after another in list at center")
        except:
            print("\n\tERROR: NOT deleted the same nodes coming at center position")

    def test_clean_with_normal_list(self):
        print("\n\nTESTING: Clean function to make tha full linked list empty")
        test_list = prepare_list()
        print("Current linked list:", end=" ")
        test_list.print_all_nodes()
        test_list.clean()
        try:
            self.assertEqual(test_list.to_values_list(), [])
            print("\n\tList cleaned successfully. List is EMPTY now.")
        except:
            print("\n\tERROR: List NOT Cleaned completely.")

    def test_clean_with_empty_list(self):
        print("\n\nTESTING: Clean function over empty list")
        test_list = LinkedList()
        test_list.clean()
        try:
            self.assertEqual(test_list.to_values_list(), [])
            print("\t--->List is EMPTY already.")
        except:
            print("\tERROR: List in NOT empty INITIALLY")

    def test_find_all_one_value(self):
        print("\n\nTESTING: find function to get result as only one occurence of value in list")
        test_list = prepare_list()
        print("Current linked list:", end=" ")
        test_list.print_all_nodes()
        result = test_list.find_all(33)
        try:
            self.assertEqual(result, [test_list.get_at(1)])
            print("\n\t--->The value found in list only once")
        except:
            print("\n\tERROR: Found the value more than one time in list")

    def test_find_all_multiple_values(self):
        print("\n\nTESTING: find function to find number of occurences for value present multiple times in list")
        test_list = prepare_list()
        print("Current linked list:", end=" ")
        test_list.print_all_nodes()
        result = test_list.find_all(42)
        try:
            self.assertEqual(result, [test_list.get_at(0), test_list.get_at(5), test_list.get_at(8)])
            print("\n\t--->Found all the multiple values present in list")
        except:
            print("\n\tERROR: NOT found the values multiple times")

    def test_length_normal_list(self):
        print("\n\nTESTING:Length of the list")
        test_list = prepare_list()
        print("Current linked list:", end=" ")
        test_list.print_all_nodes()
        result = test_list.len()
        try:
            self.assertEqual(result, 12)
            print("\n\t--->The length of the list is 12")
        except:
            print("\n\tERROR: Length function failed to return correct result.")

    def test_length_empty_list(self):
        print("\n\nTESTING: length function over empty linked list")
        test_list = LinkedList()
        result = test_list.len()
        try:
            self.assertEqual(result, 0)
            print("\t--->Linked list of length zero")
        except:
            print("\tERROR: Length function fails to return length zero for empty list")

    def test_insert_standard_node(self):
        print("\n\nTESTING: insert function to insert node at given position")
        test_list = prepare_list()
        print("Inserting element after element at specific position")
        test_list.insert(test_list.get_at(1), Node(36))
        try:
            self.assertEqual(test_list.to_values_list(), [42, 33, 36, 11, 22, 15, 42, 10, 32, 42, 60, 70, 66])
            print("\t--->Inserted successfully in linked list:", end=" ")
            test_list.print_all_nodes()
        except:
            print("\tERROR: element NOT inserted properly")

    def test_insert_node_after_first_element(self):
        print("\n\nTESTING: insert function to insert node after first elemet")
        test_list = prepare_list()
        test_list.insert(test_list.get_at(0), Node(36))
        try:
            self.assertEqual(test_list.to_values_list(), [42, 36, 33, 11, 22, 15, 42, 10, 32, 42, 60, 70, 66])
            print("\t--->Successfully inserted in list:", end=" ")
            test_list.print_all_nodes()
        except:
            print("\tERROR: NOT inserted properly")

    def test_insert_node_after_last_element(self):
        print("\n\nTESTING: insert function to insert after last element")
        test_list = prepare_list()
        test_node = Node(36)
        test_list.insert(test_list.get_at(11), test_node)
        try:
            self.assertEqual(test_list.to_values_list(), [42, 33, 11, 22, 15, 42, 10, 32, 42, 60, 70, 66, 36])
            self.assertEqual(test_list.tail, test_node)
            print("\t--->Successfully inserted after last element:", end=" ")
            test_list.print_all_nodes()
        except:
            print("\tERROR: NOT inserted properly")

    def test_insert_node_in_empty_list(self):
        test_list = LinkedList()
        test_node = Node(42)
        test_list.insert(None, test_node)
        self.assertEqual(test_list.to_values_list(), [42],
                         "Testing: 'insert'.\n"
                         "Failed while inserting element in empty list after None element.\n"
                         "Values error")
        self.assertEqual(test_node, test_list.head,
                         "Testing: 'insert'.\n"
                         "Failed while inserting element in empty list after None element.\n"
                         "Bad head pointer")
        self.assertEqual(test_node, test_list.tail,
                         "Testing: 'insert'.\n"
                         "Failed while inserting element in empty list after None element.\n"
                         "Bad tail pointer")

    def test_sum_lists_normal_case(self):
        print("\n\nTESTING: sum function to add elemets of two linked lists of equal legths")
        list1 = prepare_list()
        list2 = prepare_list()
        result = LinkedList.sum_lists(list1, list2)
        try:
            self.assertEqual(result.to_values_list(), [84, 66, 22, 44, 30, 84, 20, 64, 84, 120, 140, 132])
            print("\t--->added the lists successfully")
        except:
            print("\tERROR: Lists not added properly.")

    def test_sum_lists_different_length(self):
        print("\n\nTESTING: sum function to add different length lists")
        list1 = prepare_list()
        list2 = prepare_list()
        list2.delete(33)
        result = LinkedList.sum_lists(list1, list2)
        try:
            self.assertEqual(result, None)
            print("\t--->Result is empty list as we can not add lists of different lengths")
        except:
            print("\tERROR: Sum function failed")

    def test_sum_lists_with_zero_length(self):
        print("\n\nTESTING: sum function to add two empty lists")
        list1 = LinkedList()
        list2 = LinkedList()
        result = LinkedList.sum_lists(list1, list2)
        try:
            self.assertEqual(result.to_values_list(), [])
            print("\t--->added successfully, result is another empty list.")
        except:
            print("\tERROR: sum function failed to add empty lists.")


if __name__ == '__main__':
    unittest.main()

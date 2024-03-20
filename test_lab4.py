from rb_tree import Node, rb_tree
import unittest
 
class T0_tree_left_rotation(unittest.TestCase):

    def test_tree_left_rotation_1(self):
        print("\n")
        print("tree_left_rotation")
        tree = rb_tree()
        tree.bst_insert(2)
        tree.bst_insert(1)
        tree.bst_insert(3)
        tree.print_tree()
        print("intial prorder tree", "\n")
        tree.left_rotate(tree.root)
        tree_preorder = [node.data for node in tree.preorder()]
        self.assertEqual(tree_preorder, [3,2,1])
        tree.print_tree()
        print("tree after left rotation about root  in prorder")
        print("\n")
    
    def test_tree_left_rotation_2(self):
        print("\n")
        print("tree_left_rotation")
        tree = rb_tree()
        tree.bst_insert(7)
        tree.bst_insert(5)
        tree.bst_insert(9)
        tree.bst_insert(3)
        tree.bst_insert(6)
        tree.bst_insert(8)
        tree.bst_insert(10)
        tree.bst_insert(1)
        tree.bst_insert(2)
        tree.print_tree()
        print("intial prorder tree", "\n")
        tree.left_rotate(tree.root)
        tree_preorder = [node.data for node in tree.preorder()]
        self.assertEqual(tree_preorder, [9,7,5,3,1,2,6,8,10])
        tree.print_tree()
        print("tree after left rotation about root  in prorder")
        print("\n")
    
    #my test cases

    #1: keyerror checker
    def test_tree_left_rotation_3(self):
        print("\n")
        print("my unit test: tree_left_rotation - keyerror")
        tree = rb_tree()
        tree.bst_insert(8)
        tree.bst_insert(3)
        tree.print_tree()
        print("intial prorder tree", "\n")
        tree.left_rotate(tree.root.left)
        with self.assertRaises(KeyError) as raises:
            tree.left_rotate(tree.root.left)

    #2: test case 1 - intermediate node
    def test_tree_left_rotation_4(self):
        print("\n")
        print("tree_left_rotation - test 1")
        tree = rb_tree()
        tree.bst_insert(12)
        tree.bst_insert(16)
        tree.bst_insert(19)
        tree.bst_insert(13)
        tree.bst_insert(4)
        tree.bst_insert(7)
        tree.bst_insert(9)
        tree.bst_insert(3)
        tree.bst_insert(8)
        tree.print_tree()
        print("intial prorder tree", "\n")
        tree.left_rotate(tree.root.right)
        tree_preorder = [node.data for node in tree.preorder()]
        self.assertEqual(tree_preorder, [12, 4, 3, 7, 9, 8, 19, 16, 13])
        tree.print_tree()
        print("tree after left rotation about root  in prorder")
        print("\n")


    #3: test case 2
    def test_tree_left_rotation_5(self):
        print("\n")
        print("tree_left_rotation - test 2")
        tree = rb_tree()
        tree.bst_insert(23)
        tree.bst_insert(35)
        tree.bst_insert(16)
        tree.bst_insert(42)
        tree.bst_insert(24)
        tree.bst_insert(57)
        tree.bst_insert(29)
        tree.bst_insert(13)
        tree.bst_insert(18)
        tree.print_tree()
        print("intial prorder tree", "\n")
        tree.left_rotate(tree.root)
        tree_preorder = [node.data for node in tree.preorder()]
        self.assertEqual(tree_preorder, [35, 23, 16, 13, 18, 24, 29, 42, 57])
        tree.print_tree()
        print("tree after left rotation about root  in prorder")
        print("\n")

        


class T1_tree_right_rotation(unittest.TestCase):

    def test_tree_right_rotation_1(self):
        print("\n")
        print("tree_right_rotation")
        tree = rb_tree()
        tree.bst_insert(2)
        tree.bst_insert(1)
        tree.bst_insert(3)
        tree.print_tree()
        print("intial prorder tree", "\n")
        tree.right_rotate(tree.root)
        tree_preorder = [node.data for node in tree.preorder()]
        self.assertEqual(tree_preorder, [1,2,3])
        tree.print_tree()
        print("tree after right rotation about root  in prorder")
        print("\n")
    
    def test_tree_right_rotation_2(self):
        print("\n")
        print("tree_right_rotation")
        tree = rb_tree()
        tree.bst_insert(7)
        tree.bst_insert(5)
        tree.bst_insert(9)
        tree.bst_insert(3)
        tree.bst_insert(6)
        tree.bst_insert(8)
        tree.bst_insert(10)
        tree.bst_insert(1)
        tree.bst_insert(2)
        tree.print_tree()
        print("intial prorder tree", "\n")
        tree.right_rotate(tree.root)
        tree_preorder = [node.data for node in tree.preorder()]
        self.assertEqual(tree_preorder, [5,3,1,2,7,6,9,8,10])
        tree.print_tree()
        print("tree after right rotation about root  in prorder")
        print("\n")



    #my test cases

    #1: keyerror
    def test_tree_right_rotation_3(self):
        print("\n")
        print("tree_right_rotation - key error")
        tree = rb_tree()
        tree.bst_insert(1)
        tree.bst_insert(7)
      
        tree.print_tree()
        print("intial prorder tree", "\n")
        tree.right_rotate(tree.root.right)
        with self.assertRaises(KeyError) as raises:
            tree.left_rotate(tree.root.right)

    #2: test case 1 
    def test_tree_right_rotation_4(self):
        print("\n")
        print("tree_right_rotation - test 1")
        tree = rb_tree()
        tree.bst_insert(12)
        tree.bst_insert(15)
        tree.bst_insert(18)
        tree.bst_insert(2)
        tree.bst_insert(5)
        tree.bst_insert(11)
        tree.bst_insert(19)
        tree.bst_insert(6)
        tree.bst_insert(13)
        tree.print_tree()
        print("intial prorder tree", "\n")
        tree.right_rotate(tree.root)
        tree_preorder = [node.data for node in tree.preorder()]
        self.assertEqual(tree_preorder, [2, 12, 5, 11, 6, 15, 13, 18, 19])
        tree.print_tree()
        print("tree after right rotation about root  in prorder")
        print("\n")


    #3: test case 2 - intermediate node
    def test_tree_right_rotation_5(self):
        print("\n")
        print("tree_right_rotation - test 2")
        tree = rb_tree()
        tree.bst_insert(23)
        tree.bst_insert(54)
        tree.bst_insert(34)
        tree.bst_insert(62)
        tree.bst_insert(15)
        tree.bst_insert(21)
        tree.bst_insert(59)
        tree.bst_insert(62)
        tree.bst_insert(31)
        tree.print_tree()
        print("intial prorder tree", "\n")
        tree.right_rotate(tree.root.left)
        tree_preorder = [node.data for node in tree.preorder()]
        self.assertEqual(tree_preorder, [23, 54, 34, 31, 62, 59, 62])
        tree.print_tree()
        print("tree after right rotation about root  in prorder")
        print("\n")



class T2_tree_insert_color(unittest.TestCase):


    def test_tree_insert_color_0(self):
        print("\n")
        print("tree_color_check")
        
        tree = rb_tree()

        tree.insert(2)
        tree.insert(1)
        tree.insert(3)
        tree.insert(4)
        tree.print_tree()
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual(tree_preorder, [2, 1, 3, 4])
        self.assertEqual(tree_preorder_color, ['black', 'black', 'black', 'red'])
        print("\n")


    def test_tree_insert_color_1(self):
        print("\n")
        print("tree_color_check")
        
        tree = rb_tree()

        for i in range(1, 8):
            tree.insert(i)
        tree.print_tree()
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual(tree_preorder, [2, 1, 4, 3, 6, 5, 7])
        self.assertEqual(tree_preorder_color, ['black', 'black', 'red', 'black', 'black', 'red', 'red'])
        print("\n")


    #my test case
    def test_tree_insert_color_2(self):
        print("\n")
        print("tree_color_check - my test")
        
        tree = rb_tree()

        for i in range(20, 27):
            tree.insert(i)
        tree.print_tree()
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual(tree_preorder, [21, 20, 23, 22, 25, 24, 26])
        self.assertEqual(tree_preorder_color, ['black', 'black', 'red', 'black', 'black', 'red', 'red'])
        print("\n")


class T3_tree_delete(unittest.TestCase):


    def test_tree_delete_0(self):
        print("\n")
        print("tree_insert")
        #print("checking in order, preorder and post order")
        tree = rb_tree()

        tree.insert(7)
        tree.insert(5)
        tree.insert(9)
        tree.insert(6)
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual(tree_preorder, [7, 5, 6, 9])
        self.assertEqual(tree_preorder_color, ['black', 'black', 'red', 'black'])
        tree.delete(9)
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual(tree_preorder, [6, 5, 7])
        self.assertEqual(tree_preorder_color, ['black', 'black', 'black'])
        print("\n")

    def test_tree_delete_1(self):
        print("\n")
        print("tree_insert")
        print("checking in order, preorder and post order")
        tree = rb_tree()

        for i in range(1, 8):
            tree.insert(i)
        tree.delete(5)
        tree.delete(4)
        # tree.print_tree()
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual(tree_preorder, [2, 1, 6, 3, 7])
        self.assertEqual(tree_preorder_color, ['black', 'black', 'red', 'black', 'black'])
        print("\n")
    
    def test_tree_delete_color_2(self):
        print("\n")
        print("tree_left_rotation")
        tree = rb_tree()
        tree.insert(7)
        tree.insert(5)
        tree.insert(9)
        tree.insert(3)
        tree.insert(6)
        tree.insert(8)
        tree.insert(10)
        tree.insert(1)
        tree.insert(2)
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual(tree_preorder, [7, 5, 2, 1, 3, 6, 9, 8, 10])
        self.assertEqual(tree_preorder_color, ['black', 'red', 'black', 'red', 'red', 'black', 'black', 'red', 'red'])
        tree.delete(6)
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual(tree_preorder, [7, 2, 1, 5, 3, 9, 8, 10])
        self.assertEqual(tree_preorder_color, ['black', 'red', 'black', 'black', 'red', 'black', 'red', 'red'])
        tree.delete(7)
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual(tree_preorder, [8, 2, 1, 5, 3, 9, 10])
        self.assertEqual(tree_preorder_color, ['black', 'red', 'black', 'black', 'red', 'black', 'red'])
        print("\n")



    #my test cases
    def test_tree_delete_3(self):
        print("\n")
        print("tree_insert")
        print("checking in order, preorder and post order")
        tree = rb_tree()

        for i in range(21, 28):
            tree.insert(i)
        tree.delete(25)
        tree.delete(24)
        # tree.print_tree()
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual(tree_preorder, [22, 21, 26, 23, 27])
        self.assertEqual(tree_preorder_color, ['black', 'black', 'red', 'black', 'black'])
        print("\n")
    


if __name__ == "__main__":
    unittest.main()

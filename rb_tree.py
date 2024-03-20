class Node(object):
    def __init__(self, data, left = None, right = None, parent = None, color = 'red'):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent
        self.color = color


class rb_tree(object):
    """
    Data Structures: Red-Black Tree

    Attributes:
        A BST is a red-black tree if it satisfies the fact that every node is either red or black, every leaf counts as black, every simple path from a node to a descendant lead contains the same number of black nodes, and the root node is aways black. In a case that the a node is red, then both of its children are black.

    Methods:
        def print_tree(self):
            Print the data of all nodes in order

        def __print_tree(self, curr_node):
            Recursively print a subtree (in order), rooted at curr_node
            Printed in preorder

        def __print_with_colors(self, curr_node):
            Recursively print a subtree (in order), rooted at curr_node
            Printed in PREORDER
            Extracts the color of the node and print it in the format -dataC- where C is B for black and R for red
        
        def print_with_colors(self):
            Also prints the data of all node but with color indicators

        def __iter__(self):
            iterate over the nodes with inorder traversal using a for loop

        def inorder(self):
            inorder traversal : (LEFT, ROOT, RIGHT)
        
        def preorder(self):
            preorder traversal : (ROOT, LEFT, RIGHT)
        
        def postorder(self):
            postorder traversal : (LEFT, RIGHT, ROOT)

         def __traverse(self, curr_node, traversal_type):
            helper method implemented using generators and all the traversals can be implemented using a single method and yield data of the correct node/s

        def find_min(self):
            find_min travels across the leftChild of every node, and returns
        
        def find_node(self, data):
            expects a data and returns the Node object for the given data

        def __get(self, data, current_node):
            helper function __get receives a data and a node. Returns the node with the given data

        def find_successor(self, data):
            Private Method, can only be used inside of BST.

        def insert(self, data):
            put adds a node to the tree

        def bst_insert(self, data):
            Insertion for Binary Search Tree

        def __put(self, data, current_node):
            helper function __put finds the appropriate place to add a node in the tree

        def delete(self, data):
            Same as binary tree delete, except we call rb_delete fixup at the end.

        def left_rotate(self, current_node):
            Transforms the configuration of the two nodes on the right into the configuration on the left by changing a constant number of pointers

        def right_rotate(self, current_node):
            Transforms the configuration of the two nodes on the left into the configuration on the right by changing a constant number of pointers
        
        def __rb_insert_fixup(self, z):
            maintains the balancing and coloring property after bst insertion into the tree. 

        def __rb_delete_fixup(self, x):
            maintains the balancing and coloring property after bst deletion from the tree.
    """

    PREORDER = 1
    INORDER = 2
    POSTORDER = 3

    # initialize root and size
    def __init__(self):
        self.root = None
        self.sentinel = Node(None, color = 'black')
        self.sentinel.parent = self.sentinel
        self.sentinel.left = self.sentinel
        self.sentinel.right = self.sentinel
    
    def print_tree(self):
        # Print the data of all nodes in order
        self.__print_tree(self.root)
    
    def __print_tree(self, curr_node):
        # Recursively print a subtree (in order), rooted at curr_node
        # Printed in preorder
        if curr_node is not self.sentinel:
            print(str(curr_node.data), end=' ')  # save space
            self.__print_tree(curr_node.left)
            self.__print_tree(curr_node.right)

    def __print_with_colors(self, curr_node):
        # Recursively print a subtree (in order), rooted at curr_node
        # Printed in PREORDER
        # Extracts the color of the node and print it in the format -dataC- where C is B for black and R for red
        if curr_node is not self.sentinel:

            if curr_node.color is "red":
                node_color = "R"
            else:
                node_color = "B"

            print(str(curr_node.data)+node_color, end=' ')  # save space
            self.__print_with_colors(curr_node.left)
            self.__print_with_colors(curr_node.right)

    def print_with_colors(self):
        # Also prints the data of all node but with color indicators
        self.__print_with_colors(self.root)
            
            
    def __iter__(self):
        return self.inorder()

    def inorder(self):
        return self.__traverse(self.root, rb_tree.INORDER)

    def preorder(self):
        return self.__traverse(self.root, rb_tree.PREORDER)

    def postorder(self):
        return self.__traverse(self.root, rb_tree.POSTORDER)

    def __traverse(self, curr_node, traversal_type):
        if curr_node is not self.sentinel:
            if traversal_type == self.PREORDER:
                yield curr_node
            yield from self.__traverse(curr_node.left, traversal_type)
            if traversal_type == self.INORDER:
                yield curr_node
            yield from self.__traverse(curr_node.right, traversal_type)
            if traversal_type == self.POSTORDER:
                yield curr_node

    # find_min travels across the leftChild of every node, and returns the
    # node who has no leftChild. This is the min value of a subtree
    def find_min(self):
        current_node = self.root
        while current_node.left:
            current_node = current_node.left
        return current_node
    
    # find_node expects a data and returns the Node object for the given data
    def find_node(self, data):
        if self.root:
            res = self.__get(data, self.root)
            if res:
                return res
            else:
                raise KeyError('Error, data not found')
        else:
            raise KeyError('Error, tree has no root')

    # helper function __get receives a data and a node. Returns the node with
    # the given data
    def __get(self, data, current_node):
        if current_node is self.sentinel: # if current_node does not exist return None
            print("couldnt find data: {}".format(data))
            return None
        elif current_node.data == data:
            return current_node
        elif data < current_node.data:
            # recursively call __get with data and current_node's left
            return self.__get( data, current_node.left )
        else: # data is greater than current_node.data
            # recursively call __get with data and current_node's right
            return self.__get( data, current_node.right )
    

    def find_successor(self, data):
        # Private Method, can only be used inside of BST.
        current_node = self.find_node(data)

        if current_node is self.sentinel:
            raise KeyError

        # Travel left down the rightmost subtree
        if current_node.right:
            current_node = current_node.right
            while current_node.left is not self.sentinel:
                current_node = current_node.left
            successor = current_node

        # Travel up until the node is a left child
        else:
            parent = current_node.parent
            while parent is not self.sentinel and current_node is not parent.left:
                current_node = parent
                parent = parent.parent
            successor = parent

        if successor:
            return successor
        else:
            return None

    # put adds a node to the tree
    def insert(self, data):
        # if the tree has a root
        if self.root:
            # use helper method __put to add the new node to the tree
            new_node = self.__put(data, self.root)
            self.__rb_insert_fixup(new_node)
        else: # there is no root
            # make root a Node with values passed to put
            self.root = Node(data, parent = self.sentinel, left = self.sentinel, right = self.sentinel)
            new_node = self.root
            self.__rb_insert_fixup(new_node)
    
    #Insertion for Binary Search Tree
    def bst_insert(self, data):
        # if the tree has a root
        if self.root:
            # use helper method __put to add the new node to the tree
            self.__put(data, self.root)
        else: # there is no root
            # make root a Node with values passed to put
            self.root = Node(data, parent = self.sentinel, left = self.sentinel, right = self.sentinel)
        
    # helper function __put finds the appropriate place to add a node in the tree
    def __put(self, data, current_node):
        if data < current_node.data:
            if current_node.left != self.sentinel:
                new_node = self.__put(data, current_node.left)
            else: # current_node has no child
                new_node = Node(data,
                parent = current_node,
                left = self.sentinel,
                right = self.sentinel )
                current_node.left = new_node
        else: # data is greater than or equal to current_node's data
            if current_node.right != self.sentinel:
                new_node = self.__put(data, current_node.right)
            else: # current_node has no right child
                new_node = Node(data,
                parent = current_node,
                left = self.sentinel,
                right = self.sentinel )
                current_node.right = new_node
        return new_node

    
    def delete(self, data):
        # Same as binary tree delete, except we call rb_delete fixup at the end.

        z = self.find_node(data)
        if z.left is self.sentinel or z.right is self.sentinel:
            y = z
        else:
            y = self.find_successor(z.data)
        
        if y.left is not self.sentinel:
            x = y.left
        else:
            x = y.right
        
        if x is not self.sentinel:
            x.parent = y.parent

        if y.parent is self.sentinel:
            self.root = x

        else:
            if y == y.parent.left:
                y.parent.left = x
            else:
                y.parent.right = x
        
        if y is not z:
            z.data = y.data
    
        if y.color == 'black':
            if x is self.sentinel:
                self.__rb_delete_fixup(y)
            else:
                self.__rb_delete_fixup(x)


    def left_rotate(self, current_node):
        # If there is nothing to rotate with, then raise a KeyError
        # if x is the root of the tree to rotate with left child subtree T1 and right child y, 
        # where T2 and T3 are the left and right children of y then:
        # x becomes left child of y and T3 as its right child of y
        # T1 becomes left child of x and T2 becomes right child of x

        # refer page 328 of CLRS book for rotations

        """
        Transforms the configuration of the two nodes on the right into the configuration on the left by changing a constant number of pointers

        Args:
            self, current_node
            
        Raise:
            KeyError: if there is nothing to rotate with
        """

        #to see for no rotation
        if current_node is self.sentinel:   
            raise KeyError
        if self.root == None:
            raise KeyError

        rotate_left = current_node.right
        current_node.right = rotate_left.left

       #gets the parent structure of left
        if rotate_left.left != self.sentinel:
            rotate_left.left.parent = current_node

        rotate_left.parent = current_node.parent

        #with x being the root
        if current_node.parent == self.sentinel: 
            self.root = rotate_left

        #with x bring the left child
        elif current_node == current_node.parent.left: 
            current_node.parent.left = rotate_left

        #with x bring the right child
        else: 
            current_node.parent.right = rotate_left
            
        rotate_left.left = current_node
        current_node.parent = rotate_left

        
    
    def right_rotate(self, current_node):
        # If there is nothing to rotate with, then raise a KeyError
        # If y is the root of the tree to rotate with right child subtree T3 and left child x, 
        # where T1 and T2 are the left and right children of x then:
        # y becomes right child of x and T1 as its left child of x
        # T2 becomes left child of y and T3 becomes right child of y

        # refer page 328 of CLRS book for rotations

        """
        Transforms the configuration of the two nodes on the left into the configuration on the right by changing a constant number of pointers

        Args:
            self, current_node
            
        Raise:
            KeyError: if there is nothing to rotate with
        """

        #to see for no rotation
        if current_node is self.sentinel:   
            raise KeyError
        if self.root == None:
            raise KeyError

        rotate_right = current_node.left
        current_node.left = rotate_right.right

        #gets the parent structure of right
        if rotate_right.right != self.sentinel:
            rotate_right.right.parent = current_node

        rotate_right.parent = current_node.parent

        #with x being the root
        if current_node.parent == self.sentinel: 
            self.root = rotate_right

        #with x being the right child
        elif current_node == current_node.parent.right: 
            current_node.parent.right = rotate_right
        
        #with x being the left child
        else: 
            current_node.parent.left = rotate_right

        rotate_right.right = current_node
        current_node.parent = rotate_right

    
    def __rb_insert_fixup(self, z):
        # This function maintains the balancing and coloring property after bst insertion into
        # the tree. Please red the code for insert() method to get a better understanding
        # refer page 330 of CLRS book and lecture slides for rb_insert_fixup

        """
        Calls on this function if the property of the red-black tree is violated

        Args:
            self, z
        """

        while z.parent.color == "red":

            #with left child
            if z.parent == z.parent.parent.left:  
                
                #giving the new item the uncle of z
                element = z.parent.parent.right               


                #main case
                if element.color == "red":                    
                    z.parent.color = "black"
                    element.color = "black"
                    z.parent.parent.color = "red"
                    z = z.parent.parent
                
                #other cases
                else: 

                    if z == z.parent.right:           
                        z = z.parent
                        self.left_rotate(z)             
                    
                    z.parent.color = "black"
                    z.parent.parent.color = "red"
                    self.right_rotate(z.parent.parent) 

            #with right child
            else:  

                #giving the new item the uncle of z                                 
                element = z.parent.parent.left               


                if element.color == "red":
                    z.parent.color = "black"
                    element.color = "black"
                    z.parent.parent.color = "red"
                    z = z.parent.parent


                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)

                    z.parent.color = "black"
                    z.parent.parent.color = "red"
                    self.left_rotate(z.parent.parent)

        #sets to black
        self.root.color = "black"


    def __rb_delete_fixup(self, x):
        # This function maintains the balancing and coloring property after bst deletion 
        # from the tree. Please read the code for delete() method to get a better understanding.
        # refer page 338 of CLRS book and lecture slides for rb_delete_fixup

        """
        Changes colors and performs rotation to restore the red-black properties

        Args:
            self, z
        """
        
        
        #loop strucutre: ends once it reaches the root or the node is red
        while x != self.root and x.color == "black":  
      

            if x == x.parent.left:
                item = x.parent.right

                #if red node, switch to black
                if item.color == "red":            
                    item.color = "black"

                    #gets the parent as red
                    x.parent.color = "red"  

                    #left rotation of the parent   
                    self.left_rotate(x.parent) 

                    #updates color
                    item = x.parent.right         

                #when the nodes are both black, change to red
                if item.left.color == "black" and item.right.color == "black":   
                    item.color = "red"
                    x = x.parent    
                    
                else:
                    #checks to make sure that the left node is bloack
                    if item.right.color == "black":   
                        item.left.color = "black"

                        #changes to red
                        item.color = "red"            
                        self.right_rotate(item)     
                        item = x.parent.right      
                    
                    #if it is not black
                    else:                           
                        item.color = x.parent.color

                        #changes the parent to black    
                        x.parent.color = "black"    
                        item.right.color = "black"   
                        self.left_rotate(x.parent)  
                        x = self.root             
           
            else:
                item = x.parent.left               

                #if red node, switch to black
                if item.color == "red":            
                    item.color = "black"   

                    #gets the parent as red       
                    x.parent.color = "red"   

                    #right rotation of the parent  
                    self.right_rotate(x.parent)    

                    #updates color
                    item = x.parent.left               


                #when both are black
                if item.right.color == "black" and item.left.color == "black":    
                    
                    item.color = "red"            
                    x = x.parent               
                
               
                else:                         
                    
                    #updates to red
                    if item.left.color == "black": 
                        item.right.color = "black"      
                        
                        item.color = "red"          
                        self.left_rotate(item)
                        item = x.parent.left    
                    
                    
                    else:                         
                        item.color = x.parent.color  
                        x.parent.color = "black"   
                        item.left.color = "black"   
                        self.right_rotate(x.parent)  
                        x = self.root         

        #ends at black
        x.color = "black" 


    


    
    
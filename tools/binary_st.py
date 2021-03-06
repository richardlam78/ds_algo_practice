# BINARY SEARCH TREE SYMBOL TABLE ############################################
# Compared to the other implementation of a Symbol Table, this implementation 
# uses a Node class to store two pointers: a left pointer to point to a
# smaller key value, and a right pointer to point to a bigger key value than
# the current Node's value.
# Also, this implementation is an answer to question 3.2.12, so it will not
# use rank(), select(), or a count field in Node.
# 
# The text uses recursive methods to keep things consistent, but a good
# exercises is to implement them without recursion, which is how elementary
# BST's are implemented, and without a count field for each Node.
#
# First, do it recursively, for the recursion practice, then do it non-
# recursively.
# Also, these recursive implementations are not exactly Pythonic. But this can
# be changed later with default parameter values.
# 

class Node(object):
    """
    Node that stores a key-value pair and two pointers to other Nodes.
    """
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return "{}({}, {})".format(
                self.__class__.__name__, 
                self.key,
                self.value)

    # def __str__(self):
    #     return_string = str(self.key) # + " " + str(self.value)
    #     return return_string



class BinaryST(object):
    """
    Search Tree made of Nodes with methods using the basic binary search
    algorithm.
    """
    
    def __init__(self):
        self.root = None


    def size(self):
        """
        Recursion starter for finding tree size. 
        """
        # NOTE: the challenge here was to not have a count field for each Node
        # but a recursive function for size is also a slow one (linear).
        if self.root == None:
            return 0
        return self.recur_size(self.root)


    def recur_size(self, target_node):
        """
        Directly recursive function to find the number of nodes under the 
        given node as root including itself.
        """
        if target_node == None:
            return 0
        left_size = self.recur_size(target_node.left)
        right_size = self.recur_size(target_node.right)
        return 1 + left_size + right_size
    

    def put(self, key, value):
        """
        Recursion starter for adding a value or updating if exists.
        """
        if self.root == None:
            self.root = Node(key, value)
            return
        self.root = self.recur_put(self.root, key, value)


    def recur_put(self, node, key, value):
        """
        Directly recursive function to add or update the given key with given
        value..
        """
        if node == None:
            node = Node(key, value)
            return node 
        if key < node.key:
            node.left = self.recur_put(node.left, key, value)
        elif key > node.key:
            node.right = self.recur_put(node.right, key, value)
        else:
            node.value = value
        return node


    def min(self, node=None):
        """
        Return the minimum value of a subtree rooted at the given node.
        """
        if self.root == None:
            return None
        
        if not node:
            node = self.root
        
        traveling = node
        while traveling.left:
            traveling = traveling.left
        return traveling


    def delete_min(self):
        """
        Recursion starter for deleting the minimum value.
        """
        if self.root == None:
            print("Empty tree!")
        self.root = self.recur_delete_min(self.root)


    def recur_delete_min(self, node):
        """
        Directly recursive function to delete minimum value of a subtree 
        rooted at given node.
        """
        if not node.left:
            return node.right
        node.left = self.recur_delete_min(node.left)
        return node


    def max(self, key=None):
        """
        Return maximum value.
        """
        if self.root == None:
            return None

        if not self.root.right:
            if self.root.left:
                return self.root.left
            return self.root

        if not key:
            key = self.root

        traveling = key
        while traveling.right:
            traveling = traveling.right
        return traveling


    def delete(self, key):
        """
        Recursion starter for deleted node with a given key.
        """
        if self.root == None:
            return None
        try:
            self.root = self.recur_delete(self.root, key)
        except AttributeError:
            return None
   

    def recur_delete(self, node, key):
        """
        Directly recursive function to delete given key if found in subtree
        rooted at the given node.
        """

        traveling = node
        if key < traveling.key:
            traveling.left = self.recur_delete(traveling.left, key)
        elif key > traveling.key:
            traveling.right = self.recur_delete(traveling.right, key)
        else:
            if traveling.left and traveling.right:
                replacement = Node()
                successor = self.min(traveling.right)
                
                replacement.key = successor.key
                # assigning val repetitive since del_min returns a node?
                replacement.value = successor.value
                replacement.left = traveling.left
                replacement.right = self.recur_delete_min(traveling.right)
                
                # see above comment
                successor = None
                return replacement
            else: 
                if traveling.left:
                    return traveling.left
                elif traveling.right:
                    return traveling.right
                else:
                    return None
        return node


    def print_tree(self):
        """
        Recursion starter for printing entire tree.

        This and the directly recursive function that it calls is similar to 
        the implementation of the function that will return a list or sublist
        of nodes between and including two given keys.
        """
        if self.root == None:
            print("Empty tree.")
        self.recur_print(self.root)


    def recur_print(self, node):
        """
        Directly recursive function for printing each node of the tree.
        """
        if node == None:
            return 
   
        if node.left:
            self.recur_print(node.left)
        print(node)
        if node.right:
            self.recur_print(node.right)


    def get_keys(self, lo, hi):
        """
        Returns a list of Nodes with key values between and including the
        nodes with keys equal to the given lo and hi keys.
        """
        key_list = []
        self.recur_get_keys(self.root, key_list, lo, hi)
        return key_list

    def recur_get_keys(self, node, key_list, lo, hi):
        """
        Directly recursive function for printing a list of keys.
        """
        if node == None:
            return
       
        if node.key < lo:
            self.recur_get_keys(node.right, key_list, lo, hi)
        if node.key >= lo and node.key <= hi:
            self.recur_get_keys(node.left, key_list, lo, hi)
            key_list.append(node.key)
            self.recur_get_keys(node.right, key_list, lo, hi)
        if node.key > hi:
            self.recur_get_keys(node.left, key_list, lo, hi)


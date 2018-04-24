# RED BLACK TREE #############################################################
# A binary search tree that is based on the 2-3 tree and the standard binary
# search tree.
#
# It maintains tree balance like the 2-3 tree, so searching times can remain
# consistent and independent of the order of elements from input. It also
# maintains 'black balance', which is the number of black colored paths that
# it takes to get from the queried node to the root and stays the same for 
# each node.
#
# The node model used will include a key value pair, two links to other nodes,
# a 'color' boolean value, and an integer value to store the number of nodes
# in the subtree (which is an alternative to a recursive calculation).
#
# The most notable functions will the inserts, rotations, and the color flip.
#

class Node(object):
    def __init__(self, key=None, value=None,
                 color=True):
        self.key = key
        self.value = value
        self.color = color
        self.left = None
        self.right = None
        self.N = 1


class RedBlackBST(object):
    def __init__(self):
        self.root = None

    def is_red(self, node):
        if not node:
            return False
        return node.color

    def rotate_left(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        return new_root

    def rotate_right(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        return new_root

    def flip_colors(self, node):
        node.color = not node.color
        node.left.color = not node.left.color
        node.right.color = not node.right.color

    def put(self, key, value):
        self.root = self.recur_put(self.root, key, value)
        self.root.color = False

    def recur_put(self, node, key, value):
        if not node:
            return Node(key, value)

        if key < node.key:
            node.left = self.recur_put(node.left, key, value)
        elif key > node.key:
            node.right = self.recur_put(node.right, key, value)
        else:
            node.value = value

        if not self.is_red(node.left) and self.is_red(node.right):
            node = self.rotate_left(node)
        if self.is_red(node.left) and not self.is_red(node.left.left):
            node = self.rotate_right(node)
        if self.is_red(node.left) and self.is_red(node.right):
            self.flip_colors(node)

        if node.left:
            node.N += node.left.N
        if node.right:
            node.N += node.right.N
        return node
            
    def print_keys(self, node=None):
        if not node: 
            node = self.root
        if node.left:
            self.print_keys(node.left)
        print(node.key)
        if node.right:
            self.print_keys(node.right)




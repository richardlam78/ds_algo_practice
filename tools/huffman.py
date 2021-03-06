# HUFFMAN CODE ###############################################################
# Takes a string and turns each character into a sequence of 0's and 1's
# based on the frequency of each character in the input.
#
#
# OKAY, this part of the comments section has gotten out of hand. Maybe it's
# better to have personal notes and comments up here, and all the actual
# documentation of the tool inside the class wrapped in triple quotes.
#                              ^^^^^^^^^^^^
# In the book, they assume the message will just be in english and only
# include the characters of the english alphabet. That way, you would only
# need an array to store the code for each letter for the given input and
# the Node will carry the actual values.
# But is this better than using a dictionary? It actually might be just based
# on the usage of the Huffman Code. Having key:value entries of each letter
# and their 'encryption' makes it easy to store and later find the code, but
# the array does not need to know what the character is itself and a dynamic
# array would be able to store more values, which makes a dictionary
# implementation just more than necessary. So go with an array implementation
# well, at least for now.
# Aaaand of course, I forgot about the frequency sort...
#
# Also, think about if there is a better way to implement this thing.
# The HuffmanMachine is really more like a client that uses the NodeTree. But
# the problem is, the current implementation of the NodeTree does not use
# a custom compare key, it can only compare by value.
# So, consider creating a NodeTree (or an ArrayTree for that matter) that
# can compare values with a compare key, maybe implemented inside the Node
# class?
#

class Node(object):
    """
    Node that is specifically made for the Huffman Code. Besides left and right
    'pointers' the only difference is that it also carries the frequency of
    each value that the HuffmanMachine finds and uses that to navigate through
    the tree.

    Yeah. Let's have official documentation of the tool in here. Best to do this
    last.

    Also, this Node is named the same as other Nodes. Python won't be confused
    with this...would it?
    """
    def __init__(self, value=None, freq=0):
        self.data = value
        self.frequency = freq
        self.left = None
        self.right = None


class HuffmanMachine(object):
    """
    It's really all going to be explained in the comments above the class.
    Wait, is it better practice to put it in here? Huh.
    """

    def __init__(self, target_string=""):
        self.head = Node()
        self.alpha_array = []
        self.message = target_string
        self.char_key = {}            # could be a N initialized array


    def run(self):
        self.count_frequencies()
        self.sort_alpha()
        self.build_node_tree()
        self.build_char_key()


    def count_frequencies(self):
        """
        First step of the Huffman Code.

        Sort input by frequency and put it in...frequency array?
        Then it would have to be an array of Nodes.

        Also, clients don't need to explicitly use this so maybe good to
        protect this later.
        """
        # first, sort the message by value for easy counting.
        # use the stock sort function since I didn't full test mine.
        sorted_message = sorted(self.message)

        # double while loops insert create a node for each distinct char
        # and sets it's frequency count before appending it to the alpha.
        i = 0
        while i < len(sorted_message):
            new_node = Node(sorted_message[i])
            i += 1
            count = 1
            while i < len(sorted_message) and \
                  sorted_message[i] == sorted_message[i-1]:
                i += 1
                count += 1
            new_node.frequency = count
            self.alpha_array.append(new_node)


    def sort_alpha(self):
        """
        Second step of the Huffman Code as well as a reused step.
        """
        # sort the alpha arrays so that is is sorted by
        # frequency, which means not necessarily alphabetical order.
        # used: modified shell_sort
        n = len(self.alpha_array)
        gap = 1

        while gap < (n / 3):
            gap = (3 * gap) + 1

        while gap > 0:
            for i in range(gap, n):
                pivot = self.alpha_array[i]
                j = i
                while (j - gap) >= 0:
                    if self.alpha_array[j-gap].frequency > pivot.frequency or \
                       (self.alpha_array[j-gap].frequency == pivot.frequency and \
                        pivot.data == None):
                        self.alpha_array[j] = self.alpha_array[j-gap]
                    else:
                        break
                    j -= gap
                self.alpha_array[j] = pivot
            gap = (gap - 1) // 3


    def build_node_tree(self):
        """
        Third step of the Huffman Code that relies on second step.
        """
        # connect first two nodes of the sorted array that contains them,
        # resort, and repeat until all that is left in the array is the
        # root node of the whole tree.
        while len(self.alpha_array) > 1:
            new_node = Node()
            new_node.frequency = self.alpha_array[0].frequency + \
                                 self.alpha_array[1].frequency
            new_node.left = self.alpha_array.pop(0)
            new_node.right = self.alpha_array.pop(0)
            self.alpha_array.append(new_node)
            self.sort_alpha()
        self.head = self.alpha_array[0]
        # relieve alpha_array?


    def build_char_key(self):
        while self.head.frequency > 0:
            current = self.head
            # traverse through None Nodes and keep track of the path traversed.
            track = ""
            while current.data == None and current.frequency > 0:
                if current.left.frequency > 0:
                    current = current.left
                    track += "0"
                elif current.right.frequency > 0:
                    current = current.right
                    track += "1"
                else: # both left and right frequencies are 0
                    current.frequency = 0
                    current = self.head
                    track = ""

            # arrive at a Node with a value and store it.
            # set frequency to 0 to mark that it has been stored.
            self.char_key[current.data] = track
            current.frequency = 0


    def encode(self):
        encoded_message = ""
        for char in self.message:
            encoded_message += self.char_key[char]
        return encoded_message


    def decode(self, encoded_message):
        decoded_message = ""
        current = self.head
        track = ""   # testing
        for char in encoded_message:
            if current.data == None:
                if char == "0" and current.left:
                    current = current.left
                    track += "0"   # testing
                elif char == "1" and current.right:
                    current = current.right
                    track += "1"   # testing
                if current.data != None:
                    decoded_message += current.data
                    current = self.head
                    track = ""
        return decoded_message


    # FOR TESTING!
    def get_dict(self):
        ret = {}
        for alpha in self.alpha_array:
            ret[alpha.data] = alpha.frequency
        return ret


    def print_alpha(self):
        for alpha in self.alpha_array:
            print(alpha.data, alpha.frequency)

    def print_tree(self, node):
        """Use after the node tree is built."""
        current = node
        print(current.data, current.frequency)
        if current.left:
            self.print_tree(current.left)
        if current.right:
            self.print_tree(current.right)

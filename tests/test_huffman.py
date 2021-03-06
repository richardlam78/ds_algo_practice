import unittest
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), "../tools"))

from huffman import HuffmanMachine
from huffman import Node

class HuffmanTestBase(unittest.TestCase):
    """
    Test the Huffman Machine against some input.
    """

    def setUp(self):
        self.sample_input = "Ninja turtles love pizza. I love pizza too. But I love cookies more."
        self.sample_machine = HuffmanMachine(target_string=self.sample_input)


    def test_frequency_sort(self):
        """
        Runs the frequency sort function in HuffmanMachine to assure it is
        creating a good frequency table of characters
        """
        self.sample_machine.count_frequencies()
        self.sample_machine.sort_alpha()

        sample_set = set(self.sample_input)
        test_dict = self.sample_machine.get_dict()
        for char in sample_set:
            self.assertEqual(self.sample_input.count(char),
                             test_dict[char])


    def test_build_node_tree(self):
        self.sample_machine.count_frequencies()
        self.sample_machine.sort_alpha()
        self.sample_machine.build_node_tree()

        # check that the array only carries the root
        # and that it has the a frequency equal to the lenth of the
        # sample input
        self.assertEqual(1, len(self.sample_machine.alpha_array))
        self.assertEqual(len(self.sample_input),
                         self.sample_machine.head.frequency)


    def test_encode_and_decode_message(self):
        self.sample_machine.run()

        encoded_message = self.sample_machine.encode()
        decoded_message = self.sample_machine.decode(encoded_message)
        self.assertEqual(decoded_message, self.sample_input)


    def test_one_char_message(self):
        self.sample_input = "A"
        self.sample_machine = HuffmanMachine(self.sample_input)
        self.sample_machine.run()

        encoded_message = self.sample_machine.encode()
        decoded_message = self.sample_machine.decode(encoded_message)
        self.assertEqual(decoded_message, self.sample_input)




if __name__ == '__main__':
    unittest.main()



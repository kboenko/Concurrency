import unittest
import main

class ConcTest(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(main.sum_numbers(31,5), main.simpleSum())

if __name__ == '__main__':
   unittest.main()
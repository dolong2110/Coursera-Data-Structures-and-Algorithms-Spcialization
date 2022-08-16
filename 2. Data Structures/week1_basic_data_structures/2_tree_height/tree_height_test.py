import unittest
from tree_height import compute_height


class TestStringMethods(unittest.TestCase):

    def test_equal(self):
        self.assertEqual(compute_height(5, [4, -1, 4, 1, 1]), 3, "This should be 3")
        self.assertEqual(compute_height(5, [-1, 0, 4, 0, 3]), 4, "This should be 4")


if __name__ == '__main__':
    unittest.main()

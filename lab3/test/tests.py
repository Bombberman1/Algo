import unittest

from lab3.src.binary_tree import BinaryTree, in_order_traversal


class BinaryTreeTests(unittest.TestCase):
    def test_1(self):
        root = BinaryTree(12)
        root.left = BinaryTree(9)
        root.right = BinaryTree(20)
        root.left.left = BinaryTree(8)
        root.left.right = BinaryTree(11)
        root.left.right.left = BinaryTree(5)
        root.left.right.right = BinaryTree(15)
        root.right.left = BinaryTree(18)
        root.right.right = BinaryTree(40)
        root.right.right.right = BinaryTree(80)
        expected = [8, 9, 5, 11, 15, 12, 18, 20, 40, 80]
        actual = in_order_traversal(root)
        self.assertEqual(expected, actual)

    def test_2(self):
        root = BinaryTree(3)
        root.left = BinaryTree(9)
        root.right = BinaryTree(20)
        root.right.left = BinaryTree(15)
        root.right.right = BinaryTree(7)
        expected = [9, 3, 15, 20, 7]
        actual = in_order_traversal(root)
        self.assertEqual(expected, actual)

    def test_3(self):
        root = BinaryTree(9)
        root.left = BinaryTree(4)
        root.left.left = BinaryTree(3)
        root.left.left.left = BinaryTree(2)
        root.left.left.left.right = BinaryTree(90)
        root.left.left.right = BinaryTree(74)
        root.right = BinaryTree(60)
        root.right.left = BinaryTree(40)
        root.right.left.left = BinaryTree(30)
        root.right.right = BinaryTree(100)
        expected = [2, 90, 3, 74, 4, 9, 30, 40, 60, 100]
        actual = in_order_traversal(root)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

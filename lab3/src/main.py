from binary_tree import BinaryTree, in_order_traversal

if __name__ == "__main__":
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
    #
    #                          12
    #                    ______||______
    #                   /              \
    #                  9                20
    #                 / \              /  \
    #                8   11          18    40
    #                   /  \                 \
    #                  5    15                80
    #
    print(in_order_traversal(root))

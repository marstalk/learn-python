#coding=utf8
"""
doc
"""

class TreeNode:
    """
    Node represents node
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    """
    binary search tree
    """
    def convert_to_bst(self, arrs):
        """
        convert list to binary search tree
        """
        if not arrs:
            return None
        arrs.sort()
        middle_index = len(arrs) // 2
        root = TreeNode(arrs[middle_index])
        root.left = self.convert_to_bst(arrs[:middle_index])
        root.right = self.convert_to_bst(arrs[middle_index +1 : ])
        return root


    def query(self, root, value):
        """
        check if element exists in bst
        """
        if not root:
            return False
        if root.value == value:
            return True
        if value < root.value:
            return self.query(root.left, value)
        return self.query(root.right, value)


    def insert(self, root, value):
        """
        insert element to bst
        """
        if not root:
            return TreeNode(value)
        if value < root.value:
            root.left = self.insert(root.left, value)
        root.right = self.insert(root.right, value)


    def convert_to_list(self, root, arrs):
        """
        convert bst to list
        """
        if not root:
            return
        self.convert_to_list(root.left, arrs)
        arrs.append(root.value)
        self.convert_to_list(root.right, arrs)
        return arrs


def test_bst():
    """
    test bst function
    """
    bst = BST()
    root = bst.convert_to_bst([34, 67, 1, 5, 89, 345, 7, 94, 54])
    print(bst.query(root, 67))
    print(bst.convert_to_list(root, list()))

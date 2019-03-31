# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root, val):
        """700. Search in a binary search tree

        :type root: TreeNode
        :type val: int
        :rtyoe: TreeNode
        """
        current_node = root
        while current_node != None:
            if current_node.val == val:
                return current_node
            elif current_node.val < val:
                current_node = current_node.right
            else:
                current_node = current_node.left
        return None
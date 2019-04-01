# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root):
        """
        
        :type: TreeNode
        :rtype: bool
        """
        # solution 1
        def dfs(root, val):
            if not root:
                return True
            if root.val != val:
                return False
            else:
                return dfs(root.left, val) and dfs(root.right, val)
            
        return dfs(root, root.val)

        #solution 2
        if not root:
            return True
        if root.right and root.right.val != root.val:
            return False
        if root.left and root.left.val != root.val:
            return False
        if root:
            return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
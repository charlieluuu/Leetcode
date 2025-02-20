# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:  # avoid no root
            return None

        a = root.right
        root.right = root.left
        root.left = a
        root.right = self.invertTree(root.right)
        root.left = self.invertTree(root.left)

        return root
    
if __name__ == '__main__':
    solution = Solution()
    result = solution.invertTree([4,2,7,1,3,6,9])
    print(result)
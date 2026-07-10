# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        count = 0
        maxSeen = root.val
        queue = [(root, maxSeen)]
        res = []
        while queue:
            level = []
            for i in range(len(queue)): 
                node, maxSeen = queue.pop(0)
                maxSeen = max(maxSeen, node.val)
                level.append((node.val, maxSeen))
                if node.val >= maxSeen:
                    count += 1
                if node.left:
                    queue.append((node.left, maxSeen))
                if node.right:
                    queue.append((node.right, maxSeen))
        return count
            

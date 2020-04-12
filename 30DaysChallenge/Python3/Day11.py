# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        farthestNode = None
        farthestDistance = 0
        
        def dfsFromRoot(node ,parent ,distance):
             
            nonlocal farthestDistance
            nonlocal farthestNode
            if node is None:
                return 
            if distance > farthestDistance:
                farthestDistance = distance
                farthestNode = node
                
           # print(node ,distance , farthestDistance , farthestNode)    
            node.parent = parent
        
            dfsFromRoot(node.left, node, distance + 1)
            dfsFromRoot(node.right, node, distance + 1)
        
        dfsFromRoot(root , None ,0)
        #print(fathestDistance, farthestNode)
    
        farthestDistanceSecond= 0
    
        def dfs(node ,distance):
            nonlocal farthestDistanceSecond
      
            if node is None:
                 return 
            if hasattr(node, 'used'):
                 return
            if distance > farthestDistanceSecond:
                 farthestDistanceSecond= distance
            
            node.used = True
        
            dfs(node.left ,distance + 1)
            dfs(node.right ,distance + 1)
            dfs(node.parent ,distance + 1)
        
        
        dfs(farthestNode, 0)
        return farthestDistanceSecond
    
    
    
    
class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self,root):
        #Write your code here
        # max_depth = max(max dept of left subtree,  max depth of right subtree) + 1
        if root == None:
            return -1;
        
        # print("node: ", root.data)
        l_depth = self.getHeight(root.left)
        r_depth = self.getHeight(root.right)
        # print(l_depth, r_depth, max(l_depth, r_depth))
        return max(l_depth, r_depth) + 1

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)

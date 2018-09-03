import sys

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

    def levelOrder(self,root):
        #Write your code here
        import queue
        
        q = queue.Queue()
        if root:
            q.put(root)
            # print("q.put():", root.data)
        
        while(not q.empty()):
            item = q.get()
            # print("q.get():", item.data)
            print(item.data, end=' ')
            if (item.left):
                q.put(item.left)
                # print("q.put():", item.left.data)
            if (item.right):
                q.put(item.right)
                # print("q.put():", item.right.data)

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def insert(self,head,data):
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head  
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    """ Not be limited with the Constraints
    def removeDuplicates(self,head):
        #Write your code here
        items = []
        current = prev = head
        # print(current, prev, head)
        while current:
            # print("items:", items, "current.data:", current.data)
            # self.display(head)
            # print()
            if(current == prev):
                items.append(current.data)
                current = current.next
                # print("current == prev")
            elif(current.data in items):
                prev.next = current.next
                current = current.next
                # print("current.data in items")
            else:
                items.append(current.data)
                # print("items append:", current.data)
                prev = current
                current = current.next        
        return head
    """
    
    # with Constraints: The data elements of the linked list argument will always be in non-decreasing order.
    def removeDuplicates(self,head):
        #Write your code here
        current = prev = head
        while current:
            if(current == prev):
                current = current.next
            elif(current.data == prev.data):
                prev.next = current.next
                current = current.next
            else:
                prev = current
                current = current.next        
        return head

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
head=mylist.removeDuplicates(head)
mylist.display(head); 


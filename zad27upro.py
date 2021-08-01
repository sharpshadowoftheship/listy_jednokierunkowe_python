class Node:
    def __init__(self):
        self.val=None
        self.next=None




n1=int(input())

first1=None

for i in range(n1):
    v=Node()
    k=int(input())
    v.val=k
    v.next=first1
    first1=v


n2=int(input())

first2=None

for i in range(n2):
    p=Node()
    k=int(input())
    p.val=k
    p.next=first2
    first2=p

first=None
while p!=None and v!=None:
    n=Node()
    if p.val<v.val:
        n.val=p.val
        n.next=first
        first=n
        p=p.next
    elif v.val<p.val:
        n.val=v.val
        n.next=first
        first=n
        v=v.next


while p!=None:
    n=Node()
    n.val=p.val
    n.next=first
    first=n
    p=p.next

while v!=None:
    n=Node()
    n.val=v.val
    n.next=first
    first=n
    v=v.next




print(" ")
while n!=None:
    print(n.val)
    n=n.next




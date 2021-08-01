class Node:
    def __init__(self):
        self.val=None
        self.next=None




n1=int(input())

first1=None
mini=1000000
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




f=0
print(" ")
while v!=None and p!=None:
    zap2=v
    if p.val>v.val:
        zap=v
        v=v.next
    else:
        q=Node()
        q.val=p.val
        p=p.next
        zap.next=q
        q.next=v
        v=q

v=zap2
while p!=None:
    q=Node()
    v.next=q
    q.val=p.val
    p=p.next
    v=v.next

v=first1

while v!=None:
    print(v.val)
    v=v.next


class Node:
    def __init__(self):
        self.val=None
        self.next=None




n=int(input())

first=None
v=Node()
v.val=-1
v.next=first
first=v
for i in range(n):
    v=Node()
    k=int(input())
    v.val=k
    v.next=first
    first=v

v=Node()
v.val=-1
v.next=first
first=v

v=v.next
while (v.next).val!=-1:
    pom=v.next
    v.next=pom.next
    pom=None
    if (v.next).val!=-1:
        v=v.next


v=first
while v!=None:
    print(v.val)
    v=v.next





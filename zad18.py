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

print(" ")

f=1
zap=v
while (v.next).val!=-1:
    q=zap
    while (q.next).val!=-1:
        if v.next!=q.next:
            if (v.next).val==(q.next).val:
                f=0
                pom=q.next
                q.next=pom.next
                pom=None
            else:
                q=q.next
        else:
            q=q.next
    if f==0:
        pom=v.next
        v.next=pom.next
        pom=None
    else:
        v=v.next
    f=1


v=first
while v!=None:
    print(v.val)
    v=v.next











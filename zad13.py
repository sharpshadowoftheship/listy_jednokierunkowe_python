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




first2=None


while v!=None:
    odwru=Node()
    odwru.val=v.val
    odwru.next=first2
    first2=odwru
    v=v.next

f=0

while (odwru.next).val!=-1:
    zap=odwru
    odwru=odwru.next
    while (odwru.next).val!=-1:
        if (odwru.next).val>(zap.next).val:
            f=1
            break
        else:
            odwru=odwru.next
    if f==1:
        pom=zap.next
        zap.next=pom.next
        pom=None
        odwru=zap
    else:
        odwru=zap.next
    f=0


odwru=first2

while odwru!=None:
    print(odwru.val)
    odwru=odwru.next

#pozostaje skopiowac odwru do nowej listy by byla ona w odwrotnej kolejnosci



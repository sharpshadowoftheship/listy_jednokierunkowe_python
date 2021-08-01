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

maxi=-1
il=1
v=v.next
while True:
    zap=v
    while (v.next).val>v.val and v.next!=-1:
        il+=1
        v=v.next
    if il>maxi:
        maxi=il
        p=zap
        k=v
    il=1
    if v.val==-1 or (v.next).val==-1:
        break
    else:
        v=v.next

print(" ")
v=p

while v!=k:
    print(v.val)
    v=v.next

print(v.val)




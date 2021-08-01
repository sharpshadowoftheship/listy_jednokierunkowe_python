class Node:
    def __init__(self):
        self.val=None
        self.next=None




n=int(input())

first=None
dl=0
for i in range(n):
    v=Node()
    k=int(input())
    v.val=k
    v.next=first
    first=v
    dl+=1

pom=dl
pom-=1
for i in range(dl//2):
    zap=v
    for j in range(pom):
        v=v.next
    tmp=zap.val
    zap.val=v.val
    v.val=tmp
    pom-=2
    v=zap
    v=v.next


v=first
print(" ")
while v!=None:
    print(v.val)
    v=v.next






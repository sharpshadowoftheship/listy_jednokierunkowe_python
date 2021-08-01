class Node:
    def __init__(self):
        self.val=(None,None)
        self.next=None







n=int(input())

first=None

for i in range(n):
    v=Node()
    a=int(input())
    b=int(input())
    v.val=(a,b)
    v.next=first
    first=v

#jesli dwa zbiory sa rozlaczne to pozostawiam
#jesli nie to modyfikuje pierwszy i usuwam drugi
while v!=None:
    zap=v
    v=v.next
    pop=zap
    while v!=None:
        if zap.val[1]<v.val[0] or zap.val[0]>v.val[1]:
            v=v.next
        elif v.val[0]>=zap.val[0] and v.val[1]<=zap.val[1]:
            pom=v
            pop.next=pom.next
            pom=None
            v=v.next
        elif v.val[0]<zap.val[0] and v.val[1]>zap.val[1]:
            zap.val=v.val
            pom=v
            pop.next=pom.next
            pom=None
            v=v.next
        elif zap.val[1]>v.val[0]:
            zap.val[1]=v.val[1]
            pom=v
            pop.next=pom.next
            pom=None
            v=v.next
        elif zap.val[0]<v.val[1]:
            zap.val[0]=v.val[0]
            pom=v
            pop.next=pom.next
            pom=None
            v=v.next
        pop=pop.next
    v=zap.next

v=first
while v!=None:
    print(v.val[0]," ", v.val[1])
    v=v.next








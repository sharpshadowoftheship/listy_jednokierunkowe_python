class Node:
    def __init__(self):
        self.val=(None,None)
        self.next=None







n=int(input())

first=None
v=Node()
v.val=('!','!')
v.next=first
first=v

for i in range(n):
    v=Node()
    a=int(input())
    b=int(input())
    v.val=(a,b)
    v.next=first
    first=v

v=Node()
v.val=('!','!')
v.next=first
first=v


while (v.next).val!=('!','!'):
    pom=v.next
    while (pom.next).val!=('!','!') and pom.val!=('!','!') and pom!=None and pom.next!=None:
        if (v.next).val[1]<(pom.next).val[0] or (pom.next).val[1]<(v.next).val[0]:
            pom=pom.next
        elif (pom.next).val[0]<=(v.next).val[0] and (pom.next).val[1]>=v.next.val[1]:
            (v.next).val=(pom.next).val
            tmp=pom.next
            pom=tmp.next
            tmp=None
        elif (v.next).val[0]<=(pom.next).val[0] and (v.next).val[1]>=pom.next.val[1]:
            tmp=pom.next
            pom=tmp.next
            tmp=None
        elif (v.next).val[1]>(pom.next).val[0] and (v.next).val[0]<(pom.next).val[0] and (pom.next).val[1]>(v.next).val[1]:
            (v.next).val[1]=(pom.next).val[1]
            tmp=pom.next
            pom=tmp.next
            tmp=None
        elif (pom.next).val[1]>(v.next).val[0] and (pom.next).val[0]<(v.next).val[0] and (v.next).val[1]>(pom.next).val[1]:
            (v.next).val[0]=(pom.next).val[0]
            tmp=pom.next
            pom=tmp.next
            tmp=None
    if (v.next).val!=('!','!'):
        v=v.next

v=first
while v!=None:
    print(v.val)
    v=v.next









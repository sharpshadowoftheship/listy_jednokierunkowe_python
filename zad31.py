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
firstpd=None
firstnu=None
#pd
#nu
nu=None
pd=None

while (v.next).val!=-1:
    pom=(v.next).val
    if pom%2==0 and pom>0:
        pd=Node()
        pd.val=pom
        pd.next=firstpd
        firstpd=pd
        v=v.next
    elif pom%2!=0 and pom<0:
        nu=Node()
        nu.val=pom
        nu.next=firstnu
        firstnu=nu
        v=v.next
    else:
        q=v.next
        v.next=q.next
        q=None


print(" ")
while nu!=None:
    print(nu.val)
    nu=nu.next
print(" ")
while pd!=None:
    print(pd.val)
    pd=pd.next

print(" "," ")

v=first
while v!=None:
    print(v.val)
    v=v.next










#przesuwanie elementow majacych parzytsa ilosc piatek w zapisie osemkowym


class Node:
    def __init__(self):
        self.val=None
        self.next=None


def czy_parz_ilosc_piatek_w_okt(a):
    il5=0
    while a>0:
        if a%8==5:
            il5+=1
        a/=8
    if il5%2==0:
        return 1
    else:
        return 0




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

f=0
while (v.next).val!=-1:
    if czy_parz_ilosc_piatek_w_okt((v.next).val)==0:
        zap=(v.next).val
        pom=v.next
        v.next=pom.next
        pom=None
        q=Node()
        q.val=zap
        q.next=first
        first=q
    else:
        v=v.next


v=first
print(" ")
while v.next!=None:
    if (v.next).val==-1:
        pom=v.next
        v.next=pom.next
        pom=None
    else:
        v=v.next

v=first
while v!=None:
    print(v.val)
    v=v.next














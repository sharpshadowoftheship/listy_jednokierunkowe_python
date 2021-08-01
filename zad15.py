class Node:
    def __init__(self):
        self.val=None
        self.next=None


def czy_wieksza_ilosc_jedynek_niz_dwojek(a):
    jedynki=0
    dwojki=0
    while a>0:
        if a%3==1:
            jedynki+=1
        if a%3==2:
            dwojki+=1
        a/=3
    if jedynki>dwojki:
        return 1
    else:
        return 0

def usuwanie_jesli_warunek(v):
    while (v.next).val!=-1:
        if  czy_wieksza_ilosc_jedynek_niz_dwojek((v.next).val)==1:
            pom=v.next
            v.next=pom.next
            pom=None
        else:
            v=v.next



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



usuwanie_jesli_warunek(v)


v=first
while v!=None:
    print(v.val)
    v=v.next


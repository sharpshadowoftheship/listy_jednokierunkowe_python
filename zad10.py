class Node:
    def __init__(self):
        self.val=None
        self.next=None




n1=int(input())

first1=None
dlv=0
for i in range(n1):
    v=Node()
    k=int(input())
    v.val=k
    v.next=first1
    first1=v
    dlv+=1


n2=int(input())

first2=None
dlp=0
for i in range(n2):
    p=Node()
    k=int(input())
    p.val=k
    p.next=first2
    first2=p
    dlp+=1


if dlv>dlp:
    roz=dlv-dlp
    for i in range(roz):
        p=Node()
        p.val=0
        p.next=first2
        first2=p

if dlp>dlv:
    roz=dlp-dlv
    for i in range(roz):
        v=Node()
        v.val=0
        v.next=first1
        first1=v
dod=0



v=first1
p=first2
firstn=None
while True:
    if v.val+p.val+dod<10:
        nowa=Node()
        nowa.val=v.val+p.val+dod
        nowa.next=firstn
        firstn=nowa
        dod=0
    else:
        nowa=Node()
        nowa.val=(v.val+p.val+dod)%10
        nowa.next=firstn
        firstn=nowa
        dod=1
    if v.next!=None:
        v=v.next
        p=p.next
    else:
        break


if dod==1:
    nowa=Node()
    nowa.val=1
    nowa.next=firstn
    firstn=nowa


print(" ")
while nowa!=None:
    print(nowa.val)
    nowa=nowa.next






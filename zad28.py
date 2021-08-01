class Node:
    def __init__(self):
        self.val=None
        self.next=None




n1=int(input())

first1=None

v=Node()
v.val=-1
v.next=first1
first1=v
#pierwsza to posortowana
for i in range(n1):
    v=Node()
    k=int(input())
    v.val=k
    v.next=first1
    first1=v

v=Node()
v.val=-1
v.next=first1
first1=v

n2=int(input())

first2=None

p=Node()
p.val=-1
p.next=first2
first2=p
for i in range(n2):
    p=Node()
    k=int(input())
    p.val=k
    p.next=first2
    first2=p

p=Node()
p.val=-1
p.next=first2
first2=p

f=1
zap=p
print(" ")
while (v.next).val!=-1:
    p=zap
    while (p.next).val!=-1:
        if (p.next).val==(v.next).val:
            f=0
            q=p.next
            p.next=q.next
            q=None
        else:
            p=p.next
    if f==0:
        q=v.next
        v.next=q.next
        q=None
    if f==1:
        v=v.next
    f=1


v=first1
p=first2

while v!=None:
    print(v.val)
    v=v.next

print(" ")
while p!=None:
    print(p.val)
    p=p.next


#jeszcze usunac -1





#tuple
a=(1,2,3,4,5)
print(a.count(2))
print(a.index(3))
print(len(a))
print(a[1:4])
l=list(a)   
print(l)

b=(1,82,30,64,50,7,93,10)
print(max(b))
print(min(b))
print(sum(b))   
print(sorted(b))
# key=int(input("Enter a number to find: "))
# if key in b:
#     print("Index:", b.index(key))
# else:   
#     print("element not found") 

c=(1,2,3,4,5)
d=(6,7,8,9,10)
e=c+d
print(e)   

#list
l=[1,2,3,4,5] 
print(l.insert(2,10))  
print(l.count(2))
print(l.index(3))
print(l.append(6))
print(l.reverse())
print(l.remove(4))
print(len(l))
print(l[1:4])
print(max(l))
print(min(l))
print(sum(l))
print(sorted(l))
# print("Enter a number to find: ")
even=0
odd=0
for i in l:
    if i%2==0:
        even+=1
    else:
        odd+=1  
        print("Even numbers:", even)
        print("Odd numbers:", odd)



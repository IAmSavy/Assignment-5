#a) positive numbers           
l=[]
for i in range(10):
    a=int(input("Enter value: "))
    l.append(a)
print("\nThe positive numbers are")
for i in l:
    if i>0:
        print(i)
#b) negative numbers
print("\nThe negative numbers are")
for i in l:
    if i<0:
        print(i)
#c) odd numbers
print("\nThe odd numbers are")
for i in l:
    if i%2==1:
        print(i)
#d) even numbers
print("\nThe even numbers are")
for i in l:
    if i%2==0:
        print(i)
#e) Number of times each number occurs in the List
print("\nNumber of times each number occurs in the List")
for i in l:
    count=0
    for ele in l:
        if (ele == i):
            count = count + 1
    print("Count of",i,"=",count)
##Reverse in list in Python
list=[10,65,89,"test1"]
print(list[3][2])##priting the insex value from string
print(list[::-1])
list.reverse()
print(list)
##Sorting the list
list2=[65,2,1,100,55]
list2.sort()
print(list2)
print(list[3])
##Concatinate list
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
list3=[i+j for i,j in zip(list1,list2)]##This will cancatinate two string
print(list3)
##Squaring the list
numbers =[1,2,3,4,5,6,7]
numbers1=[]
for i in numbers:
    numbers1.append(i*i)
print(numbers1)
##Exercise 4: Concatenate two lists in the following order
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
##['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
list3=[i+j for i in list1 for j in list2]
print(list3)
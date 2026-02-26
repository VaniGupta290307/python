#ordered,changeable,allow duplicates
list1=["vani",18,"dehradun"]
list=(("vani",18,"dehradun"))
print(list1[0:2])
print("vani" in list1)
list1[1]=19
#to insert at specified index
list1.insert(2,"student")
#to insert at last
list1.append("python")
#extend list
list2=["ML","AI"]
list1.extend(list2)
#remove specified index
list1.remove("student")
list1.pop(2)
#del complete list
x=[1,2,3,4]
print(x.reverse())
print(x)

n=int(input("Enter numbers"))
list1=[]
i=0
for i in range(n):
    list1.append(i)
print(list1)

list2=[1,9,2,8]
list2.sort(reverse=True)
print(list2)
list3=list2.copy()


n=int(input("Enter total number of elements to be inserted:"))
tuple1=()
sum=0
i=0
for i in range(n):
    num=int(input("Enter a number:"))
    x=list(tuple1)
    x.append(num)
    tuple1=tuple(x)
print(tuple1)
for x in tuple1:
    sum=sum+x
    average=sum/n
print("Average of tuple elements is :",average)

n=int(input("Enter n values in range 0-3:"))
i=0
count0=0
count1=0
count2=0
count3=0
while i<n:
    num=int(input("Enter a number:"))
    if num==0:
        count0=count0+1
    if num==1:
        count1=count1+1
    if num==2:
        count2=count2+1
    if num==3:
        count3=count3+1
    i=i+1
print("Count of 0,1,2,3 is:",count0,count1,count2,count3)

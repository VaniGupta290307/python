ate=int(input("Enter date:"))
month=int(input("Enter month:"))
year=int(input("Enter year:"))

if(month==1 or month==3 or month==5 or month==7 or month==10 or month==12):
    if(date>0 and date<=31):
        print("valid date")
    else:
        print("Invalid date")
    print("Next date in calendar:")
    if(date<31):
        print(date+1,"/",month,"/",year)
    else:
        if(month==12):
            print("1/1/",year+1)
        else:
            print("1/",month+1,"/",year)

elif(month==4 or month==6 or month==9 or month==11):
    if(date>0 and date<=30):
        print("valid date")
    else:
        print("Invalid date")
    if(date<30):
        print(date+1,"/",month,"/",year)
    else:
        if(month==12):
            print("1/1/",year+1)
        else:
            print("1/",month+1,"/",year)
elif(month==2):
    if(date>0 and date<28):
        print("valid date")
    else:
        print("Invalid date")
    if(year%400==0 or (year%4==0 and year%100!=0)):
        if(date<29):
            print(date+1,"/",month,"/",year)
        else:
            print("1/3/",year)
    if(date<28):
        print(date+1,"/",month,"/",year)
    else:
        print("1/3/",year)
else:
    print("Invalid month")
print("for next date in calendar")

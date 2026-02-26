x="apple"
for i in x:
    print(i)
print(len(x))
#check string --> in ,not in (membership operator) return boolean values
print("app" in x)
print("app" not in x)
print(x[:3])
print(x[1:])
print(x[-6:-2])
print(x[-6:])
print(x[:-1])

#modifying srings-->.upper,.lower(),.split(),.replace(),.strip()
y="UPES Dehradun"
print(y.upper())
print(y.lower())
print(y.capitalize())
print(y.replace("Dehradun","mumbai"))
a="   UPES,DEHRADUN   "
print(a.strip())
print(a.split("E"))

a="Vani"
b="Gupta"
print(a+b)
print(a+" "+b)
print(a*3)

a="""Vani
Gupta
18"""
print(a)

mobile_number=7017855101
print(f"my mobile number is {mobile_number}")
print(f"the price is {10*10}")

a="my name is \"vani\" "
print('it\'s alright')


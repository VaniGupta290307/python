#ordered,changeable,not alloww duplicates
dict1={
    "name":"vani",
    "age":18,
    "city":"dehradun",
}
print(dict1["name"])
print(dict1.get("age"))
for i in dict1:
    print(i) #output keys
for i in dict1.values():
    print(i) #output values
for i,j in dict1.items():
    print(i,j) #output key and value
dict2=dict1.copy()
print(dict2)
#if duplicates
students={
    "name":"vani",
    "age":18,
    "city":"dehradun",
    "name":"amrit",
}
print(students["name"]) #output amrit

#dict_constructor
dict2=dict(name="vani",age=18,city="dehradun")
print(dict2)
 #list and tuple can be used as values in dictionary but not as keys because they are mutable

#nested dictionary
dict2={
    "person"={
        "vani"={
            "age":18,
            "city":"dehradun",
        }
        "amrit"={
            "age":20,
            "city":"delhi",
        }
    }

}
print(dict2["person"]["vani"]["age"])

a={
    "key":"value",
    "marks":100,
    "list":[99,98,100]
}

print(type(a["list"]))
print(a.keys)

#set in python => collection of non repetitive elements

s=set()
s.add(1)
s.add(2)
s.add(1)

print(s)
print("the length of the set s is : ", len(s))

#methods => s.union, s.intersection 
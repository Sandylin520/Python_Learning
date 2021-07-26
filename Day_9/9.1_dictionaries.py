# Concept_1
programming_dictionary = {
  "Bug": "The bug",
  "Function": "The function"
}


programming_dictionary["Loop"] = "The loop" #add key-value pair to dictionary

for key in programming_dictionary:
    print(key)#print the key
    print(programming_dictionary[key])#print the value


"""
Output:

Bug
The bug
Function
The function
Loop
The loop

"""

"""
# Concept_2
Nesting lists

[{
    Key:[List],
    key2:{Dict},
},
{
    Key:Value,
    Key2:Value,
}]

"""
# Concept_3
dict = {
    "a": 1,
    "b": 2,
    "c": 3,
}

# no key matches，會報錯
# dict[1] = 4
# print(dict)
for key in dict:
    dict[key] += 1
print(dict)


#更改key的value
dict["c"] = [1,2,3]
print(dict)


# Concept_4
order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}
print(order["main"][2][0])#Steak




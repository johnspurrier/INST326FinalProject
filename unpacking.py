from typing import Union


names = ["Farhan", "Nick", "Ilyas", "G", "Hanna"]
for number, name in enumerate(names):
    print(f"{name} is number {number} in the list")
    
for number in range(len(names)):
    name = names[number]
    print(f"{name} is number {number+1} in the list")
    
salaries = [("George", 1000), ("Brendan", 1500), ("Walter", 1750), ("Louise", 2000)]
for name, salary in salaries: 
    print(f"{name} has a salary of {salary}")
    
name1, salary1 = salaries[0]

# d = dict()
# d = {}
# d["Brenda"] = 1500 
# print(d["Brenda"]) or print(d.get("Brenda")) 
# print returns key error, d.get returns none if "Brenda" is not in the dict

def func1(num):
    return num+5
def func2(num):
    return num-5

def dosomething(num, op):
    funcdict = {
        "plus": func1,
        "minus": func2
    }
    return funcdict[op](num)

# things can only be in a set one time, values are unique 
# set() --> actually a class not a function, unordered 
# to create a set with values in it, use {}; knows its a set because there are no colons 

# operators --> union (|), intersection (&), difference (-), symmetric difference (^)
# union -takes two sets and gives you all of the things in the sets
# intersection - the things that are in both sets
# difference - the things that are only in one of the sets
# symmetric difference - things in one or the other but not both

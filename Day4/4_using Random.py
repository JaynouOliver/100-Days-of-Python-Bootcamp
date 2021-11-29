import random

name = input("Gimme names")
names = name.split(", ")

items = len(names)

randomChoice = random.randint(0, items-1)
personWho_will_pay = names[randomChoice]

print(personWho_will_pay + "is going to pay the bill")
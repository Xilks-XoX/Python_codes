import random

Element = ["water", "fire", "earth", "wind"]
print(Element)
ask = input("element:")
comp = random.choice(Element)

print("Computer chooses this:",comp)
print("i chose this",ask)

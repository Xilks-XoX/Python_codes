# challenge 1)
# name = input("name:")
# age = int(input("age:"))
# if age < 13:
#     print("You are a kid")
# else:
#     print("Welcome")
# print("HELLO", name.upper())

# challenge 2)
# coffees = 50
# p1 = int(input("amount of coffees:"))
# cakes = 30
# p2 = int(input("amount of cakes:"))
# total = (coffees * p1) + (cakes * p2)
# print(total)
# dis = total * (1/10)
# if total > 200:
#     print(dis)

# challenge 3)
# C = int(input("temperature (C):"))
# Kel = C + 273
# print(Kel)
# if C > 30:
#     print("hot")
# elif C < 20:
#     print("cold")
# else:
#     print("nice weather")

# challenge 4)
# user = input("username:")
# password = input("password:")
# if user == "admin" and password == "1234":
#     print("welcome")
# else:
#     print("login failed")

# challenge 5)
# name = input("name:")
# age = int(input("age:"))
# age += 1
# food = input("favourite food:")
# print(name.upper())
# print(age)
# print(food)

# challenge 6)
# num = int(input("number:"))
# if num % 2 == 0:
#     print("even number")
# else:
#     print("odd number")

# challenge 7)
# score = int(input("score:"))
# if score >= 80:
#     print("excellent")
# elif score >= 50:
#     print("pass")
# else:
#     print("fail")

# challenge 8)
# tsp = int(input("total shopping price"))
# if tsp >= 1000:
#     print("VIP customer")
# elif tsp >= 500:
#     print("You got a free gift")

# challenge 9)
# password = input("password")
# if len(password) < 6:
#     print("weak password")
# else:
#     print("strong password")

# challenge 10)
# quiz = int(input("What's 5 + 3?"))
# if quiz == 8:
#     print("correct")
# else:
#     print("try again")

# challenge 11)
# import random
# bot = random.randint(1, 10)
# player = int(input("number:"))
# if player == bot:
#     print("gg")
# else:
#     print(bot)

# challenge 12)
# # age = int(input("age:"))
# if age < 18:
#     print("child")
# else:
#     print("senior")

# challenge 13)
# score = 0
# num = int(input("number:"))
# score += num
# num2 = int(input("number:"))
# score += num2
# num3 = int(input("number:"))
# score += num3
# print(score)

# challenge 14)
# attempts = 0
# while True:
#     user = input("username:")
#     password = input("password:")
#     if user == "admin" and password == "1234":
#         print("login success")
#         break
#     elif attempts >= 2:
#         print("account locked")
#         break
#     else: 
#         print("try again")
#         attempts += 1
#         continue

# challenge 15)
# import random
# bot = random.choice(["water", "fire", "earth", "wind"])
# user = input("element:")
# print(bot)
# if user == "water" and bot == [0]:
#     print("draw")
# elif user == "water" and bot == "fire" or \
#     user == "fire" and bot == "earth" or \
#     user == "earth" and bot == "wind" or \
#     user == "wind" and bot == "water" :
#     print("you win")
# elif bot == "water" and user == "fire" or \
#     bot == "fire" and user == "earth" or \
#     bot == "earth" and user == "wind" or \
#     bot == "wind" and user == "water":
#     print("bot wins")
# else:
#     print("invalid element")

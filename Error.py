# list = ["a", "b", "c"]
# try:
#     print(list)
#     q = int(input("index:"))
#     sl = list[q]
#     print(f"You selected {sl}")
# except IndexError:
#     print("That choice is out of range")
# except ValueError:
#     print("Index only")

# try:
#     open("secret_plans.txt", "r")
# except FileNain.otFoundError:
#     print("This requested file doesn't exist")

# try:
#     "2" + 24
# except TypeError:
#     print("son 😭😭😭😭")

# try:
#     num1 = input("number:")
#     num2 = input("number:")
#     if not num1.isdigit() or not num2.isdigit():
#         raise TypeError("Both inputs must be integers")
#     int1 = int(num1)
#     int2 = int(num2)
#     print(f"heres your number {int1} and {int2}")
# except TypeError as e:
#     print(f"Error: {e}")

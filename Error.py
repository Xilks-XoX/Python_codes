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
#     print("son)

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

# import random
# def guess_number():
#     while True:
#         try:
#             num  = random.randint(1, 10)
#             guess = int(input("number:"))
#             if num ==  guess:
#                 print("correct")
#                 break
#             else:
#                 print(f"correct number: {num}")
#                 print("")
#                 continue
#         except ValueError:
#             print("NUMBERS")
#             print("")
# guess_number()

# import random
# num = [1, 2, 3, 4, 5, 6]
# for i in range(1, 6):
#     print(random.choice(num))

# words_list = ["append", "input", "tie", "win"]
# def filter_long_word(words_list):
#     new_word = input("word:")
#     words_list.append(new_word)
#     for i in words_list:
#         if len(i) > 4:
#             print(f"-{i}")
# filter_long_word(words_list)# class room:
#     def __init__(self, classname, students, teacher_name):
#         self.classname = classname
#         self.students = students
#         self.teacher_name = teacher_name
#     def preview(self):
#         print(f"class: {self.classname}")
#         print(f"students: {self.students}")
#     def teacher(self):
#         print(f"teacher: {self.teacher_name}")
# c = room("4A", 100, "Bright")
# c.preview()
# c.teacher()

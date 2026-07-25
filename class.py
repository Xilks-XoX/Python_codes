# class room:
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

# class circle:
#     def __init__ (self, r):
#         self.r = r
#     def get_area(self):
#         A = 3.142 * (self.r**2)
#         print(f"Area: {A}")
#     def get_circumference(self):
#         C = 2 * 3.142 * (self.r)
#         print(f"Circumference: {C}")
# radius = circle(7)
# radius.get_area()
# radius.get_circumference()

# class BankAccount:
#     def __init__(self, account_holder, balance):
#         self.account_holder = account_holder
#         self.balance = balance
#     def deposit(self, amount):
#         try:
#             if amount <= 0:
#                 raise ValueError("deposit: Amount must be positive")
#             self.balance += amount
#         except ValueError as e:
#             print(f"\n[ERROR] {e}")
#         except TypeError:
#             print("\n[ERROR] deposit: Invalid number type")
#     def withdraw(self, amount):
#         try:
#             if amount <= 0:
#                 raise ValueError("withdraw: Amount must be positive")
#             elif amount > self.balance:
#                 raise ValueError("withdraw: Insufficient funds")
#             self.balance -= amount      
#         except ValueError as e:
#             print(f"[ERROR] {e}")
#         except TypeError:
#             print("[ERROR] withdraw: Invalid number type")
#     def display_balance(self):
#         print("\n--- Account Status ---")
#         print(f"Account Holder: {self.account_holder}")
#         print(f"Balance: ${self.balance:.2f}")
#         print("----------------------\n")
# print("Welcome to the World Government Bank")
# BA = BankAccount("Xilks", 1000000)
# print("What do you want to do today?")
# while True:
#     print("1. Deposit")
#     print("2. Withdraw")
#     print("0. Cancel")
#     choice = input("Enter choice:").strip()
#     if choice == "1":
#         try:
#             d = float(input("Enter deposit amount: "))
#             BA.deposit(d)
#             BA.display_balance()
#         except ValueError:
#             print("[ERROR] Please enter a valid number for deposit.\n")        
#     elif choice == "2":
#         try:
#             w = float(input("Enter withdraw amount: "))
#             BA.withdraw(w)
#             BA.display_balance()
#         except ValueError:
#             print("[ERROR] Please enter a valid number for withdrawal.\n")         
#     elif choice == "0":
#         break        
#     else:
#         print("[ERROR] Invalid choice. Please select 1, 2, or 0.\n")
# print("\nThank you for using our service")

# def add_expense():
#     global expense
#     expense_input = input("name, amount, category: ")
#     parts = expense_input.split()
#     if len(parts) == 3:
#         new_expense = {
#             "name": parts[0],
#             "amount": parts[1],
#             "category": parts[2]
#         }
#         expense.append(new_expense)
#     else:
#         print("Error")
# def view_expenses():
#     for i in expense:
#         print(f"{i['name']:12}{i['amount']:12}{i['category']:12}")
# add_expense()
# view_expenses()

# class Cat:
#     def __init__(self, name):
#         self.name = name
#         self.is_hungry = True
#     def feed(self):
#         self.is_hungry = False
# cat1 = Cat("Simon")
# cat2 = Cat("Salmon")
# cat3 = Cat("Sam")
# cat2.feed()
# list = [cat1, cat2, cat3]
# for i in list:
#     if i.is_hungry == False:
#         print(f"{i.name} is full")
#     else:
#         print(f"{i.name} is hungry")

# class Spaceship:
#     def __init__(self, name):
#         self.name = name
#         self.is_launched = False
#     def launch(self):
#         self.is_launched = True
#         print(f"{self.name} launched")
# s1 = Spaceship("Apollo")
# s2 = Spaceship("Falcon")
# s3 = Spaceship("Voyager")
# s1.launch()
# s2.launch()
# fleet = [s1, s2, s3]
# print("\n---------status----------\n")
# for i in fleet:
#     if i.is_launched == True:
#         print(f"{i.name} is lauched")
#     else:
#         print(f"{i.name} is still on the launch pad")

# class Robot:
#     def __init__(self, model_name):
#         self.model_name = model_name
#         self.is_powered_on = False
#     def press_power_button(self):
#         self.is_powered_on = True
# r1 = Robot("RobotX")
# r2 = Robot("Meta")
# r3 = Robot("iRobot")
# r1.press_power_button()
# factory = (r1, r2, r3)
# for i in factory:
#     if i.is_powered_on == True:
#         print(f"{i.model_name} is active")
#     else:
#         print(f"{i.model_name} is inactive")

# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.grades = {}
#     def add_grades(self):
#         self.grades["Physics"] = 97
#         self.grades["Chemistry"] = 98
#         self.grades["Biology"] = 96
#         self.grades["Astronomy"] = 99
#     def profile(self):
#         print(self.name)
#         print(self.grades)
# s = Student("Alex")
# s.add_grades()
# s.profile()

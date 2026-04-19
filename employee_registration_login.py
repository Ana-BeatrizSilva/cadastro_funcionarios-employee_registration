print("="*30)

print("Welcome! Register the three new employees:")
print("-"*30)

name1 = input("Enter the name of the first employee: ")
id1 = int(input(f"Enter the numeric ID of {name1}: "))

name2 = input("Enter the name of the second employee: ")
id2 = int(input(f"Enter the numeric ID of {name2}: "))

name3 = input("Enter the name of the third employee: ")
id3 = int(input(f"Enter the numeric ID of {name3}: "))

print("You have registered all employees")
print("="*30)
print("Welcome! Enter your data to continue:")
print("-"*30)

name = input("Enter your name: ")

if name == name1:
    print(f"Hello, {name}!")
    user_id = int(input("Enter your ID: "))
    if user_id == id1:
        print("Access GRANTED!")
    else:
        print("Access DENIED")
elif name == name2:
    print(f"Hello, {name2}!")
    user_id = int(input("Enter your ID: "))
    if user_id == id2:
        print("Access GRANTED!")
    else:
        print("Access DENIED")
elif name == name3:
    print(f"Hello, {name3}!")
    user_id = int(input("Enter your ID: "))
    if user_id == id3:
        print("Access GRANTED!")
    else:
        print("Access DENIED")
else:
    print("Registration not found")

print("="*30)
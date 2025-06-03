"""# varible 
name = "abdul muheed"
age = 20

#list(not changeable
fruits = {"apple", "mango", "banana"}
fruits.add("orange")

#tuple (changeable)
clour = ("red", "green", "blue")

print("name: ", name)
print("list: ", fruits)
print("tuple:", clour)

# dictionary
student = {
    "name": "abdul muheed",
    "age": 20,
}

#set(no duplicate values)
numbers = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}

print("student info:", student)
print("set:", numbers)"""

# Control Structure
marks = int(input("Enter your marks: "))

if marks >= 80:
    print("Grade: A")
elif marks >= 60:
    print("Grade: B")
elif marks >= 40:
    print("Grade: C")
else:
    print("Grade: F")

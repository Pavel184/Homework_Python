# Pavel Krupenya
# Work with variables

a = 12345
b = "one, two, three"
c = 1.2345
d = True
print("Variable a =", a, " variable type is:", type(a), "\nVariable b =", b, " variable type is:", type(b),
     "\nVariable b =", c, " variable type is:", type(c), "\nVariable b =", d, " variable type is:", type(d))
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
height = float(input("Please enter your height in meters: "))
gender = input("Please input your gender(male/female): ")

if gender == "male":
    retirement = 65 - age
    print(f"Hello {name} you are {age} year(s) old.\n{retirement} year(s) left to retirement")
    if height >= 1.8:
        print("Hmm ", height, "meters, You are tall!")
elif gender == "female":
    retirement = 60 - age
    print(f"Hello {name} you are {age} year(s) old.\n{retirement} year(s) left to retirement")
    if height >= 1.8:
        print("Hmm ", height, "meters, you are tall!")
input("\nPress any button to exit")
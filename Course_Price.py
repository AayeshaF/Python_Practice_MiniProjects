name = input("Please Enter Your Name: ").strip().capitalize()
country= input("Please enter the country where you are from: ").strip().lower()
is_Student = input("Are you currently a student (yes/no): ").strip().lower()

courseName = "Python for Beginners"
price = 250

grp1 = ["egypt","turkey","syria","palestine","tunis","libya"]
grp2 = ["ksa","qatar","kuwait","bahrain","saudi arabia"]
grp3 = ["usa","italy","brazil","england","germany"]

if country in grp1:
    if is_Student=="yes":
        final_price = price - 90
    else:
        final_price = price-80
elif country in grp2:
    if is_Student=="yes":
        final_price = price - 70
    else:
        final_price = price- 60
elif country in grp3:
        final_price = price
else:
    if is_Student=="yes":
        final_price = price - 40
    else:
        final_price = price - 30

print(f"Hi {name}!")
print(f"The Course {courseName} is ${final_price}")




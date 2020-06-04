# Pavel Krupenya
# Division function

def userData(name, surname, yearOfBirth, city, email, phone):
    string = str(name), str(surname), str(yearOfBirth), str(city), str(email), str(phone)
    return " ".join(string)
print(userData(name=input("Name: "), surname=input("Surname: "), yearOfBirth=input("Year of Birth: "), city=input("City: "), email=input("Email: "), phone=input("Phone: ")))
input("\n Press Enter for exit")
name = "leo"
age = "20"
height = 175.12
weight = "72.323"
city = "Forssa"
print(f"name: {name.capitalize()}")
print(f"age: {int(age)}")
print(f"height: {float(height):.1f} CM")
print(f"weight: {float(weight):.2f} KG")
print(f"city: {city.upper()}")
# caculate BMI
bmi = float(weight) / (height / 100) ** 2
print(f"bmi: {bmi:.2f}")
if 18.5 <= bmi <= 23.9:
    print(f"You have a great figure! You are {bmi:.2f}% breeze.")
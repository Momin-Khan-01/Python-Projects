# Rent Calcutor

rent = int(input("enter your rent = "))
food = int(input("enter your food order = "))
electricity_bill = int(input("enter your bill = "))
charge_per_unit = int(input("enter your charge_per_unit = "))
persons = int(input("enter persons in living in room = "))

total_bill = electricity_bill * charge_per_unit
output = (food + rent + total_bill) // persons

print("Each persons will pay =", output)
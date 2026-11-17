value_1 = 10
value_2 = 5

# add two numbers
sum_result = value_1 + value_2
print("The sum of", value_1, "and", value_2, "is", sum_result)

# multiply two numbers
product_result = value_1 * value_2
print("The product of", value_1, "and", value_2, "is", product_result)

# subtract two numbers
difference_result = value_1 - value_2
print("The difference of", value_1, "and", value_2, "is", difference_result)

# divide two numbers
if value_2 != 0:
    division_result = value_1 / value_2
    print("The division of", value_1, "by", value_2, "is", division_result)
else:
    print("Error: Division by zero is not allowed.")

# divide two numbers using floor division
quotient_result = value_1 // value_2
print("The quotient of", value_1, "by", value_2, "is", quotient_result)

name = input("What is your name? ").strip()
print(f"Hello, {name or 'friend'}!")

lastname = input("What is your last name? ").strip()
firstname = input("What is your first name?").strip()
print(f"Hello, {lastname.upper()}!")
print(f"Hello, {firstname.title()}!")
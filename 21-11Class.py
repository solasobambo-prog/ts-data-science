# ==========================================
# PART 1: COMPENSATION CALCULATOR (if/else)
# ==========================================
print("--- Part 1: Compensation Calculator ---")
bonus_threshold = 10000
commission_rate_threshold = 0.3

name = input("What is your name? ").strip()
salary = float(input("What is your salary? "))
bonus = float(input("What is your bonus? "))
commission_rate = float(input("What is your commission rate (as a decimal)? "))

if bonus <= bonus_threshold and commission_rate <= commission_rate_threshold:
    total_compensation = salary + bonus + (salary * commission_rate)
    print(f"Total compensation for {name or 'Employee'} is: ${total_compensation:.2f}")
else:
    print(f"Salary entry for {name or 'Employee'} exceeds the threshold.")


# ==========================================
# PART 2: GRADE EVALUATOR (if / elif / else)
# ==========================================
print("\n--- Part 2: Grade Evaluator ---")
score = 45

if score >= 70:
    print(f"Score {score}: Grade A")
elif score >= 60:
    print(f"Score {score}: Grade B")
elif score >= 50:
    print(f"Score {score}: Grade C")
elif score >= 40:
    print(f"Score {score}: Grade D")
else:
    print(f"Score {score}: Grade F")


# ==========================================
# PART 3: FUNCTIONS (return vs. print)
# ==========================================
print("\n--- Part 3: Functions with return ---")

def add_numbers(num1, num2):
    return num1 + num2

# Reusing returned values in further calculations
first_sum = add_numbers(5, 3)
second_sum = add_numbers(10, 7)
print("Combined total of returned sums:", first_sum + second_sum)

# Converting user inputs to float so they add mathematically
x = float(input("Enter the first number to add: "))
y = float(input("Enter the second number to add: "))
print(f"The sum of {x} and {y} is: {add_numbers(x, y)}")


# ==========================================
# PART 4: CONDITIONALS INSIDE FUNCTIONS
# ==========================================
print("\n--- Part 4: Boolean Function ---")

def is_even(number):
    return number % 2 == 0

print("Is 4 even?", is_even(4))  # True
print("Is 5 even?", is_even(5))  # False
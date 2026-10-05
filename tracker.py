# Module 2 - Laboratory 3 - Installment 3
# Author: OLEGARIO, FERN KIAN S.
# An expense tracker that calculates totals, tax, and budget

print("=" * 40)
print(f"{'EXPENSE TRACKER':^40}")
print(f"{'Know where your money goes.':^40}")
print("=" * 40)

print("MAIN MENU")
print(f"{'[1] Add an expense':<25}(coming soon)")
print(f"{'[2] View all expenses':<25}(coming soon)")
print(f"{'[3] Show total spent':<25}(coming soon)")
print(f"{'[4] Exit':<25}(coming soon)")

name = input("What's your name? ")
print(f"Welcome, {name}! Let's log two expenses.")

subtotal = 0

item1 = input("First expense? ")
amount1 = float(input("Amount? "))
subtotal = subtotal + amount1

item2 = input("Second expense? ")
amount2 = float(input("Amount? "))
subtotal = subtotal + amount2

average = subtotal / 2

tax_percent = int(input("Tax rate %? "))
tax = subtotal * (tax_percent / 100)

total = subtotal + tax

budget = float(input("Your budget? "))
over_budget = total > budget
left = budget - total

print("-" * 40)
print("SUMMARY")
print(f" - {item1}:\t${amount1}")
print(f" - {item2}:\t${amount2}")
print(f"Subtotal:\t${subtotal}")
print(f"Average:\t${average}")
print(f"Tax ({tax_percent:.1f}%):\t${tax}")
print(f"Grand total:\t${total}")
print(f"Over budget?\t{over_budget}")
print(f"Left in budget:\t${left}")
print("-" * 40)

print(f"Made by: OLEGARIO, FERN KIAN S. | Installment 3")
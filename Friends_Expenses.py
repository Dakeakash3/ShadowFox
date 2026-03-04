# -------------------- 1. Friends List & Tuple --------------------

print("-------------------- 1. Friends List & Tuple --------------------")
friends = ["Aakash", "Rahul", "Sneha", "Priya", "Vikram"]

# Create list of tuples (name, length of name)
name_length_tuples = []

for name in friends:
    name_length_tuples.append((name, len(name)))

print("List of friends:", friends)
print("Name and length tuples:", name_length_tuples)



# -------------------- 2. Trip Expense Comparison --------------------
print("\n-------------------- 2. Trip Expense Comparison --------------------")
your_expenses = {
    "Hotel": 1200,
    "Food": 800,
    "Transportation": 500,
    "Attractions": 300,
    "Miscellaneous": 200
}

partner_expenses = {
    "Hotel": 1000,
    "Food": 900,
    "Transportation": 600,
    "Attractions": 400,
    "Miscellaneous": 150
}

# Calculate totals
your_total = sum(your_expenses.values())
partner_total = sum(partner_expenses.values())

print("\nYour total expenses:", your_total)
print("Partner total expenses:", partner_total)

# Who spent more
if your_total > partner_total:
    print("You spent more money overall.")
elif partner_total > your_total:
    print("Your partner spent more money overall.")
else:
    print("Both spent the same amount.")

# Find category with biggest difference
max_difference = 0
max_category = ""

for category in your_expenses:
    difference = abs(your_expenses[category] - partner_expenses[category])
    if difference > max_difference:
        max_difference = difference
        max_category = category

print("Highest spending difference is in:", max_category)
print("Difference amount:", max_difference)
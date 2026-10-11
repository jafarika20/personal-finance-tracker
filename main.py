
"""
My name is Karo Jafari
Expense and Income Manager

In this project, I want to use everything I know in Python.
I am trying to practice what I have learned in a real project.
"""

print("\t\tWelcome to Python with Karo!\n")

total_expenses = 0.0
total_income = 0.0
transactions = []

while True:
    user_exit = input(
        "Press E to exit, or press Enter to continue: "
    ).strip().lower()

    if user_exit == "e":
        break
    elif user_exit != "":
        print("Please enter E to exit or press Enter to continue.")
        continue

    # Get a valid transaction amount
    while True:
        amount_input = input(
            "Please enter the transaction amount (or E to exit): "
        ).strip()

        if amount_input.lower() == "e":
            user_exit = "e"
            break

        try:
            transaction_amount = float(amount_input)

            if transaction_amount <= 0:
                print("Please enter an amount greater than zero.")
                continue

            break

        except ValueError:
            print(
                "Invalid amount. Please enter a number, "
                "such as 25 or 10.50."
            )

    if user_exit == "e":
        break

    # Get a valid transaction type
    while True:
        transaction_type = input(
            "Is this an expense (E) or income (I)? Enter E/I: "
        ).strip().lower()

        if transaction_type in ("e", "i"):
            break

        print("Invalid choice. Please enter E for expense or I for income.")

    if transaction_type == "e":
        total_expenses += transaction_amount
        transactions.append(("Expense", transaction_amount))

        print(f"Expense of {transaction_amount:.2f} recorded.")

    else:
        total_income += transaction_amount
        transactions.append(("Income", transaction_amount))

        print(f"Income of {transaction_amount:.2f} recorded.")

    print()

# Show summary
print("\n--- Transaction Summary ---")

if transactions:
    for number, (kind, amount) in enumerate(transactions, start=1):
        print(f"{number}. {kind}: {amount:.2f}")
else:
    print("No transactions were recorded.")

balance = total_income - total_expenses

print(f"\nTotal income:   {total_income:.2f}")
print(f"Total expenses: {total_expenses:.2f}")
print(f"Final balance:  {balance:.2f}")

print("\nGoodbye, Karo!")

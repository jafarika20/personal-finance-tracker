
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


#تبدیل کردن به توابع==>just to easy manage and control
def Exit_Continue():
    while True:   
        user_exit = input(
            "Press E to exit, or press Enter to continue: "
        ).strip().lower()
        if user_exit == "e":
            return "e"
        
        elif user_exit=="":
            return ""
        
        else:
            print("Please enter E to exit or press Enter to continue.")
            continue


# Get a valid transaction amount
def Get_Transaction_Amount():
    while True:
        amount_input = input(
            "Please enter the transaction amount (or E to exit): "
        ).strip().lower()

        if amount_input == "e":
            return None
        try:
            transaction_amount = float(amount_input)

            if transaction_amount <= 0:
                print("Please enter an amount greater than zero.")
                continue
            return transaction_amount
        except ValueError:
            print(
                "Invalid amount. Please enter a number, "
                "such as 25 or 10.50."
            )

# Get a valid transaction type
def Get_Transaction_Type():
    while True:
        transaction_type = input(
            "Is this an expense (E) or income (I)? Enter E/I: "
        ).strip().lower()

        if transaction_type in ("e", "i"):
            return transaction_type

        print(
            "Invalid choice. Please enter E for expense or I for income."
        )

# Show_Transaction_Summary
def Show_Transaction_Summary(transactions, total_income, total_expenses):
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

while True:
    # تابع خروج
    Exit=Exit_Continue()
    if Exit== "e":
        break

    
    # Get transaction amount
    transaction_amount = Get_Transaction_Amount()

    if transaction_amount is None:
        break


    # Get a valid transaction type
    Transaction_Type=Get_Transaction_Type()

    if Transaction_Type == "e":
        total_expenses += transaction_amount
        transactions.append(("Expense", transaction_amount))

    else:
        total_income += transaction_amount
        transactions.append(("Income", transaction_amount))


# Display the final summary
Show_Transaction_Summary(
    transactions,
    total_income,
    total_expenses
)

print("\nGoodbye, Karo!")

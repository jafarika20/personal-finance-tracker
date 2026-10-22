
"""
My name is Karo Jafari
Expense and Income Manager

In this project, I want to use everything I know in Python.
I am trying to practice what I have learned in a real project.
"""



# کلاس بندی برای مدیریت بهتر کد
class ExpenseIncomeManager:
    """Manage expenses and incomes with a simple CLI."""

    def __init__(self):
        # این‌ها قبلاً متغیر سراسری بودند؛ الان ویژگی (attribute) شیء هستند
        self.total_expenses = 0.0
        self.total_income = 0.0
        self.transactions = []

    #تبدیل کردن به توابع==>just to easy manage and control
    def exit_continue(self):
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
    def get_transaction_amount(self):
        """Get a valid transaction amount (or None to exit)."""

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
    def get_transaction_type(self):
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
    def show_transaction_summary(self):
        """Display all transactions and the final balance."""
        print("\n--- Transaction Summary ---")

        if self.transactions:
            for number, (kind, amount) in enumerate(self.transactions, start=1):
                print(f"{number}. {kind}: {amount:.2f}")
        else:
            print("No transactions were recorded.")

        balance = self.total_income - self.total_expenses

        print(f"\nTotal income:   {self.total_income:.2f}")
        print(f"Total expenses: {self.total_expenses:.2f}")
        print(f"Final balance:  {balance:.2f}")

    # for run program
    def run(self):
        """ Main loop of the program."""
        print("\t\tWelcome to Python with Karo!\n")

        while True:
            # تابع خروج
            Exit=self.exit_continue()
            if Exit== "e":
                break

            
            # Get transaction amount
            transaction_amount = self.get_transaction_amount()

            if transaction_amount is None:
                break


            # Get a valid transaction type
            Transaction_Type=self.get_transaction_type()

            if Transaction_Type == "e":
                self.total_expenses += transaction_amount
                self.transactions.append(("Expense" ,transaction_amount))

            else:
                self.total_income += transaction_amount
                self.transactions.append(("Income" ,transaction_amount))


        # Display the final summary
        self.show_transaction_summary()

        print("\nGoodbye, Karo!")


if __name__ == "__main__":
    manager = ExpenseIncomeManager()
    manager.run()


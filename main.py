import os
import ast

class ExpenseTracker:
    def __init__(self, file_path="expense_data.txt"):
        self.file_path = file_path
        self.load_data()

    def load_data(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                data = file.read()
                if data:
                    self.transactions = ast.literal_eval(data)
                else:
                    self.transactions = []
        else:
            self.transactions = []

    def save_data(self):
        with open(self.file_path, "w") as file:
            file.write(str(self.transactions))

    def add_transaction(self, amount, category):
        self.transactions.append({"amount": amount, "category": category})
        self.save_data()

    def view_balance(self):
        balance = sum(transaction["amount"] for transaction in self.transactions)
        return f"Current Balance: ${balance:.2f}"

    def view_transactions(self):
        if not self.transactions:
            return "No transactions yet."
        else:
            transaction_history = "Transaction History:\n"
            for transaction in self.transactions:
                transaction_history += f"${transaction['amount']:.2f} - {transaction['category']}\n"
            return transaction_history

def main():
    tracker = ExpenseTracker()

    while True:
        print("\n1. Add Transaction\n2. View Balance\n3. View Transactions\n4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            amount = float(input("Enter the transaction amount: $"))
            category = input("Enter the category: ")
            tracker.add_transaction(amount, category)
            print("Transaction added successfully.")

        elif choice == "2":
            print(tracker.view_balance())

        elif choice == "3":
            print(tracker.view_transactions())

        elif choice == "4":
            print("Exiting the expense tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()

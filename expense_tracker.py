import os
import json
from datetime import datetime

# List to store expenses
expenses = []

# File to store expenses
expense_file = "expenses.txt"

# Load expenses from the file
def load_expenses():
    if os.path.exists(expense_file):
        with open(expense_file, "r") as file:
            try:
                global expenses
                expenses = json.load(file)
            except json.JSONDecodeError:
                expenses = []
    else:
        expenses = []

# Save expenses to the file
def save_expenses():
    with open(expense_file, "w") as file:
        json.dump(expenses, file)

# Add an expense
def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (e.g., Food, Transport): ")
    amount = input("Enter amount: ")

    # Automatically adds a dollar sign if not entered by the user
    if not amount.startswith("$"):
        amount = f"${amount}"

    expenses.append({"date": date, "category": category, "amount": amount})
    save_expenses()
    print("Expense added successfully!")

# View all expenses
def view_expenses():
    if not expenses:
        print("No expenses recorded.")
        return
    print("\nID | Date       | Category       | Amount")
    print("-" * 40)
    for index, expense in enumerate(expenses):
        print(f"{index:<3}| {expense['date']} | {expense['category']:<14} | {expense['amount']}")
    print("-" * 40)

# Remove an expense
def remove_expense():
    if not expenses:
        print("No expenses to remove.")
        return
    view_expenses()
    try:
        index = int(input("Enter the ID of the expense to remove: "))
        if 0 <= index < len(expenses):
            removed = expenses.pop(index)
            save_expenses()
            print(f"Removed expense: {removed['category']} on {removed['date']} for {removed['amount']}")
        else:
            print("Invalid ID. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid numerical ID.")

# Calculate total expenses
def total_expenses():
    total = sum(float(expense["amount"][1:]) for expense in expenses)  # Removes dollar sign for calculations
    print(f"\nTotal expenses: ${total:.2f}")

# Main menu
def main():
    load_expenses()
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Remove Expense")
        print("4. Total Expenses")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            remove_expense()
        elif choice == "4":
            total_expenses()
        elif choice == "5":
            print("Goodbye!")  
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
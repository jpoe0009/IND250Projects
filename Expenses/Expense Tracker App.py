import json
from datetime import datetime
import matplotlib.pyplot as plt

FILE_NAME = "expenses.json"

# ---------------------- DATA HANDLING ----------------------
def load_expenses():
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_expenses(expenses):
    # Sort by amount before saving
    expenses.sort(key=lambda x: x["amount"])
    with open(FILE_NAME, "w") as f:
        json.dump(expenses, f, indent=4)

# ---------------------- CORE FUNCTIONS ----------------------
def add_expense(expenses):
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")

    expense = {
        "name": name,
        "amount": amount,
        "category": category,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added!\n")


def view_expenses(expenses):
    if not expenses:
        print("No expenses found.\n")
        return

    for i, exp in enumerate(expenses):
        print(f"{i}: {exp['name']} | ${exp['amount']} | {exp['category']} | {exp['date']}")
    print()


def edit_expense(expenses):
    view_expenses(expenses)
    try:
        index = int(input("Enter index of expense to edit: "))
        exp = expenses[index]

        exp["name"] = input(f"New name ({exp['name']}): ") or exp["name"]
        exp["amount"] = float(input(f"New amount ({exp['amount']}): ") or exp["amount"])
        exp["category"] = input(f"New category ({exp['category']}): ") or exp["category"]

        # Update timestamp automatically
        exp["date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        save_expenses(expenses)
        print("Expense updated!\n")

    except (IndexError, ValueError):
        print("Invalid index.\n")


def delete_expense(expenses):
    view_expenses(expenses)
    try:
        index = int(input("Enter index to delete: "))
        removed = expenses.pop(index)
        save_expenses(expenses)
        print(f"Deleted: {removed['name']}\n")
    except (IndexError, ValueError):
        print("Invalid index.\n")


def summarize_expenses(expenses):
    if not expenses:
        print("No expenses to summarize.\n")
        return

    total = sum(exp["amount"] for exp in expenses)
    average = total / len(expenses)

    category_totals = {}
    for exp in expenses:
        category_totals.setdefault(exp["category"], 0)
        category_totals[exp["category"]] += exp["amount"]

    print("\n--- Expense Summary ---")
    print(f"Total Expenses: ${total:.2f}")
    print(f"Average Expense: ${average:.2f}")

    print("\nBy Category:")
    for cat, amt in category_totals.items():
        print(f"{cat}: ${amt:.2f}")
    print()


def generate_pie_chart(expenses):
    if not expenses:
        print("No expenses to display.\n")
        return

    category_totals = {}
    for exp in expenses:
        category_totals.setdefault(exp["category"], 0)
        category_totals[exp["category"]] += exp["amount"]

    labels = list(category_totals.keys())
    sizes = list(category_totals.values())

    plt.figure()
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.title("Expenses by Category")
    plt.show()

# ---------------------- MENU ----------------------
def main():
    expenses = load_expenses()

    while True:
        print("""
1. Add Expense
2. View Expenses
3. Edit Expense
4. Delete Expense
5. Summary
6. Pie Chart
7. Exit
""")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            edit_expense(expenses)
        elif choice == "4":
            delete_expense(expenses)
        elif choice == "5":
            summarize_expenses(expenses)
        elif choice == "6":
            generate_pie_chart(expenses)
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.\n")


if __name__ == "__main__":
    main()

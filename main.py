import json
expenses=[]
def add_expense():
      while True:
          category=input("Enter category:").strip()
          if category:
              break
          print("Category cannot be empty")
      while True:
          try:
              amount=int(input("Enter amount:"))
              if amount<=0:
                  print("Amount must be greater than 0")
                  continue
              break
          except ValueError:
              print("Please Enter a valid number:")
      while True:
          description= input("Enter description:").strip()
          if description:
              break
          print("Description cannot be empty")
      expense={
            "category":category,
            "amount":amount,
            "description":description
      }
      
      expenses.append(expense)


def view_expenses(): 
    if not expenses:
        print("No expenses avaialable")
        return
    for i, expense in enumerate(expenses,start=1):
        print(i, expense["category"],
              expense["amount"],
              expense["description"])    

def search_expense():
    key=input("Enter category to search:")
    found=True
    for expense in expenses:
        if expense["category"]==key:
            print(expense)
            found=True
        if found==False:
            print("No Expense found")    

def delete_expense():
    view_expenses()
    if not expenses:
        return
    try:
        num=int(input("Enter expense number to delete: "))
        if num<1 or num>len(expenses):
            print("Invalid expense number")
            return
        expenses.pop(num-1)
        save_expenses()

        print("Expense deleted successfully")
    except ValueError:
        print("Please enter a valid number")    
              


def total_expense():
    total=0
    for expense in expenses:
        total=total+expense["amount"]
    print("Total spending:",total) 

def category_total():
    totals={}

    for  expense in expenses:
        category=expense["category"]
        amount=expense["amount"]

        if category in totals:
            totals[category]=totals[category]+amount
        else:
            totals[category]= amount
    print(totals)                 

def save_expenses():
    with open("expenses.json","w") as file:
        json.dump(expenses,file,indent=4)
    print("Expenses saved successfully!")

def load_expenses():
    global expenses

    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)
    except FileNotFoundError:
        expenses = []


while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Search Expense")
    print("4. Delete Expense")
    print("5. Total Spending")
    print("6. Category-wise Spending")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        search_expense()
    elif choice == "4":
        delete_expense()
    elif choice == "5":
        total_expense()
    elif choice == "6":
        category_total()
    elif choice == "7":
        save_expenses()
        print("Goodbye!")
        break
    else:
        print("Invalid choice")


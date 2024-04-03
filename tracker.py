from expenses import Expenses

def main():
    print("Welcome to the Budget Tracker ")
    options = 0
    file_name = "expense_tracker.csv"
    new_expense = expense()
    save_expense(new_expense,file_name)
    summarize(file_name)
    while(True):
        options = int(input("Put 1 if you want to exit the program and 2 to continue in the budget tracker"))
        if(options == 1):
            break
        new_expense = expense()
        save_expense(new_expense,file_name)
        summarize(file_name)
    print("Thank you for using the BUdget Tracker")
    # Get User Expense
    
    
    
def expense():
    name = input("Enter the name of expense: ")
    amount = float(input("Enter the amount: "))
    month = input("Enter the month: ")
    day = int(input("Enter the date: "))
    year = int(input("Enter the year: "))
    categories = ["Food", "Home","Transportation","Work","Fun"]
    choice = 0
    while (True):
        print("Select a Category")
        for i, name1 in enumerate(categories):
            print(f" {i+1}. {name1}")
        choice = int(input("Enter the number correpsonding to the category: "))
        if choice in range(1,len(categories)+1):
            break
        else:
            print("Invalid selection. Try again")
    user_choice = determine_category(choice)
    new_expense = Expenses(name,user_choice,amount,month,day,year)
    return new_expense

def determine_category(number):
    category_choice = ""
    match number:
        case 1:
            category_choice = "Food"
        case 2:
            category_choice = "Home"
        case 3:
            category_choice = "Transportation"
        case 4:
            category_choice = "Work"
        case 5:
            category_choice = "Fun"
    return category_choice 
  
def save_expense(new_expense,file_name):
    print(f"Your Expense: {new_expense.name}, {new_expense.category}, {new_expense.amount}, {new_expense.month}, {new_expense.day}, {new_expense.year} is being saved to {file_name}")
    with open(file_name, "a") as file:
        file.write(f"{new_expense.name}, {new_expense.category}, {new_expense.amount}, {new_expense.month}, {new_expense.day}, {new_expense.year}\n")


def summarize(file_name,budget):
    expsobj = []
    with open(file_name, "r") as file:
        line = file.readlines()
        for l1 in line:
            print(l1)
            shortened_line = l1.strip()
            name,category,amount,month,day,year = shortened_line.split(",")
            new_expense = Expenses(name,category,float(amount),month,day,year)
            expsobj.append(new_expense)
        lst2 = total_spent(expsobj)
        print(f"You have a total of {lst2[0]} transactions and you have spent {lst2[1]} dollars intotal for all your expenses")
        category_amount = {}
        for expense1 in expsobj:
            key = expense1.category
            if key in category_amount:
                category_amount[key]+=expense1.amount
            else:
                category_amount[key] = expense1.amount
        print("Here are the expenses by category")
        for category,amount in category_amount.items():
             print(f"Category: {category}, Amount: {amount}")


            

def total_spent(lst):
    lst1 = []
    total_amount = 0
    transactions = 0
    for i in range(len(lst)):
        transactions = transactions + 1
        total_amount = total_amount + lst[i].amount
    lst1.append(transactions)
    lst1.append(total_amount)
    return lst1




    
    

    
    

if __name__ == "__main__":
    main()
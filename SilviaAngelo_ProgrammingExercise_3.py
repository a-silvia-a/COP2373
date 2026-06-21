#Program will ask user for a list of their monthly expenses.
#When asking the user for their expenses, it will also ask for the type of expense and the amount.
#The reduce method will be used to analyze the expenses and display the total expense,
#the highest expense and the lowest expense.

#Function prompts user for expense names and amounts, validates input,
#packs entry to a tuple, and appends it to master list
def get_user_expenses():
    expense_list = []

    while True:
        name = input("Please enter the type of expense: ")
        amount_input = input(f"Please enter the amount {name}: ")

        #Convert string to float number
        amount = float(amount_input)

        #Pack into tuple
        expense_tuple = (name, amount)
        expense_list.append(expense_tuple)

        keep_going = input("Would you like to continue (y/n)? ")
        if keep_going.lower()!= "y":
            break

    #Return finished list
    return expense_list

import functools
def analyze_and_display_expenses(expense_list):
    #Calculate expenses using reduce and lambdas
    total_expense_amount = functools.reduce(lambda acc, curr: acc + curr[1], expense_list, 0.0)
    highest_expense = functools.reduce(lambda acc, curr: curr if curr[1] > acc[1] else acc,expense_list)
    lowest_expense = functools.reduce(lambda acc, curr: curr if curr[1] < acc[1] else acc,expense_list)

    #Display results
    print("\n--- Expense Analysis Results ---")
    print(f"Total expense amount is: ${total_expense_amount:.2f}")
    print(f"Highest expense is {highest_expense[0]}: ${highest_expense[1]:.2f}")
    print(f"Lowest expense is {lowest_expense[0]}: ${lowest_expense[1]:.2f} ")

#Gathers data and analyses it.
def main():
    my_expenses = get_user_expenses()

    if my_expenses:
        analyze_and_display_expenses(my_expenses)
    else:
        print("\n--- No expenses ---")

if __name__ == "__main__":
    main()
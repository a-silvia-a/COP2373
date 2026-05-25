#program will pre-sell a limited number of cinema tickets.
#Each buyer can buy up to 4 tickets.
#No more than 20 tickets can be sold total.
#Prompt the user for the desired number of tickets and then display the number of remaining tickets
#Then display the total number of buyers.

def main():
    tickets_left = 20
    total_buyers = 0

    while tickets_left > 0:
        new_tickets_left = sell_tickets(tickets_left)

        if new_tickets_left != tickets_left:
            total_buyers = total_buyers + 1
            tickets_left = new_tickets_left

    print ("All tickets have been sold!")
    print (f"Total number of buyers: {total_buyers}")

def sell_tickets(remaining_tickets):
    print(f"\nThere are {remaining_tickets} tickets left.")
    user_input = input("How many tickets do you want to buy? ")
    requested_tickets: int = int(user_input)

    if requested_tickets < 1 or requested_tickets > 4:
        print("Error: You can only buy up to 4 tickets.")
        return remaining_tickets

    elif requested_tickets > remaining_tickets:
        print(f"Error: We only have {remaining_tickets} tickets left.")
        return remaining_tickets

    else:
        remaining_tickets = remaining_tickets - requested_tickets
        print(f"You bought {requested_tickets} tickets.")
        return remaining_tickets

if __name__ == "__main__":
    main()
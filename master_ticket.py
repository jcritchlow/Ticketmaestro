TICKET_PRICE = 10
SERVICE_CHARGE = 2

tickets_remaining = 100  

def calculate_price(number_of_tickets):
    #Create new constant for 2 dollar service charge
    return (number_of_tickets * TICKET_PRICE) + SERVICE_CHARGE

while tickets_remaining >= 1:
    print ("There are {} tickets remaining. Order soon!".format(tickets_remaining))
    username = input("Hello. What is your name? ")
    number_of_tickets = input("How many tickets would you like to buy, {}? ".format(username))
    #Expect a value error and handle it
    try:
        number_of_tickets = int(number_of_tickets)
        if number_of_tickets > tickets_remaining:
            raise ValueError("There are only {} tickets remaining".format(tickets_remaining))
    except ValueError as err:
        print("Oh no! We ran into an issue. {}. Please try again.".format(err))
    else:
        order_total = calculate_price(number_of_tickets)
        print("Your order comes out to ${}".format(order_total))
        proceed = input("Would you like to continue with your order? Press 'Y' for yes or 'N' for no: ")
        if proceed.lower() == "y":  
            print("SOLD! Thank you for your purchase!")
            tickets_remaining -= number_of_tickets
        else:
            print("Thank you, {}, have a great day!".format(username))
            
        
# Notify user that tickets are sold out if none available
print("Sorry, tickets are all sold out! :(")

# practice of fundamentals in python



# This program takes two numbers as input from the user, performs addition on them, and displays the result along with a custom message.
'''def add_data(t, l):

    x= int(input("Enter 1st number: "))
    y = int(input("Enter 2nd number: "))
    add(x,y)
    print("The", t, "is", l)

def add(num1, num2):
    print(f"The sum of {num1} and {num2} is {num1+num2}")

add_data()'''

'''def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")


def main():
    name = input("What is your name? ")
    age = int(input("What is your age? "))
    introduce(name, age)


main() '''

# This program defines a function to greet a user by name, and if no name is provided, it defaults to greeting "stranger". The main function prompts the user for their name and calls the greet function twice: once with the user's input and once without any arguments to demonstrate the default behavior.

'''def greet(name="stranger"):
    print(f"Hello, {name}!")

def main():
    name = input("What is your name? ")
    greet(name)
    greet()

main()'''

# This program defines a function to calculate the power of a number, and the main function prompts the user for a base number and an exponent, then calls the power function to compute and display the result. It also demonstrates the use of a default exponent by calling the power function with only the base number.

'''def main():
    user_input = int(input("Enter a number: "))
    exponent = int(input("Enter the exponent: "))
    result = power(user_input, exponent)
    print(f"{user_input} raised to the power of {exponent} is {result}")
    defualt_result = power(user_input, 2)
    print(f"{user_input} raised to the power of 2 is {defualt_result}")


def power(base, exponent):
    return pow(base, exponent)
main()'''


# This program defines a function to introduce a person by their name and age, and the main function prompts the user for their name and age, then calls the introduce function to display the introduction message.


'''def main():
    name = input("What is your name? ")
    age = int(input("What is your age? "))
    introduce(name, age)


def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")

main()'''

# This program takes two numbers as input from the user, performs addition and multiplication on them, and displays the results.

'''def main():
    x, y = int(input("Enter 1st number: ")), int(input("Enter 2nd number: "))
    add(x, y)
    multiply(x, y)

def add(num1, num2):
    print(f"The sum of {num1} and {num2} is {num1+num2}")
def multiply(num1, num2):
    print(f"The product of {num1} and {num2} is {num1*num2}")

main()'''

# This program converts an amount in dollars to another currency based on the exchange rate provided by the user.
'''def convert(dollers, exchange_rate):
    return dollers * exchange_rate

def main():
    dollers = float(input("Enter the amount in dollers: "))
    exchange_rate = float(input("Enter the exchange rate: "))
    converted_amount = convert(dollers, exchange_rate)
    print(f"{dollers} dollers is equal to {converted_amount} in the target currency.")
    
main()'''

# This program calculates the force acting on an object based on its mass using the formula F = m * g, where g is the acceleration due to gravity (9.8 m/s^2).

'''def calculate_force(mass):
    return mass * 9.8
def main():
    mass = float(input("Enter the mass of the object in kg: "))
    force = calculate_force(mass)
    print(f"The force acting on the object is {force} Newtons.")
main()'''

# This program calculates the total amount to be paid for a meal, including tax and tip, based on the user's input for the meal cost and whether they want to include a tip or not.

'''def tax(given_amount):
    return given_amount * 0.07
def tip(given_amount):
    return given_amount * 0.15
def main():
    given_amount = float(input("Enter the amount: "))
    question = input("Do you want to tip? ").lower().strip()
    if question == "yes":
        total_amount = given_amount + tax(given_amount) + tip(given_amount)
        print(f"The total amount including tax and tip is {total_amount}")
    else:
        total_amount = given_amount + tax(given_amount)
        print(f"The total amount including tax is {total_amount}")
main()'''



'''def draw_row(character, lenght):
    return character * lenght
def main(): 
    character = input("Enter a character to draw the row: ")
    lenght = int(input("Enter the length of the row: "))
    draw_row(character, lenght)

main()

'''

# This program takes a grade input from the user, determines the corresponding letter grade, and checks if the grade is passing or failing.

'''def main(): 
    grade = int(input("Enter your grade out of 100: "))
    print(get_grade(grade))
    print(is_passing(get_grade(grade)))




def get_grade(grade):
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 60:
        return "D"
    else:
        return "F"

def is_passing(grade):
    if grade != "F":
        return "Passed"
    else:
        return "Failed"

main()

'''


# This program calculates the total bill for an item based on its price and quantity, applies a discount based on the total bill, and then displays the final bill and savings to the user.

'''def main():
    item_price = float(input("Enter the price of the item: "))
    item_quantity = int(input("Enter the quantity of the item: "))
    total_bill = calculate_total_bill(item_price, item_quantity)
    finnally_bill = apply_discount(total_bill)
    print(f"This is your total bill: {total_bill}")
    print(f"Your total bill after discount is: {finnally_bill}")
    print(f"You saved: {total_bill - finnally_bill}")
    print("Thank you for shopping with us!")


def calculate_total_bill(price, quantity):
    return price * quantity

def apply_discount(total_bill,):
    if total_bill >= 1000:
        return total_bill - (total_bill * 0.2)
    elif 1000 > total_bill >= 500:
        return total_bill - (total_bill * 0.1)
    elif 500 > total_bill >= 200:
        return total_bill - (total_bill * 0.05)
    else:
        return total_bill





main()'''



# This program calculates the cost of a trip based on the travel class, age of the traveler, and whether it's a round trip or not.

'''def base_price(travel_class):
    if travel_class == "1":
        return 20000
    elif travel_class == "2":
        return 12000
    elif travel_class == "3":
        return 5000
    else:
        return "Invalid travel class. Please enter accordingly."
def age_discount(age, price):
    if age < 12:
        return price * 0.5
    elif 12 <= age < 18:
        return price * 0.2
    elif age >= 60:
        return price * 0.3
    else:
        return 0
    
def trip_cost(price, is_round_trip):
    if is_round_trip == "yes":
        return price * 1.8
    else:
        return price

def main():
    travel_class = input("Enter the travel class first - 1, buisness - 2, or first - 3: ")
    is_round_trip = input("Is it a round trip? (yes/no): ").lower().strip()
    age = int(input("Enter your age: "))
    price = base_price(travel_class)
    discount = age_discount(age, price)
    print(f"The base price for the selected travel class is: {price}")
    print(f"The discount based on age is: {discount}")
    final_price = trip_cost(price - discount, is_round_trip)
    print(f"The final price for the trip is: {final_price}")


main()
'''

# This program simulates a simple banking system where the user can check their PIN, balance, and perform withdrawal or deposit operations.


def check_pin(entered_pin, actual_pin):
    if entered_pin == actual_pin:
        return "Access granted"
    else:
        return "Access denied"
    
def check_balance(balance,amount):
    if amount <= balance:
        return True
    else:
        return False
    

def withdraw(balance, amount):
    if check_balance(balance, amount):
        return balance - amount
    else:
        return balance

def deposit(balance, amount):
    return balance + amount

def main():
    actual_pin = "1234"
    balance = 10000.0
    entered_pin = input("Enter your PIN: ")
    result = check_pin(entered_pin, actual_pin)
    print(result)
    if result == "Access granted":
        action = input("Do you want to withdraw or deposit? (withdraw/deposit/check): ").lower().strip()
        if action == "withdraw":
            amount = float(input("Enter the amount: "))
            balance = withdraw(balance, amount)
            print(f"Your new balance after withdrawal is: {balance}")
        elif action == "deposit":
            amount = float(input("Enter the amount: "))
            balance = deposit(balance, amount)
            print(f"Your new balance after deposit is: {balance}")
        elif action == "check":
            print(f"Your current balance is: {balance}")
        else:
            print("Invalid action. Please choose either 'withdraw' or 'deposit'.")
    else:
        print("Please try again with the correct PIN.")
        return

main()

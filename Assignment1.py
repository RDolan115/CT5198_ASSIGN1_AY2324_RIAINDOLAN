# Name: Riain Dolan
# Student ID: 19363073
# Date: 16/01/2024
"""
This Python program collects and analyses data on the number of customers a business had each day over a week.

Features:
a. Creates a list to store the number of customers that a business had each day.
b. Uses a for loop to ask the user to input the number of customers each day over a 7-day period.
c. Determines the maximum, minimum, and average number of customers for the week and prints the results.

Usage:
1. Run the script.
2. Enter the number of customers for each day when prompted.
3. View the results, including maximum, minimum, and average number of customers.
"""


def main():
    # Part a: Create a list to store the number of customers each day
    # Create a list containing the days of the week
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    # List setting the initial value of customer count to zero for each day
    # List of length 7 = len(days)
    customer_count = [0] * len(days)

    # Part b: Use a for loop to get user input for each day
    # The for loop is implemented over each day
    for i in range(len(days)):
        day = days[i]
        # While, try, and except to catch any invalid inputs and continue prompting the user for a correct input
        while True:
            try:
                # Input an integer for the number of customers each day
                customers = int(input(f"Enter the number of customers for {day}: "))
                # Only allow positive integer inputs
                if customers < 0:
                    print("Please enter a non-negative number of customers.")
                else:
                    # Break if a positive integer is input
                    break
                # Handle value errors, such as inputting a string instead of an integer
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        # Update the customer count value with the inputted value for that day
        customer_count[i] = customers

    # Part c: Determine maximum, minimum, and average number of customers
    # Use built-in max function
    max_customers = max(customer_count)
    # Built-in min function
    min_customers = min(customer_count)
    # Built-in sum and length functions to find the average
    avg_customers = sum(customer_count) / len(customer_count)

    # Print the results
    print("\nResults:")
    print(f"Maximum number of customers: {max_customers}")
    print(f"Minimum number of customers: {min_customers}")
    # Rounding the average to 2 decimal places
    print(f"Average number of customers: {avg_customers:.2f}")


if __name__ == "__main__":
    main()

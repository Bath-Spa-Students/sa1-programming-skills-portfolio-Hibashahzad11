# Function to check if a number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return f"{number} is even."
    else:
        return f"{number} is odd."

# Main function
def main():
    try:
        user_input = int(input("Enter a number: "))  # Ask the user for a number
        result = check_even_odd(user_input)          # Call the function
        print(result)                                # Print the returned message
    except ValueError:
        print("Please enter a valid integer.")

# Run the main function
if __name__ == "__main__":
    main()
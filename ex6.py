# Define the correct password 
correct_password = "12345"

# Set maximum number of attempts
max_attempts = 5
attempts = 0

# Loop until correct password is entered or attemp ran out 
while attempts < max_attempts:
    user_input = input("Enter the password: ")
    if user_input== correct_password:
      print("Access granted. welcome!")
      break
    else:
        attempts += 1
        remaining = max_attempts - attempts
if remaining > 0:
    print(f"Incorrect password. you have {remaining} attempt(s) remaining. ")

else: 
    print(" Maximum attempts reached. The authorities have been alerted ")

# Initialize the list of names
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# Optional: Let the user input the search term
search_name = input("Enter the name you want to search for: ")

# Check if the name exists in the list
if search_name in names:
    print(f"{search_name} was found in the list.")
else:
    print(f"{search_name} was NOT found in the list.")
# Dictionary mapping moth number to number of days
month_days={
   1 : 31, 
   2 : 28,  # Default for February, will adjust for leap year
   3 : 31,
   4 : 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}
# Function to check if a year is a leap year
def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False
# get month input from user 
month = int(input("Enter the month number (1-12): "))
# check if the input is valid 
if month < 1 or month > 12:
 print("invalid number.please enter a number between 1 to 12." )
else: 
 # Check if month is February for leap year adjustment
    if month == 2:
        year = int(input("Enter the year to check for leap year: "))
        if is_leap_year(year):
            print("February has 29 days in a leap year.")
        else:
            print("February has 28 days.")
    else:
        print(f"Month {month} has {month_days[month]} days.")

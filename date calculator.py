#age calculator
from datetime import *
from os import system
system('cls')
print("____________________________________________DATE-CALCULATOR______________________________________")
print()
birth_year=int(input("Enter your year of birth:"))
birth_month=int(input("Enter your month of birth:"))
birth_day=int(input("Enter your day of birth:"))
present_year=(datetime.now()).year
present_month=(datetime.now()).month
present_day=(datetime.now()).day
if((present_day-birth_day)<0):
    present_month=present_month-1
    present_day=present_day+30
if((present_month-birth_month)<0):
    present_year=present_year-1
    present_month=present_month+12
print(f"your age is {present_year-birth_year} year {present_month-birth_month} month and {present_day-birth_day} day")
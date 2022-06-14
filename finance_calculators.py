# Import math module
import math

# Output welcome information with instructions
print("Welcome to the financial calculator. \n")

print("Choose either 'investment' or 'bond' from the menu below to proceed: \n")
print("investment\t - to calculate the amount of interest you'll earn on interest ")
print("bond\t\t - to calculate the amount you'll have to pay on a home loan \n")


# Request choice of investment or bond from user
invest_choice = input("Please make your choice from the menu above (investment or bond) \n").lower()


# Run if investment chosen
if invest_choice == "investment":
    amount = int(input("Please enter the amount of money you want to Invest: \n"))
    int_rate = int(input("Please enter the interest rate (number only, no % sign): \n"))
    int_percent = int_rate / 100
    years = int(input("Please enter the amount of years you will be investing for: \n"))
    interest = input("Would you like to choose Compound or Simple interest? \n").lower()
    

    ## Run if simple interest chosen
    if interest == "simple":
        simp_int = amount * (1 + (int_percent * years))
        print(f"Your total investment after {years} years, with simple interest, will be R{simp_int}")

    ## Run if compound interest chosen
    if interest == "compound":
        comp_int = amount * math.pow((1+int_percent),years)
        print(f"Your total investment after {years} years, compounded annually, will be R{comp_int}")

   


# Run if bond chosen
elif invest_choice == "bond":
    pres_value = int(input("Please enter the Present value of the house: \n"))
    int_rate = int(input("Please enter the interest rate (number only, no % sign): \n"))
    int_percent = (int_rate / 100) / 12
    n_months = int(input("Please enter the number of months you plan to take to repay the house: \n"))
    

    repay_amount = (int_percent* pres_value) / (1 - ((1+int_percent)**(-n_months)))
    print(f"Your monthly repayment will be R{repay_amount}, for {n_months} months ")




# Run if user types investment or bond incorrectly
else:
    print("You have either typed your choice incorrectly or have not chosen from the list: ")


    

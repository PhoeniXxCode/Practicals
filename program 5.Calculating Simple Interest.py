Calculating Simple Interest Write a Python program
 AIM:  to calculate the simple interest based on user input. 
  The program should prompt the user to enter the principal amount, 
  the rate of interest, and the time period in years. It should then compute
   the simple interest using the formula Simple Interest=(Principal×Rate×Time) 100
   and display the result.
  
program :
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the interest rate: "))
time = float(input("Enter the time period in years: "))
interest = (principal * rate * time) / 100
print("Simple Interest:", interest)

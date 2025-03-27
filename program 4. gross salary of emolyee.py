Calculating Gross Salary of an Employee*: 
  Write a Python program to calculate the gross salary of an employee.
 The program should prompt the user for the basic salary (BS) and then compute 
  the dearness allowance (DA) as 70% of BS, the travel allowance (TA) as 30% of BS, 
 and the house rent allowance (HRA) as 10% of BS. Finally, it should calculate the gross salary 
 as the sum of BS, DA, TA, and HRA and display the result.



program:

bs = float(input("Enter the Basic Salary :"))
hra=bs*0.1
da=bs*0.7
ta=bs*0.3
gs=bs + hra + da + ta
print("Gross Salary Rs :", gs)

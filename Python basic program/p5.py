principal = float(input("Enter Principal amount: "))  
rate = float(input("Enter Rate of interest (per annum): "))  
time = float(input("Enter Time (in years): "))  
n = float(input("Enter Number of times interest applied per year: "))  

compound_interest = principal * (1 + rate / (100 * n))**(n * time) - principal  

print("The Compound Interest is:", compound_interest)  

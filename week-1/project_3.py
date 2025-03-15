AP = "Annuity Plan"
PMT = input("Enter Payment amount for annuity? ")
R = input("What is the Annual Interest Rate? ")
T = input("What is the Time Period? ")
n = input("What is the Number of times? ")
A = int(PMT)*((1+(float(R)/int(n))**int(n)*int(T))-1)/(float(R)/int(T))
result = f"Your {AP} = {A}"
print(result)
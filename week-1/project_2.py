CI = "Compound Interest"
P = input("What is the Prinicipal Amount? ")
R = input("What is the Annual Interest Rate? ")
T = input("What is the Time Period? ")
n = input("What is the Number of times? ")
A = int(P)*(1+float(R)/int(n))**(int(n)*int(T))
result = f"Your {CI} = {A}"
print(result)
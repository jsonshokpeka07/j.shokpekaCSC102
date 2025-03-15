SI = "Simple Interest"
P = input("What is the Prinicipal Amount? ")
R = input("What is the Annual Interest Rate? ")
T = input("What is the Time Period? ")
A = int(P)*(1+(float(R)/100)*int(T))
result = f"Your {SI} = {A}"
print(result)
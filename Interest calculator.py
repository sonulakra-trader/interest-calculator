p=float(input("enter principal amount: "))
r=float(input("enter annual interest rate(%): "))
t=float(input("enter time in years: "))
SI=(p*r*t)/100
A=p*(1+r/100)**t
CI=A-p
print("simple interest for",t,"years is",SI)
print("compound interest for",t,"years is",CI)
# Compound Interest calculator
principal = float(input("Enter the principal amount = "))
while principal <= 0:
    principal = float(input("Enter the principal amount = "))
    if principal <= 0:
        print("The principal amount cannot be equal to or less than zero")

time = int(input("Enter the time period (in years) = "))
while time <= 0:
    time = int(input("Enter the time period (in years) = "))
    if time <= 0:
        print("The time period cannot be equal to or less than zero years")

rate = float(input("Enter the rate of interest = "))
while rate <= 0:
    rate = float(input("Enter the rate of interest = "))
    if rate <= 0:
       print("The rate of interest cann500ot be equal to or less than zero")


amount = principal*(1+rate/100)**time
ci = amount - principal
print(f"The amount to be paid after the addition of compound interest is equal to ${amount:.2f}")
print(f"The compound interest after {time} year(s) is equal to ${ci:.2f}")



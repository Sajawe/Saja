principle = 0
rate = 0
Time = 0

while principle <= 0:
    principle = int(input("Enter the principle amount: "))
    if principle <= 0:
        print("Principle can't be less than or equal to zero")

while rate <= 0:
    rate = int(input("Enter the interest rate: "))
    if rate <= 0:
        print("Interest rate can't be less than or equal to zero")

while Time <= 0:
    Time = int(input("Enter the time in years: "))
    if Time <= 0:
        print("Time can't be less than or equal to zero")

total = principle * pow((1 + rate / 100), Time)
print(f"Balance after {Time} year/s: ${total:.2f}")




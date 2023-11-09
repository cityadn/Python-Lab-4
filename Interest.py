def interest(capital, interest_rate, period):
    interest_rate = interest_rate / 100
    simple_interest = capital * interest_rate * period
    return simple_interest

capital = int(input("Enter the capital:\n"))
interest_rate = float(input("Enter the interest rate percentage:\n"))
period = float(input("Enter the period:\n"))
print(interest(capital, interest_rate, period))

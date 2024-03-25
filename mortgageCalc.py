# trying to use excel less
# trying to test something

import matplotlib.pyplot as plt

def calculate_payment(principal, annual_interest_rate, years, payment_frequency):
    if payment_frequency == 'monthly':
        payments_per_year = 12
    elif payment_frequency == 'bi-weekly':
        payments_per_year = 26
    elif payment_frequency == 'weekly':
        payments_per_year = 52
    else:
        raise ValueError("Invalid payment frequency")

    interest_rate_per_period = annual_interest_rate / 100 / payments_per_year
    total_payments = years * payments_per_year
    payment = principal * (interest_rate_per_period * (1 + interest_rate_per_period) ** total_payments) / ((1 + interest_rate_per_period) ** total_payments - 1)
    return payment, total_payments

def calculate_monthly_mortgage(principal, annual_interest_rate, years):
    return calculate_payment(principal, annual_interest_rate, years, 'monthly')[0]

house_price = int(input("Please enter your house purchase price: "))
interest_rate = float(input("Please enter your interest rate: "))
years = int(input("Please enter the mortgage duration (in years): "))

monthly_payment = calculate_monthly_mortgage(house_price, interest_rate, years)
print(f"Monthly Mortgage Payment: ${monthly_payment:.2f}")

# Calculate total payments for different payment frequencies
monthly_total, _ = calculate_payment(house_price, interest_rate, years, 'monthly')
bi_weekly_payment, bi_weekly_total_payments = calculate_payment(house_price, interest_rate, years, 'bi-weekly')
weekly_payment, weekly_total_payments = calculate_payment(house_price, interest_rate, years, 'weekly')

total_monthly = monthly_total * 12 * years
total_bi_weekly = bi_weekly_payment * bi_weekly_total_payments
total_weekly = weekly_payment * weekly_total_payments

# Print total payments
print(f"Total cost with monthly payments: ${total_monthly:.2f}")
print(f"Total cost with bi-weekly payments: ${total_bi_weekly:.2f}")
print(f"Total cost with weekly payments: ${total_weekly:.2f}")

# Plotting the differences
payment_frequencies = ['Monthly', 'Bi-weekly', 'Weekly']
total_costs = [total_monthly, total_bi_weekly, total_weekly]

plt.plot(payment_frequencies, total_costs, marker='o')
plt.ylabel('Total Cost')
plt.title('Total Mortgage Cost by Payment Frequency')
plt.grid(True)
plt.show()



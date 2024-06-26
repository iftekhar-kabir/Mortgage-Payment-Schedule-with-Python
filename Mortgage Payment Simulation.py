import numpy as np
import numpy_financial as npf
import pandas as pd
import matplotlib.pyplot as plt

realestate_price = 200000
downpayment_rate = 0.2
#Input Parameters
Years = 30
period = Years * 12
mortgage_loan = realestate_price - (realestate_price * downpayment_rate)
mortgage_rate = 0.0703
periodic_mortgage_rate = mortgage_rate / 12
periodic_mortgage_payment = npf.pmt(periodic_mortgage_rate, period, -mortgage_loan)
# Initialization
principal_remaining = np.zeros(period + 1) 
principal_remaining[0] = mortgage_loan 

payments = {
    "Period": np.arange(1, period + 1),
    "Payments": periodic_mortgage_payment,
    "Interest Paid": np.zeros(period),
    "Principal Paid": np.zeros(period),
    "Remaining Balance": np.zeros(period)
}
# Amortization Calculation
for i in range(period):
    interest_payment = periodic_mortgage_rate * principal_remaining[i]
    principal_payment = periodic_mortgage_payment - interest_payment

    if principal_remaining[i] < principal_payment:
        principal_payment = principal_remaining[i]

    payments["Interest Paid"][i] = interest_payment
    payments["Principal Paid"][i] = principal_payment
    payments["Remaining Balance"][i] = principal_remaining[i] - principal_payment

    principal_remaining[i + 1] = principal_remaining[i] - principal_payment

df_payments = pd.DataFrame(payments)
print(df_payments)

# Plotting
plt.figure(figsize=(10, 6))

plt.plot(df_payments["Period"], df_payments["Interest Paid"], label="Interest Paid")
plt.plot(df_payments["Period"], df_payments["Principal Paid"], label="Principal Paid")

plt.title("Interest and Principal Payments Over Time")
plt.xlabel("Periods")
plt.ylabel("Amount ($)")
plt.legend()
plt.grid(True)

plt.show()

# Mortgage Payment Simulation

A Python script for simulating mortgage payments over time. The script calculates the amortization schedule for a mortgage, including monthly payments, interest paid, principal paid, and the remaining balance

# Features:
- Calculates monthly mortgage payments based on the loan amount, interest rate, and loan term.
- Generates an amortization schedule showing the breakdown of each payment.
- Visualizes the interest and principal payments over the loan period using matplotlib.
# Usage:
- Clone the repository to your local machine.
- Install the required dependencies (numpy, numpy_financial, pandas, matplotlib).
- Run the mortgage_simulation.py script to generate the amortization schedule and plots.

# Script
```py
import numpy as np
import numpy_financial as npf
import pandas as pd
import matplotlib.pyplot as plt

realestate_price = 200000
downpayment_rate = 0.2

Years = 30
period = Years * 12
mortgage_loan = realestate_price - (realestate_price * downpayment_rate)
mortgage_rate = 0.0703
periodic_mortgage_rate = mortgage_rate / 12
periodic_mortgage_payment = npf.pmt(periodic_mortgage_rate, period, -mortgage_loan)

principal_remaining = np.zeros(period + 1)
principal_remaining[0] = mortgage_loan  

payments = {
    "Period": np.arange(1, period + 1),
    "Payments": periodic_mortgage_payment,
    "Interest Paid": np.zeros(period),
    "Principal Paid": np.zeros(period),
    "Remaining Balance": np.zeros(period)
}

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
#plot
plt.plot(df_payments["Period"],df_payments["Interest Paid"],color="red", 
         label="Interest Paid" )
plt.plot(df_payments["Period"],df_payments["Principal Paid"],color="blue", 
         label="Principal Paid")
plt.title("Interest and Principal Payments Over Time")
plt.xlabel("Periods")
plt.ylabel("Amount ($)")
plt.legend()
plt.show()
```
# Output
```
     Period     Payments  Interest Paid  Principal Paid  Remaining Balance
0         1  1067.709605     937.333333      130.376272      159869.623728
1         2  1067.709605     936.569546      131.140059      159738.483669
2         3  1067.709605     935.801283      131.908322      159606.575347
3         4  1067.709605     935.028521      132.681085      159473.894263
4         5  1067.709605     934.251231      133.458375      159340.435888
..      ...          ...            ...             ...                ...
355     356  1067.709605      30.732762     1036.976843        4209.013867
356     357  1067.709605      24.657806     1043.051799        3165.962068
357     358  1067.709605      18.547261     1049.162344        2116.799724
358     359  1067.709605      12.400918     1055.308687        1061.491037
359     360  1067.709605       6.218568     1061.491037           0.000000
```

![image](https://github.com/iftekhar-kabir/Mortgage-Payment-Schedule-with-Python/assets/163831745/f4aeaed5-ed0a-4a07-83fa-a576b93b295d)

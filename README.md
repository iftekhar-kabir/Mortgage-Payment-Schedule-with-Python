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
```
**Imports**: This section imports the necessary libraries for the script.
- `numpy` and `numpy_financial` are used for mathematical calculations.
- `pandas` is used for data manipulation and analysis.
- `matplotlib.pyplot` is used for plotting graphs.
```py
realestate_price = 200000
downpayment_rate = 0.2

Years = 30
period = Years * 12
mortgage_loan = realestate_price - (realestate_price * downpayment_rate)
mortgage_rate = 0.0703
periodic_mortgage_rate = mortgage_rate / 12
periodic_mortgage_payment = npf.pmt(periodic_mortgage_rate, period, -mortgage_loan)
```
**Input Parameters**: This section defines the input parameters for the mortgage simulation, such as the real estate price, down payment rate, loan term in years, and mortgage interest rate. It then calculates the mortgage loan amount and the periodic mortgage payment using `numpy_financial.pmt()`.
```py
principal_remaining = np.zeros(period + 1)
principal_remaining[0] = mortgage_loan  

payments = {
    "Period": np.arange(1, period + 1),
    "Payments": periodic_mortgage_payment,
    "Interest Paid": np.zeros(period),
    "Principal Paid": np.zeros(period),
    "Remaining Balance": np.zeros(period)
}
```
**Initialization**: This section initializes arrays to store the amortization schedule. `principal_remaining` stores the remaining principal balance for each period, and `payments` is a dictionary to store various payment-related information.
```py
for i in range(period):
    interest_payment = periodic_mortgage_rate * principal_remaining[i]
    principal_payment = periodic_mortgage_payment - interest_payment

    if principal_remaining[i] < principal_payment:
        principal_payment = principal_remaining[i]

    payments["Interest Paid"][i] = interest_payment
    payments["Principal Paid"][i] = principal_payment
    payments["Remaining Balance"][i] = principal_remaining[i] - principal_payment

    principal_remaining[i + 1] = principal_remaining[i] - principal_payment
```
**Amortization Calculation**: This loop calculates the interest and principal payments for each period based on the remaining principal balance. It updates the `payments` dictionary and `principal_remaining` array accordingly.
```py
df_payments = pd.DataFrame(payments)
print(df_payments)
```
**DataFrame Creation**: This section creates a pandas DataFrame (`df_payments`) from the `payments` dictionary for easy viewing and analysis. It prints the DataFrame to the console.
```py
plt.figure(figsize=(10, 6))

plt.plot(df_payments["Period"], df_payments["Interest Paid"], label="Interest Paid")
plt.plot(df_payments["Period"], df_payments["Principal Paid"], label="Principal Paid")

plt.title("Interest and Principal Payments Over Time")
plt.xlabel("Periods")
plt.ylabel("Amount ($)")
plt.legend()
plt.grid(True)

plt.show()
```
**Plotting**: Finally, this section plots the interest and principal payments over time using `matplotlib.pyplot`. It sets the title, labels, and legend for the plot before displaying it.

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

The output dictionary contains the following key-value pairs:

- Period: An array representing the periods (or months) of the mortgage loan, starting from 1.
- Payments: An array containing the constant periodic mortgage payment calculated for each period.
- Interest Paid: An array representing the interest portion of the payment for each period.
- Principal Paid: An array representing the principal portion of the payment for each period.
- Remaining Balance: An array representing the remaining principal balance after each period's payment.

# Plot
![image](https://github.com/iftekhar-kabir/Mortgage-Payment-Schedule-with-Python/assets/163831745/e30d896d-514e-437c-9736-518190c3f93c)

The plot visualizes the interest and principal payments over time during the mortgage loan period. It consists of two lines:

- Interest Paid: Plotted in red, this line represents the amount of interest paid with each mortgage payment over the loan period.
- Principal Paid: Plotted in blue, this line represents the amount of principal paid with each mortgage payment over the loan period.

The x-axis represents the periods (or months) of the mortgage loan, while the y-axis represents the amount of money paid in dollars ($). The plot helps visualize how the interest and principal payments evolve over time, providing insight into the distribution of payments throughout the loan duration.

import numpy as np
import matplotlib.pyplot as plt

def find_payment(loan, rate, months):
    """Calculate fixed monthly payment to pay off loan."""
    if rate == 0:
        return loan / months
    return loan * ((rate * (1 + rate) ** months) / ((1 + rate) ** months - 1))

class EquipmentLoan(object):
    """Abstract class for modeling an engineering equipment loan repayment."""

    def __init__(self, loan, annRate, months):
        self._loan = loan
        self._rate = annRate / 12.0  # monthly interest rate
        self._months = months
        self._paid = [0.0]
        self._outstanding = [loan]
        self._payment = find_payment(loan, self._rate, months)
        self._legend = "Equipment Loan Repayment"

    def make_payment(self):
        """Make a monthly payment and update the outstanding balance."""
        self._paid.append(self._payment)
        reduction = self._payment - self._outstanding[-1] * self._rate
        self._outstanding.append(self._outstanding[-1] - reduction)

    def get_total_paid(self):
        """Return the total amount paid so far."""
        return sum(self._paid)

    def __str__(self):
        return self._legend

    def plot_payments(self, style='b-'):
        """Plot payments over time."""
        plt.plot(self._paid[1:], style, label="Monthly Payment")

    def plot_balance(self, style='r--'):
        """Plot outstanding balance over time."""
        plt.plot(self._outstanding, style, label="Outstanding Balance")

    def plot_tot_pd(self, style='g-.'):
        """Plot total payments made over time."""
        tot_pd = [self._paid[0]]
        for i in range(1, len(self._paid)):
            tot_pd.append(tot_pd[-1] + self._paid[i])
        plt.plot(tot_pd, style, label="Total Paid")

    def plot_net(self, style='m:'):
        """Plot net cost over time."""
        tot_pd = [self._paid[0]]
        for i in range(1, len(self._paid)):
            tot_pd.append(tot_pd[-1] + self._paid[i])
        equity_acquired = np.array([self._loan]*len(self._outstanding))
        equity_acquired = equity_acquired - np.array(self._outstanding)
        net = np.array(tot_pd) - equity_acquired
        plt.plot(net, style, label="Net Cost")

# Example usage for an engineering case:

loan_amount = 50000  # Buying an industrial generator
annual_rate = 0.06   # 6% interest per annum
months = 60          # 5 years repayment

# Create an EquipmentLoan instance
equip_loan = EquipmentLoan(loan_amount, annual_rate, months)

# Simulate monthly payments
for month in range(months):
    equip_loan.make_payment()

# Plot results
plt.figure(figsize=(10, 6))
equip_loan.plot_payments()
equip_loan.plot_balance()
equip_loan.plot_tot_pd()
equip_loan.plot_net()
plt.title("Loan Repayment for Industrial Equipment Purchase")
plt.xlabel("Months")
plt.ylabel("Amount (in Naira)")
plt.legend()
plt.grid(True)
plt.show()

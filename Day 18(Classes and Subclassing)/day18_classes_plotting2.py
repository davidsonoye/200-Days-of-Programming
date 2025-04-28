import matplotlib.pyplot as plt

def plot_mortgages(morts, amt):
    def label_plot(figure, title, x_label, y_label):
        plt.figure(figure)
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.legend(loc='best')

    styles = ['k-', 'k--', 'k:']
    
    # Assign figure numbers
    payments, cost, balance, net_cost = 0, 1, 2, 3

    for i in range(len(morts)):
        plt.figure(payments)
        morts[i].plot_payments(styles[i])
        
        plt.figure(cost)
        morts[i].plot_tot_pd(styles[i])
        
        plt.figure(balance)
        morts[i].plot_balance(styles[i])
        
        plt.figure(net_cost)
        morts[i].plot_net(styles[i])

    label_plot(payments, f'Monthly Payments of ${amt:,} Mortgages', 'Months', 'Monthly Payment ($)')
    label_plot(cost, f'Total Cash Outlay of ${amt:,} Mortgages', 'Months', 'Total Payments ($)')
    label_plot(balance, f'Balance Remaining of ${amt:,} Mortgages', 'Months', 'Remaining Loan Balance ($)')
    label_plot(net_cost, f'Net Cost of ${amt:,} Mortgages', 'Months', 'Net Cost (Payments - Equity) ($)')

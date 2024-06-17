pay_per_hour = float(input("Insert the pay per work hour: "))
work_hours = float(input("Insert how many work hours in the month: "))
income = pay_per_hour * work_hours;
print(
    "\n+------------------------------------+\n"
    f"Work hours: {work_hours:.2f}h \nPay per hour = R$ {pay_per_hour:.2f}\nMonth income: R$ {income:.2f}\n"
    "+------------------------------------+\n"
)

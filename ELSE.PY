actual_cost= float(input("Please Enter the actual Product Price: "))
sale_amount=float(input("Please Enter the Sales Amomunt"))

if (sale_amount > actual_cost):
    amount=sale_amount - actual_cost
    print("Total Profit = {0}".format(amount))
else:
    print("No Profit!!!")
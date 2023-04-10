# Formula 1: Wholesale Price = (Cost of Goods + Shipping and Handling + Sales Tax + (3% * Cost of Goods)) / (1 - 20%)
def wholesale_price_formula1(cost_of_goods, shipping_handling, sales_tax):
    profit_margin = 0.03
    discount = 0.20
    wholesale_price = (cost_of_goods + shipping_handling + sales_tax + (profit_margin * cost_of_goods)) / (1 - discount)
    return wholesale_price

# Formula 2: Wholesale Price = Cost of Goods * (1 + Markup Percentage) + Shipping and Handling + Sales Tax - (10% * Cost of Goods)
def wholesale_price_formula2(cost_of_goods, shipping_handling, sales_tax):
    markup_percentage = 0.30
    discount = 0.10
    wholesale_price = (cost_of_goods * (1 + markup_percentage)) + shipping_handling + sales_tax - (discount * cost_of_goods)
    return wholesale_price

# Taking input from user
cost_of_goods = float(input("Enter the cost of goods: "))
shipping_handling = float(input("Enter the shipping and handling charges: "))
sales_tax = float(input("Enter the sales tax: "))

# Calculating and printing wholesale price using both formulas
wholesale_price_f1 = wholesale_price_formula1(cost_of_goods, shipping_handling, sales_tax)
wholesale_price_f2 = wholesale_price_formula2(cost_of_goods, shipping_handling, sales_tax)

print("Using Formula 1, the wholesale price is: ${:,.2f}".format(wholesale_price_f1))
print("Using Formula 2, the wholesale price is: ${:,.2f}".format(wholesale_price_f2))

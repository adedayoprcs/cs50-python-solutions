def process(Customers_order, Order_completed):
    Order_completed = []

    while Customers_order:
        Processing = Customers_order.pop()
        Order_completed.append(Processing)
        print(Order_completed)
    print("order completed")


Customers_order = ["Pizza", "Burger", "Hamburger"]
Order_completed = []
process(Customers_order, Order_completed)



    

    
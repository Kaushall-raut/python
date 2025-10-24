sales = [
    {"item": "Pen", "qty": 5, "price": 10},
    {"item": "Book", "qty": 3, "price": 50},
    {"item": "Notebook", "qty": 2, "price": 30}
]
total_bill = 0
max_sales_value = 0
max_sales_item = ""

for sale in sales:

    sales_value = sale["qty"] * sale["price"]

    total_bill += sales_value
    
    if sales_value > max_sales_value:
        max_sales_value = sales_value
        max_sales_item = sale["item"]

print(f"Total bill amount: {total_bill}")
print(f"Item with highest sales value: {max_sales_item} (Sales value: {max_sales_value})")

## Scenario
# In this assignment, you will create a simulation of the university cafeteria where customers arrive, purchase items, and leave. The program should track the inventory of the items, simulate customer transactions, and generate a report of the day's sales.

## Tasks:

### 1. Initialize Inventory
#- Create three separate lists to store product information:
#  - `items`: List of product names.
#  - `prices`: List of product prices.
#  - `inventories`: List of product inventories.

import random

# Some example items - feel free tho change them
items = ["Sandwich", "Salad", "Cake"]
prices = [65, 45, 50]
inventories = [100, 50, 100]
cost = [32.2, 22.5, 25.0] 
# Total cost of all items initially purchased for the cafeteria
total_cost = sum(cost[i] * inventories[i] for i in range(len(cost)))
### 2. Simulate Customer Arrivals
'''
- Create a function `simulate_customers`:
  - Simulate a given number of students arriving in the university.
  - For each student, the chance of buying an item at the cafeteria is 50%.
  - For the students that buy an item, randomly select which item it is.
  - Check if there is still inventory for the item available and process the transaction (reduce the inventory, store the sale)

  - The function should return a list `sales` storing all item ids of the performed transactions
'''
num_students = int(input("Enter the number of students arriving at the cafeteria: "))
def simulate_customers(num_students):
    sales = []
    for student in range(num_students):
        if random.random() < 0.5:  # 50% chance to buy
            item_id = random.randint(0, len(items) - 1)
            if inventories[item_id] > 0:
                inventories[item_id] -= 1
                sales.append(item_id)
    return sales
sales = simulate_customers(num_students)
print(f"Number of students who bought items: {len(sales)}")
### 3. Process Sales
'''
- Create a function `process_sales`:
  - Calculate the total revenue from the list of customer transactions (`sales`).`
'''
def process_sales(sales):
    total_revenue = 0
    for item_id in sales:
        total_revenue += prices[item_id]
    return total_revenue
total_revenue = process_sales(sales)
print(f"Total revenue from sales: {total_revenue} kr")

### 4. Generate Sales Report
'''
- Create a function `generate_report`:
  - Print a summary of the day's sales, including total revenue and remaining inventory.
'''
def generate_report(total_revenue):
    print("=== Cafeteria Sales Report ===")
    print(f"Total Revenue: {total_revenue} kr")
    print("Remaining Inventory:")
    for i in range(len(items)):
        print(f"  {items[i]}: {inventories[i]} remaining")
    print("==============================")
generate_report(total_revenue)

# Cost of all items minus the total revenue
# The cost needs to include the not sold items as well
# Assuming a fixed cost for each item for simplicity


profit = total_revenue - total_cost
print(f"Total profit for the day: {profit} kr")
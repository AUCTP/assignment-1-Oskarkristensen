## Scenario
# In this assignment, you will create a simulation of the university cafeteria where customers arrive, purchase items, and leave. The program should track the inventory of the items, simulate customer transactions, and generate a report of the day's sales.

## Tasks:

### 1. Initialize Inventory
#- Create three separate lists to store product information:
#  - `items`: List of product names.
#  - `prices`: List of product prices.
#  - `inventories`: List of product inventories.

import random

items = ["Sandwich", "Salad", "Cake"]
prices = [65, 45, 50]
inventories = [100, 50, 100]
cost = [p / 2 for p in prices] 
total_cost = sum(cost[i] * inventories[i] for i in range(len(cost)))

### 2. Simulate Customer Arrivals

num_students = int(input("Number of students arriving at the cafeteria: "))
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
print("=== Cafeteria Sales Report ===")
print(f"Number of students who bought items: {len(sales)}")
### 3. Process Sales
def process_sales(sales):
    total_revenue = 0
    for item_id in sales:
        total_revenue += prices[item_id]
    return total_revenue
total_revenue = process_sales(sales)
print(f"Total revenue from sales: {total_revenue} kr")

### 4. Generate Sales Report

def generate_report(total_revenue):
    print(f"Total Revenue: {total_revenue} kr")
    print("Remaining Inventory:")
    for i in range(len(items)):
        print(f"  {items[i]}: {inventories[i]} remaining")
generate_report(total_revenue)

### 5. Calculate Profit
def calculate_profit(total_revenue, total_cost):
    profit = total_revenue - total_cost
    return profit
profit = calculate_profit(total_revenue, total_cost)
print(f"Total profit for the day: {profit} kr")
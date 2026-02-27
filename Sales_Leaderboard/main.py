import pandas as pd

# Dataset
sales = pd.DataFrame({
    "customer": ["Ali", "Sara", "Omar", "Ali", "Sara", "Omar", "Ali", "Sara"],
    "product": ["Book", "Pen", "Notebook", "Notebook", "Book", "Pen", "Pen", "Notebook"],
    "quantity": [2, 10, 3, 1, 4, 5, 2, 3],
    "price": [120, 5, 50, 50, 120, 5, 5, 50]
})

# Step 1: Total per order
sales['total'] = sales['quantity'] * sales['price']

# Step 2: Total revenue per customer
customer_revenue = sales.groupby('customer')['total'].sum().reset_index()

# Step 3: Add rank (highest revenue = rank 1)
customer_revenue['rank'] = customer_revenue['total'].rank(method='dense', ascending=False)

# Step 4: Sort descending by revenue
customer_leaderboard = customer_revenue.sort_values('total', ascending=False).reset_index(drop=True)

# Show leaderboard
print(customer_leaderboard)
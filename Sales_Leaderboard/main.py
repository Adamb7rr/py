import pandas as pd

# Dataset
sales = pd.DataFrame({
    "customer": ["Ali", "Sara", "Omar", "Ali", "Sara", "Omar", "Ali", "Sara"],
    "product": ["Book", "Pen", "Notebook", "Notebook", "Book", "Pen", "Pen", "Notebook"],
    "quantity": [2, 10, 3, 1, 4, 5, 2, 3],
    "price": [120, 5, 50, 50, 120, 5, 5, 50]
})

sales['total'] = sales['quantity'] * sales['price']


customer_revenue = sales.groupby('customer')['total'].sum().reset_index()


customer_revenue['rank'] = customer_revenue['total'].rank(method='dense', ascending=False)


customer_leaderboard = customer_revenue.sort_values('total', ascending=False).reset_index(drop=True)


print(customer_leaderboard)

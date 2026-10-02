# --------------------------------------------------
# CUSTOMER ORDER DATA
# --------------------------------------------------

customers = [
    "Alice",
    "Bob",
    "Charlie",
    "David",
    "Emma",
    "Frank"
]

# Order format:
# (customer_name, product, price, category)

orders = [
    ("Alice", "Laptop", 850, "Electronics"),
    ("Alice", "T-Shirt", 25, "Clothing"),
    ("Bob", "Headphones", 80, "Electronics"),
    ("Bob", "Jeans", 60, "Clothing"),
    ("Charlie", "Coffee Maker", 70, "Home Essentials"),
    ("Charlie", "T-Shirt", 25, "Clothing"),
    ("David", "Smartphone", 500, "Electronics"),
    ("David", "Headphones", 80, "Electronics"),
    ("Emma", "T-Shirt", 25, "Clothing"),
    ("Emma", "Lamp", 45, "Home Essentials"),
    ("Frank", "Keyboard", 40, "Electronics"),
    ("Frank", "Notebook", 15, "Home Essentials")
]

customer_orders = {
    "Alice": ["Laptop", "T-Shirt"],
    "Bob": ["Headphones", "Jeans"],
    "Charlie": ["Coffee Maker", "T-Shirt"],
    "David": ["Smartphone", "Headphones"],
    "Emma": ["T-Shirt", "Lamp"],
    "Frank": ["Keyboard", "Notebook"]
}

product_categories = {
    "Laptop": "Electronics",
    "T-Shirt": "Clothing",
    "Headphones": "Electronics",
    "Jeans": "Clothing",
    "Coffee Maker": "Home Essentials",
    "Smartphone": "Electronics",
    "Lamp": "Home Essentials",
    "Keyboard": "Electronics",
    "Notebook": "Home Essentials"
}
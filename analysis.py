# --------------------------------------------------
# CUSTOMER ORDER ANALYSIS
# --------------------------------------------------

def calculate_customer_spending(customers, orders):
    customer_spending = {}

    for customer in customers:
        total_spending = 0

        for order in orders:
            order_customer, product, price, category = order

            if order_customer == customer:
                total_spending += price

        customer_spending[customer] = total_spending

    return customer_spending


def classify_customers(customer_spending):
    customer_classification = {}

    for customer, spending in customer_spending.items():

        if spending > 100:
            classification = "High-Value Buyer"
        elif spending >= 50:
            classification = "Moderate Buyer"
        else:
            classification = "Low-Value Buyer"

        customer_classification[customer] = classification

    return customer_classification


def calculate_category_revenue(orders):
    category_revenue = {}

    for order in orders:
        customer, product, price, category = order

        if category not in category_revenue:
            category_revenue[category] = 0

        category_revenue[category] += price

    return category_revenue


def get_unique_products(orders):
    unique_products = set()

    for order in orders:
        product = order[1]
        unique_products.add(product)

    return unique_products


def get_electronics_customers(orders):
    electronics_customers = list(dict.fromkeys([
        order[0]
        for order in orders
        if order[3] == "Electronics"
    ]))

    return electronics_customers


def get_top_customers(customer_spending, count=3):
    return sorted(
        customer_spending.items(),
        key=lambda item: item[1],
        reverse=True
    )[:count]

def get_multi_category_customers(orders):
    customer_categories = {}

    for order in orders:
        customer, product, price, category = order

        if customer not in customer_categories:
            customer_categories[customer] = set()

        customer_categories[customer].add(category)

    multi_category_customers = {
        customer: categories
        for customer, categories in customer_categories.items()
        if len(categories) > 1
    }

    return multi_category_customers

def get_electronics_and_clothing_customers(orders):
    electronics_customers = set()
    clothing_customers = set()

    for order in orders:
        customer, product, price, category = order

        if category == "Electronics":
            electronics_customers.add(customer)

        elif category == "Clothing":
            clothing_customers.add(customer)

    return electronics_customers & clothing_customers

def get_product_purchase_frequency(orders):
    product_frequency = {}

    for order in orders:
        product = order[1]

        if product not in product_frequency:
            product_frequency[product] = 0

        product_frequency[product] += 1

    return product_frequency

def get_most_purchased_products(product_frequency):
    return sorted(
        product_frequency.items(),
        key=lambda item: item[1],
        reverse=True
    )

def demonstrate_dictionary_operations(customer_orders):
    # Retrieve a customer's products using get()
    alice_products = customer_orders.get("Alice", [])

    # Create a copy so the original data is not changed
    updated_customer_orders = {
        customer: products.copy()
        for customer, products in customer_orders.items()
    }

    # Modify a customer record using setdefault()
    updated_customer_orders.setdefault("Alice", []).append("Mouse")

    return alice_products, updated_customer_orders

def generate_business_insights(
    customer_spending,
    category_revenue,
    product_frequency,
    customer_classification,
    electronics_clothing_customers
):
    total_revenue = sum(category_revenue.values())

    highest_revenue_category = max(
        category_revenue,
        key=category_revenue.get
    )

    most_purchased_product = max(
        product_frequency,
        key=product_frequency.get
    )

    high_value_customers = [
        customer
        for customer, classification in customer_classification.items()
        if classification == "High-Value Buyer"
    ]

    return {
        "total_revenue": total_revenue,
        "highest_revenue_category": highest_revenue_category,
        "highest_category_revenue": category_revenue[
            highest_revenue_category
        ],
        "most_purchased_product": most_purchased_product,
        "most_purchased_count": product_frequency[
            most_purchased_product
        ],
        "high_value_customers": high_value_customers,
        "electronics_clothing_customers": electronics_clothing_customers
    }
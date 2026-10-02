from data import (
    customers,
    orders,
    customer_orders,
    product_categories
)

from analysis import (
    calculate_customer_spending,
    classify_customers,
    calculate_category_revenue,
    get_unique_products,
    get_electronics_customers,
    get_top_customers,
    get_multi_category_customers,
    get_electronics_and_clothing_customers,
    get_product_purchase_frequency,
    get_most_purchased_products,
    demonstrate_dictionary_operations,
    generate_business_insights
)


# --------------------------------------------------
# 1. CUSTOMER ORDERS
# --------------------------------------------------

print("CUSTOMER ORDERS")
print("=" * 50)

for customer, products in customer_orders.items():
    print(f"{customer}: {', '.join(products)}")


# --------------------------------------------------
# 2. DICTIONARY OPERATIONS
# --------------------------------------------------

alice_products, updated_customer_orders = (
    demonstrate_dictionary_operations(customer_orders)
)

print("\nDICTIONARY OPERATIONS")
print("=" * 50)

print(f"Alice's products: {', '.join(alice_products)}")
print(
    f"Alice's updated products: "
    f"{', '.join(updated_customer_orders['Alice'])}"
)

# --------------------------------------------------
# 2. PRODUCT CATEGORIES
# --------------------------------------------------

categories = set(product_categories.values())

print("\nPRODUCT CATEGORIES")
print("=" * 50)

for category in categories:
    print(category)


# --------------------------------------------------
# 3. CUSTOMER SPENDING & CLASSIFICATION
# --------------------------------------------------

customer_spending = calculate_customer_spending(
    customers,
    orders
)

customer_classification = classify_customers(
    customer_spending
)

print("\nCUSTOMER SPENDING & CLASSIFICATION")
print("=" * 50)

for customer in customers:
    print(
        f"{customer}: ${customer_spending[customer]} "
        f"-> {customer_classification[customer]}"
    )


# --------------------------------------------------
# 4. CATEGORY REVENUE
# --------------------------------------------------

category_revenue = calculate_category_revenue(orders)

print("\nREVENUE BY PRODUCT CATEGORY")
print("=" * 50)

for category, revenue in category_revenue.items():
    print(f"{category}: ${revenue}")


# --------------------------------------------------
# 5. UNIQUE PRODUCTS
# --------------------------------------------------

unique_products = get_unique_products(orders)

print("\nUNIQUE PRODUCTS")
print("=" * 50)

for product in unique_products:
    print(product)


# --------------------------------------------------
# 6. ELECTRONICS CUSTOMERS
# --------------------------------------------------

electronics_customers = get_electronics_customers(orders)

print("\nCUSTOMERS WHO PURCHASED ELECTRONICS")
print("=" * 50)

for customer in electronics_customers:
    print(customer)


# --------------------------------------------------
# 7. TOP 3 CUSTOMERS
# --------------------------------------------------

top_customers = get_top_customers(
    customer_spending
)

print("\nTOP 3 HIGHEST-SPENDING CUSTOMERS")
print("=" * 50)

for customer, spending in top_customers:
    print(f"{customer}: ${spending}")

# --------------------------------------------------
# 8. MULTI-CATEGORY CUSTOMERS
# --------------------------------------------------

multi_category_customers = get_multi_category_customers(orders)

print("\nCUSTOMERS WHO PURCHASED FROM MULTIPLE CATEGORIES")
print("=" * 50)

for customer, categories in multi_category_customers.items():
    print(f"{customer}: {', '.join(categories)}")


# --------------------------------------------------
# 9. ELECTRONICS & CLOTHING CUSTOMERS
# --------------------------------------------------

electronics_clothing_customers = (
    get_electronics_and_clothing_customers(orders)
)

print("\nCUSTOMERS WHO BOUGHT ELECTRONICS AND CLOTHING")
print("=" * 50)

for customer in electronics_clothing_customers:
    print(customer)


# --------------------------------------------------
# 10. PRODUCT PURCHASE FREQUENCY
# --------------------------------------------------

product_frequency = get_product_purchase_frequency(orders)

most_purchased_products = get_most_purchased_products(
    product_frequency
)

print("\nPRODUCT PURCHASE FREQUENCY")
print("=" * 50)

for product, count in most_purchased_products:
    print(f"{product}: {count} purchase(s)")

# --------------------------------------------------
# 12. BUSINESS INSIGHTS
# --------------------------------------------------

business_insights = generate_business_insights(
    customer_spending,
    category_revenue,
    product_frequency,
    customer_classification,
    electronics_clothing_customers
)

print("\nBUSINESS INSIGHTS")
print("=" * 50)

print(
    f"Total Revenue: "
    f"${business_insights['total_revenue']}"
)

print(
    f"Highest Revenue Category: "
    f"{business_insights['highest_revenue_category']} "
    f"(${business_insights['highest_category_revenue']})"
)

print(
    f"Most Frequently Purchased Product: "
    f"{business_insights['most_purchased_product']} "
    f"({business_insights['most_purchased_count']} purchases)"
)

print(
    "High-Value Customers: "
    f"{', '.join(business_insights['high_value_customers'])}"
)

print(
    "Customers Buying Both Electronics and Clothing: "
    f"{', '.join(business_insights['electronics_clothing_customers'])}"
)
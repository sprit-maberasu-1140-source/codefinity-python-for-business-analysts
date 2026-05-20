def top_products_by_revenue(summary_dict):
    # Write your code here
    pass
    sorted_products = sorted(summary_dict.items(), key=lambda x:x[1],reverse=True)
    top_3 = [product for product, revenue in sorted_products[:3]]
    return top_3
    

# Sample calls
summary_dict = {
    "Product A": 15000,
    "Product B": 22000,
    "Product C": 18000,
    "Product D": 9000,
    "Product E": 12000
}
result = top_products_by_revenue(summary_dict)
print(result)

summary_dict2 = {
    "Gadget": 5000,
    "Widget": 7000,
    "Thingamajig": 3000
}
result2 = top_products_by_revenue(summary_dict2)
print(result2)

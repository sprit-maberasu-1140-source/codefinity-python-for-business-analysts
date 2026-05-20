import matplotlib.pyplot as plt

def plot_sales_performance(summary_dict):
    product_names = list(summary_dict.keys())
    revenues = list(summary_dict.values())
    plt.figure(figsize=(8, 5))
    bars = plt.bar(product_names, revenues, color='skyblue')
    plt.title("Product Sales Performance")
    plt.xlabel("Product")
    plt.ylabel("Revenue")
    for bar, revenue in zip(bars, revenues):
        label = str(revenue)
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), label, ha='center', va='bottom')
    plt.tight_layout()
    plt.show()

summary_dict = {"Widget": 15000, "Gadget": 12000, "Doohickey": 9000}
plot_sales_performance(summary_dict)
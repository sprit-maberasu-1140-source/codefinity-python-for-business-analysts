def summarize_products(sales_records):
    summary = {}
    for record in sales_records:
        product = record['product']
        units = record['units_sold']
        revenue = record['revenue']
        if product not in summary:
            summary[product] = {'units_sold': 0, 'revenue': 0}
        summary[product]['units_sold'] += units
        summary[product]['revenue']  += revenue
    return summary
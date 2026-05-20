def clean_sales_data(sales_records):
    cleaned_records = []
    for record in sales_records:
        cleaned_record = record.copy()
        if cleaned_record.get('units_sold') is None:
            cleaned_record['units_sold'] =0
        if cleaned_record.get('revenue') is None:
            cleaned_record['revenue'] = 0
        if 'product' in cleaned_record and isinstance(cleaned_record['product'],str):
            cleaned_record['product'] = cleaned_record['product'].title()
        cleaned_records.append(cleaned_record)
    return cleaned_records
            

sales_data = [
    {'date': '2024-06-01', 'product': 'laptop', 'units_sold': 10, 'revenue': 15000},
    {'date': '2024-06-02', 'product': 'Laptop', 'units_sold': None, 'revenue': 14500},
    {'date': '2024-06-03', 'product': 'tablet', 'units_sold': 5, 'revenue': None},
    {'date': '2024-06-04', 'product': 'SMARTphone', 'units_sold': None, 'revenue': None},
]

cleaned_sales = clean_sales_data(sales_data)
print(cleaned_sales)

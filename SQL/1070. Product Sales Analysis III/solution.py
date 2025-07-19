import pandas as pd

def sales_analysis(sales: pd.DataFrame) -> pd.DataFrame:
    min_years = sales.groupby(by='product_id',as_index=False).agg(year=('year','min'))
    print(min_years)
    merged_sales = sales.merge(min_years,how='inner',on=['product_id','year',]).rename(columns={
        'product_id_x': 'product_id',
        'year':'first_year'
    })
    print(merged_sales)
    return(merged_sales[['product_id','first_year','quantity','price']])
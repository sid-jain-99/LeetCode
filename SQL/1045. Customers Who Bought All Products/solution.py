import pandas as pd

def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    product_count = product['product_key'].nunique()
    grp_cust = customer.groupby(by='customer_id',as_index=False).agg(prod_cnt = ('product_key','nunique'))
    return grp_cust.loc[grp_cust['prod_cnt']==product_count,['customer_id']]
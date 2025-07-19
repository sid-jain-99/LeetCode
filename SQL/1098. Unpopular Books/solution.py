
import pandas as pd

def unpopular_books(books: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    unpop_books = orders[orders['dispatch_date']>=pd.to_datetime('2019-06-23')-pd.DateOffset(years=1)].groupby(by='book_id',as_index=False)['quantity'].sum().query('quantity>=10')
    
    filt_1 = (books['available_from']< pd.to_datetime('2019-06-23')-pd.DateOffset(months=1))
    filt_2 = (books['book_id'].isin(unpop_books['book_id']))
    return books.loc[filt_1 & ~filt_2,['book_id','name']]
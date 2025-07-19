import pandas as pd

def swap(id,count):
    # id = row['id']
    if id%2 !=0:
        if id != count:
            id+=1
    else:
        id-=1
    return id    


def exchange_seats(seat: pd.DataFrame) -> pd.DataFrame:
    count = seat['id'].count()
    print(count)
    seat['id'] = seat['id'].apply(lambda row: swap(row,count) )
    print(seat)
    seat.sort_values(by='id',inplace=True)
    return seat
    
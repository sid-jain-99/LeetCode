import pandas as pd

def new_users_daily_count(traffic: pd.DataFrame) -> pd.DataFrame:
    df = traffic[traffic['activity']=='login']
    first_login = df.groupby('user_id', as_index=False)['activity_date'].min()
    print(first_login)
    first_login = first_login[first_login.activity_date.between(pd.to_datetime('2019-06-30')- timedelta(days=90),pd.to_datetime('2019-06-30'))]
    final = first_login.groupby('activity_date', as_index=False).agg(user_count=('user_id','count')).rename(columns={
        'activity_date': 'login_date'
    })
    return final
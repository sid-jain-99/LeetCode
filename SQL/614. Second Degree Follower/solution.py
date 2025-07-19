import pandas as pd

def second_degree_follower(follow: pd.DataFrame) -> pd.DataFrame:
    filt1 = follow['followee'].isin(follow['follower'])
    filtered = follow[filt1].groupby(by='followee',as_index=False).agg(num=('followee','count'))
    filtered.sort_values(by='followee',inplace=True)
    filtered.rename(columns={
        'followee': 'follower'
    },inplace=True)
    print(filtered)
    return(filtered)

    
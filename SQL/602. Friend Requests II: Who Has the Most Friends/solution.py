import pandas as pd

def most_friends(request_accepted: pd.DataFrame) -> pd.DataFrame:
    filtered = pd.concat([request_accepted['requester_id'],request_accepted['accepter_id']]).to_frame('id')
    filtered = filtered.groupby('id',as_index=False).agg(num=('id','count'))
    filtered.sort_values('num',inplace=True,ascending=False)
    return filtered.head(1)
    
import pandas as pd

def find_investments(insurance: pd.DataFrame) -> pd.DataFrame:
    insurance = insurance.assign(
        tiv_2015_cnt = insurance.groupby('tiv_2015')['pid'].transform('count'),
        loc_cnt = insurance.groupby(['lat', 'lon'])['pid'].transform('count')
    )
    print(insurance)

    filtered = insurance[(insurance['loc_cnt']==1)&(insurance['tiv_2015_cnt']>1)].agg(tiv_2016 = ('tiv_2016',sum)).round(2)
    return filtered
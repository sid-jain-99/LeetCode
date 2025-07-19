import pandas as pd
import numpy as np

def shortest_distance(point2_d: pd.DataFrame) -> pd.DataFrame:
    merged = point2_d.merge(point2_d, how='cross',suffixes=("_1","_2"))
    merged['shortest'] = np.sqrt(((merged['x_2']-merged['x_1'])**2)+((merged['y_2']-merged['y_1']))**2)
    merged = merged[merged['shortest']>0]
    return pd.DataFrame({'shortest': [round(merged['shortest'].min(), 2)]})
    
import pandas as pd

def project_employees(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    merged_df = project.merge(employee, how='inner', on= 'employee_id')
    merged_df['ranked_exp'] = merged_df.groupby('project_id')['experience_years'].rank(method='min',ascending=False)
    print(merged_df)
    return merged_df.loc[merged_df['ranked_exp']==1,['project_id','employee_id']]
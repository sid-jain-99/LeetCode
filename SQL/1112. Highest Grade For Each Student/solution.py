import pandas as pd

def highest_grade(enrollments: pd.DataFrame) -> pd.DataFrame:
    enrollments = enrollments.sort_values(by=['student_id','grade','course_id'],ascending=[True,False,True])
    enrollments['course_rank']= enrollments.groupby('student_id')[['grade']].rank(method='first',ascending=False)
    print(enrollments)

    return enrollments.loc[enrollments['course_rank']==1,['student_id','course_id','grade']].sort_values('student_id')
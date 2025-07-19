-- Write your PostgreSQL query statement below
with min_login_dt_by_user as (
    select user_id, min(activity_date) as min_date
    from traffic
    where activity = 'login'
    group by user_id
)select min_date as login_date, count(user_id) as user_count
from min_login_dt_by_user
where min_date >= to_date('2019-06-30','YYYY-MM-DD')- INTERVAL '90 days'
group by min_date
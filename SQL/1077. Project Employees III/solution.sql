-- Write your PostgreSQL query statement below
select project_id, employee_id
from(
    select project_id, project.employee_id, 
RANK() over( partition by project_id order  by experience_years desc) as exp_rank
from project join employee
on project.employee_id = employee.employee_id
) AS RANKED_EMP
where exp_rank=1


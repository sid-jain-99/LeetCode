-- Write your PostgreSQL query statement below
select student_id, course_id, grade 
from(
    select student_id, course_id, grade,
RANK() over(partition by student_id order by grade desc, course_id) as course_rank
from enrollments
) x
where course_rank = 1
order by student_id

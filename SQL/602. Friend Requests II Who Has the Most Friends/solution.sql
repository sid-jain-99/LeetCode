select id, count(id) num
from(
    select requester_id as id 
    from RequestAccepted
    union all
    select accepter_id as id 
    from RequestAccepted
)group by id order by count(id) desc
limit 1
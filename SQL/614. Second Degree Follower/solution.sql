select followee as follower, count(*) as num
from follow 
where followee in (select followee from follow) 
and followee in (select follower from follow)
group by followee
order by followee
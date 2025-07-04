-- Write your PostgreSQL query statement below
-- select distinct tiv_2015
-- from insurance
-- group by tiv_2015
-- having count(distinct pid)>1

-- select concat(lat,',',lon) as lat_lon
-- from insurance
-- group by concat(lat,',',lon)
-- having count(distinct pid) = 1

-- select round(cast(sum(tiv_2016)as numeric),2) as tiv_2016
-- from insurance i join (
--     select distinct tiv_2015
--     from insurance
--     group by tiv_2015
--     having count(distinct pid)>1
-- ) tiv
-- on i.tiv_2015 = tiv.tiv_2015
-- join (select concat(lat,',',lon) as lat_lon
-- from insurance
-- group by concat(lat,',',lon)
-- having count(distinct pid) = 1) la
-- on concat(i.lat,',',i.lon) = la.lat_lon

select round(cast(sum(tiv_2016) as numeric),2)as tiv_2016
from(
select *,
count(*) over (partition by tiv_2015) as tiv_count,
count(*) over (partition by lat,lon) as lat_lon_cnt
from insurance) as ins
where tiv_count>1 and lat_lon_cnt = 1

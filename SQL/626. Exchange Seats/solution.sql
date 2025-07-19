-- Write your PostgreSQL query statement below
select
(case
    when mod(id,2)!=0 and counts!=id then id+1
    when mod(id,2)!=0 and counts=id then id
    else id-1
 END) as id, student
    from seat, (select count(*) as counts from seat) as seat_count
    order by id asc;
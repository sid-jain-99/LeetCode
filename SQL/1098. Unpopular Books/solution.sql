-- Write your PostgreSQL query statement below
with unpop_books as (
    select book_id
    from orders
    where dispatch_date>=  to_date('2019-06-23', 'YYYY-MM-DD') - INTERVAL '1 year'
    group by book_id
    having sum(quantity)>=10
)select book_id,name
from books
where book_id not in (select book_id from unpop_books)
and available_from < to_date('2019-06-23', 'YYYY-MM-DD') - INTERVAL '1 month'
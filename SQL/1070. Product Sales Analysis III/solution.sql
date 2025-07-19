
select product_id, year as first_year, quantity, price
from sales as out_sales
where year = (
    select min(year) from sales in_sales where in_sales.product_id = out_sales.product_id 
)

-- faster solution
select product_id, year as first_year, quantity, price
from sales as out_sales
where (product_id,year) in (
    select product_id, min(year) from sales group by product_id
)
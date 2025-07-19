with c as (
    select a.x as x1, a.y as y1, b.x as x2, b.y as y2
    from point2d a, point2d b
) select ROUND(MIN(|/(((x2-x1)^2)+((y2-y1)^2)))::numeric,2) as shortest from c
where |/(((x2-x1)^2)+((y2-y1)^2))>0
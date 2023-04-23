with
    salesData as (
        select
            extract(year from saleDate) as saleYear
            product
        from
            sales
    )
select
    saleYear,
    product
from
    salesData;

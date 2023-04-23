with
    -- This is camel case
    camelCase as (
        select
            *
        from
            `camelCaseTable`
        where
            1 = 1
    ),
    -- This is snake case
    snake_case as (
        select
            *
        from
            `snake_case_table_1`
        union all
        select
            *
        from
            `snake_case_table_2`
    ),
    -- This is kebab case
    connected_table as (
        select
            *
        from
            camelCase
            left join snake_case on camelCase.id = snake_case.id
            right join left_table on camelCase.id = left_table.id
    )
select
    *
from
    connected_table
limit
    10

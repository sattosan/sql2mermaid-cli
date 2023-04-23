with
    bar as (
        select
            *
        from
            baz
    )
select
    *
from
    foo
    inner join bar on foo.id = bar.id

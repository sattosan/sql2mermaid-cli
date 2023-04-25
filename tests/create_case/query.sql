CREATE
OR
REPLACE TEMP
TABLE HOGE AS (
        SELECT
            hoge_id hoge_name
        FROM hoge
    );

CREATE TABLE fuga AS (
        SELECT fuga
        FROM BAR
            INNER JOIN BAZ ON BAR.bar_id = BAZ.bar_id
            LEFT JOIN HOGE ON BAR.hoge_id = BAZ.hoge_id
        WHERE
            BAR.hoge_name = "hoge"
    );

SELECT COUNT(*) FROM fuga;

CREATE OR REPLACE TEMP TABLE HOGE AS (
  SELECT
      hoge_id
      hoge_name
  FROM
      hoge
);

CREATE TABLE ${env}.fuga.${timestamp_suffix} AS (
  SELECT fuga
  FROM _SESSION.BAR
  INNER JOIN _SESSION.BAZ ON BAR.bar_id = BAZ.bar_id
  LEFT JOIN _SESSION.HOGE ON BAR.hoge_id = BAZ.hoge_id
  WHERE BAR.hoge_name = "hoge"
);

SELECT COUNT(*) FROM ${env}.fuga.${timestamp_suffix};

-- 2-fans.sql
-- Rank country origins of bands by total (non-unique) fans

SELECT
  origin,
  SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;

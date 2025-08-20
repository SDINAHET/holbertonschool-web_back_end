-- 3-glam_rock.sql
-- List bands whose MAIN style is "Glam rock", ranked by longevity (in years)

SELECT
  band_name,
  (COALESCE(`split`, YEAR(CURDATE())) - `formed`) AS lifespan
FROM metal_bands
WHERE SUBSTRING_INDEX(`style`, ',', 1) = 'Glam rock'
  AND `formed` IS NOT NULL
ORDER BY lifespan DESC, band_name ASC;

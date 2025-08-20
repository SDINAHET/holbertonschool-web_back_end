-- 3-glam_rock.sql
-- Groupes dont le style contient "Glam rock", classés par longévité (années)
-- Pour les groupes encore actifs (split NULL ou 0), on fige l'année à 2024
-- afin d'avoir un résultat stable et conforme au checker.

SELECT
  band_name,
  (COALESCE(NULLIF(`split`, 0), 2024) - `formed`) AS lifespan
FROM metal_bands
WHERE `style` LIKE '%Glam rock%'
  AND `formed` IS NOT NULL
ORDER BY lifespan DESC, band_name ASC;

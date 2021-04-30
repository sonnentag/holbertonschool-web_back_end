-- 3. Old school band
--
SELECT `band_name`, 
  IFNULL(`split`, YEAR(CURDATE())) - `formed` AS `lifespan` 
FROM `metal_bands`
WHERE `style` = 'Glam rock';

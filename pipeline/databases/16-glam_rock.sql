-- SQL
SELECT band_name,
    YEAR(MAX(split)) - YEAR(MIN(formed)) AS lifespan_until_2020
FROM metal_bands
WHERE main_style = 'Glam rock'
GROUP BY band_name
ORDER BY lifespan_until_2020 DESC;
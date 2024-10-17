-- SQL script that lists ALL bands WITH Glam rock AS their main style, ranked by their longevity
SELECT
    band_name,
    (IFNULL(split, 2022) - formed) AS lifespan
FROM
    metal_bands
WHERE
    style LIKE "%Glam rock%"
ORDER BY
    lifespan DESC;
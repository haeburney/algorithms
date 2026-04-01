SELECT
    I.FOOD_TYPE,
    I.REST_ID,
    I.REST_NAME,
    I.FAVORITES
FROM 
    REST_INFO I
WHERE
    (I.FAVORITES, I.FOOD_TYPE) IN (
        SELECT 
            MAX(I2.FAVORITES), 
            I2.FOOD_TYPE
        FROM 
            REST_INFO I2
        GROUP BY 
            I2.FOOD_TYPE
    )
ORDER BY 
    I.FOOD_TYPE DESC
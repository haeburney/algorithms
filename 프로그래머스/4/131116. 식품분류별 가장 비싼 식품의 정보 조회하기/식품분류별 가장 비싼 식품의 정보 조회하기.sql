SELECT 
    F.CATEGORY, 
    F.PRICE,
    F.PRODUCT_NAME
FROM
    FOOD_PRODUCT F
WHERE 
    F.PRICE = (
        SELECT 
            MAX(F2.PRICE)
        FROM 
            FOOD_PRODUCT F2
        WHERE 
            F.CATEGORY = F2.CATEGORY
        GROUP BY CATEGORY
    ) 
    AND F.CATEGORY IN ( '과자', '국', '김치', '식용유')
ORDER BY F.PRICE DESC
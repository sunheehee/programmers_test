-- 코드를 작성해주세요
WITH GRADE AS (
    SELECT CASE
        WHEN SKILL_CODE & (SELECT SUM(CODE) FROM SKILLCODES WHERE CATEGORY = 'FRONT END') > 0 
        AND SKILL_CODE & (SELECT SUM(CODE) FROM SKILLCODES WHERE NAME = 'Python') > 0 THEN 'A' 
        WHEN SKILL_CODE & (SELECT SUM(CODE) FROM SKILLCODES WHERE NAME = 'C#') > 0 THEN 'B'
        WHEN SKILL_CODE & (SELECT SUM(CODE) FROM SKILLCODES WHERE CATEGORY = 'FRONT END') > 0 THEN 'C'
        END AS GRADE,
    ID,
    EMAIL
    FROM DEVELOPERS
    )

SELECT *
FROM GRADE
WHERE GRADE IS NOT NULL
ORDER BY GRADE, ID;
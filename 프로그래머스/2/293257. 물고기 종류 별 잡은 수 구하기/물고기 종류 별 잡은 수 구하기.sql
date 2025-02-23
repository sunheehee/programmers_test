-- 코드를 작성해주세요
SELECT COUNT(I.FISH_TYPE) AS FISH_COUNT, FISH_NAME
FROM FISH_INFO I
JOIN FISH_NAME_INFO N
ON I.FISH_TYPE = N.FISH_TYPE
GROUP BY I.FISH_TYPE, FISH_NAME
ORDER BY FISH_COUNT DESC


----------------------------------------------------------------------

🌱오답노트

SELECT COUNT(I.FISH_TYPE) AS FISH_COUNT, FISH_NAME
FROM FISH_INFO I
JOIN FISH_NAME_INFO N
ON I.FISH_TYPE = N.FISH_TYPE
GROUP BY I.FISH_TYPE
ORDER BY FISH_COUNT DESC  
  
   
#ERROR
(1055, "Expression #2 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'programmers.N.FISH_NAME' 
which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by")

➡️ Group By 절에 포함되지 않는 column을 select할 경우 발생하는 에러

# -- 코드를 입력하세요
# 2022년 1월의 도서 판매 데이터를 기준으로 저자 별, 카테고리 별 매출액(TOTAL_SALES = 판매량 * 판매가) 을 구하여, 저자 ID(AUTHOR_ID), 저자명(AUTHOR_NAME), 카테고리(CATEGORY), 매출액(SALES) 리스트를 출력하는 SQL문을 작성해주세요.
# 결과는 저자 ID를 오름차순으로, 저자 ID가 같다면 카테고리를 내림차순 정렬해주세요
SELECT 
    B.AUTHOR_ID, 
    AUTHOR_NAME, 
    CATEGORY, 
    SUM(SALES * PRICE) AS TATAL_SALES
FROM BOOK_SALES S
JOIN BOOK B ON S.BOOK_ID = B.BOOK_ID
JOIN AUTHOR A ON B.AUTHOR_ID = A.AUTHOR_ID
WHERE S.SALES_DATE BETWEEN '2022-01-01' AND '2022-01-31'
GROUP BY
    B.AUTHOR_ID,
    AUTHOR_NAME,
    CATEGORY
ORDER BY AUTHOR_ID, CATEGORY DESC;
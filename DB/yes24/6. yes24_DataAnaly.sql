- 저자별 평균 평점 및 판매지수를 분석하여 인기 있는 저자를 확인합니다.
    
    ```sql
    SELECT author, AVG(rating) as avg_rating, AVG(sales) as avg_sales FROM Books 
    GROUP BY author ORDER BY AVG(rating) DESC, AVG(sales) DESC;
    ```
    
- 출판일에 따른 책 가격의 변동 추세를 분석합니다.
    
    ```sql
    SELECT publishing, AVG(price) FROM Books GROUP BY publishing
    ORDER BY publishing ASC;
    ```
    
- 출판사별 출간된 책의 수와 평균 리뷰 수를 비교 분석합니다.
    
    ```sql
    SELECT publisher, COUNT(*) as book_count, SUM(review) AS review_sum 
    FROM Books GROUP BY publisher ORDER BY book_count DESC;
    ```
    
- 국내도서랭킹과 판매지수의 상관관계를 분석합니다.
    
    ```sql
    SELECT ranking, AVG(sales) FROM Books GROUP BY ranking;
    ```
    
- 가격 대비 리뷰 수와 평점의 관계를 분석하여 가성비 좋은 책을 찾습니다.
    
    ```sql
    SELECT price, AVG(review), AVG(rating) FROM Books GROUP BY price;
    ```
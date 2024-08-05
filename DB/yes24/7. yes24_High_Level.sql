- 출판사별 평균 판매지수가 가장 높은 저자 찾기
    - 각 출판사별로 평균 판매지수가 가장 높은 저자의 이름과 그 평균 판매지수를 조회하세요.
    
    ```sql
    SELECT publisher, author, AVG(sales) as avg_sales
    FROM Books
    GROUP BY publisher, author
    ORDER BY publisher, avg_sales DESC
    ```
    
- 리뷰 수가 평균보다 높으면서 가격이 평균보다 낮은 책 조회
    - 리뷰 수와 가격의 전체 평균을 계산한 후, 이보다 리뷰 수는 높고 가격은 낮은 책들을 조회하세요.
    
    ```sql
    SELECT title, review, price
    FROM Books
    WHERE review > (SELECT AVG(review) FROM Books) AND price < (SELECT AVG(price) FROM Books);
    ```
    
- 가장 많은 종류의 책을 출판한 저자 찾기
    - 서로 다른 제목의 책을 가장 많이 출판한 저자를 찾으세요.
    
    ```sql
    SELECT author, COUNT(DISTINCT title) as num_books
    FROM Books
    GROUP BY author
    ORDER BY num_books DESC
    LIMIT 1;
    ```
    
- 각 저자별로 가장 높은 판매지수를 기록한 책 조회
    - 각 저자별로 가장 높은 판매지수를 기록한 책의 제목과 그 판매지수를 조회하세요.
    
    ```sql
    SELECT author, MAX(sales) as max_sales
    FROM Books
    GROUP BY author;
    ```
    
- 연도별 출판된 책 수와 평균 가격 비교
    - 연도별로 출판된 책의 수와 그 해 출판된 책들의 평균 가격을 비교 분석하세요.
    
    ```sql
    SELECT YEAR(publishing) as year, COUNT(*) as num_books, AVG(price) as avg_price
    FROM Books
    GROUP BY year;
    ```
    
- 출판사가 같은 책들 중 평점 편차가 가장 큰 출판사 찾기
    - 같은 출판사에서 출판된 책들 중 평점 편차가 가장 큰 출판사와 그 편차를 조회하세요.
    
    ```sql
    SELECT publisher, MAX(rating) - MIN(rating) as rating_difference
    FROM Books
    GROUP BY publisher
    HAVING COUNT(*) >= 2
    ORDER BY rating_difference DESC;
    ```
    
- 특정 저자의 책들 중 판매지수 대비 평점이 가장 높은 책 찾기
    - 특정 저자의 책들 중 판매지수 대비 평점이 가장 높은 책의 제목과 그 비율을 조회하세요.
    
    ```sql
    SELECT title, sales, rating / sales as ratio
    FROM Books
    WHERE author = '특정 저자'
    ORDER BY ratio DESC
    LIMIT 1;
    ```
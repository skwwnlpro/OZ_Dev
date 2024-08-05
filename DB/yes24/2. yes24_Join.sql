- 저자별로 출판한 책의 수를 조회하세요.
    
    ```sql
    SELECT author, COUNT(*) AS books_count FROM Books GROUP BY author;
    ```
    
- 가장 많은 책을 출판한 출판사를 찾으세요.
    
    ```sql
    SELECT publisher, COUNT(*) AS num_books FROM Books GROUP BY publisher ORDER BY num_books DESC LIMIT 1;
    ```
    
- 가장 높은 평균 평점을 가진 저자를 찾으세요.
    
    ```sql
    SELECT author, AVG(rating) AS avg_rating FROM Books GROUP BY author ORDER BY avg_rating DESC LIMIT 1;
    ```
    
- 국내도서랭킹이 1위인 책의 제목과 저자를 조회하세요.
    
    ```sql
    SELECT * FROM Books WHERE ranking = 1;
    ```
    
- 판매지수와 리뷰 수가 모두 높은 상위 10개의 책을 조회하세요.
    
    ```sql
    SELECT title, sales, review FROM Books ORDER BY sales DESC, review DESC LIMIT 10;
    ```
    
- 가장 최근에 출판된 5권의 책을 조회하세요.
    
    ```sql
    SELECT * FROM Books ORDER BY publishing DESC LIMIT 5;
    ```
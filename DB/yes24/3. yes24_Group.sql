- 저자별 평균 평점을 계산하세요.
    
    ```sql
    SELECT author, AVG(rating) AS rating_avg FROM Books GROUP BY author ORDER BY rating_avg;
    ```
    
- 출판일별 출간된 책의 수를 계산하세요.
    
    ```sql
    SELECT publishing, COUNT(*) FROM Books GROUP BY publishing;
    ```
    
- 책 제목별 평균 가격을 조회하세요.
    
    ```sql
    SELECT title, price FROM Books;
    ```
    
- 리뷰 수가 가장 많은 상위 5권의 책을 찾으세요.
    
    ```sql
    SELECT * FROM Books ORDER BY review DESC LIMIT 5;
    ```
    
- 국내도서랭킹 별 평균 리뷰 수를 계산하세요.
    
    ```sql
    SELECT ranking, AVG(review) FROM Books GROUP BY ranking;
    ```
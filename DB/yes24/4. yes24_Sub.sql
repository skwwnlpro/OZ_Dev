- 평균 평점보다 높은 평점을 받은 책들을 조회하세요.
    
    ```sql
    SELECT title, rating FROM Books 
    WHERE rating > (SELECT AVG(rating) FROM Books)
    ORDER BY rating DESC;
    ```
    
- 평균 가격보다 비싼 책들의 제목과 가격을 조회하세요.
    
    ```sql
    SELECT title, price, publisher FROM Books 
    WHERE price > (SELECT AVG(price) FROM Books);
    ```
    
- 가장 많은 리뷰를 받은 책보다 많은 리뷰를 받은 다른 책들을 조회하세요.
    
    ```sql
    SELECT title, review FROM Books 
    WHERE review > (SELECT MAX(review) FROM Books);
    ```
    
- 평균 판매지수보다 낮은 판매지수를 가진 책들을 조회하세요.
    
    ```sql
    SELECT title, sales FROM Books 
    WHERE sales < (SELECT AVG(sales) FROM Books);
    ```
    
- 가장 많이 출판된 저자의 책들 중 최근에 출판된 책을 조회하세요.
    
    ```sql
    SELECT author, title FROM books 
    WHERE author = (SELECT author FROM Books GROUP BY author ORDER BY COUNT(*) DESC LIMIT 1);
    ```
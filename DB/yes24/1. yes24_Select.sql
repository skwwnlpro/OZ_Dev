- 모든 책의 제목과 저자를 조회하세요.
    
    ```sql
    SELECT title, author FROM Books;
    ```
    
- 평점이 8 이상인 책 목록을 조회하세요.
    
    ```sql
    SELECT title, rating FROM Books WHERE rating >= 8;
    ```
    
- 리뷰 수가 100개 이상인 책들의 제목과 리뷰 수를 조회하세요.
    
    ```sql
    SELECT title, review FROM Books WHERE review >= 100 ORDER BY review DESC;
    ```
    
- 가격이 20,000원 미만인 책들의 제목과 가격을 조회하세요.
    
    ```sql
    SELECT title, price FROM Books WHERE price < 20000;
    ```

- 국내도서 TOP100에 4주 이상 머문 책들을 조회하세요.
    
    ```sql
    SELECT * FROM Books WHERE ranking_weeks >= 4 ORDER BY ranking_weeks DESC;
    ```
    
- 특정 저자의 모든 책을 조회하세요.
    
    ```sql
    SELECT title FROM Books WHERE author = 'author';
    ```
    
- 특정 출판사가 출판한 책들을 조회하세요.
    
    ```sql
    SELECT title FROM Books WHERE publisher = 'publisher';
    ```
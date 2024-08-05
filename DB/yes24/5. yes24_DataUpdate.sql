- 특정 책의 가격을 업데이트하세요.
    
    ```sql
    UPDATE Books SET price = 100 WHERE title = 'Title';
    ```
    
- 특정 저자의 책 제목을 변경하세요.
    
    ```sql
    UPDATE Books SET title = 'Updated' WHERE author = 'author';
    ```
    
- 판매지수가 가장 낮은 책을 데이터베이스에서 삭제하세요.
    
    ```sql
    DELETE FROM Books WHERE sales = (SELECT MIN(sales) FROM Books);
    ```
    
- 특정 출판사가 출판한 모든 책의 평점을 1점 증가시키세요.
    
    ```sql
    UPDATE Books SET rating = rating + 1 WHERE publisher = 'pub';
    ```
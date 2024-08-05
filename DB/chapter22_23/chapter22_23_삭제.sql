-- 초급
-- (1) **`customers`** 테이블에서 특정 고객을 삭제하세요.
delete from customers where customerNumber = 1;
-- (2) **`products`** 테이블에서 특정 제품을 삭제하세요.
delete from products where productCode = '111';
-- (3) **`employees`** 테이블에서 특정 직원을 삭제하세요.
delete from employees where employeeNumber = 1;
-- (4) **`offices`** 테이블에서 특정 사무실을 삭제하세요.
delete from offices where officeCode = 1;
-- (5) **`orders`** 테이블에서 특정 주문을 삭제하세요.
delete from orders where orderNumber = 1;
-- (6) **`orderdetails`** 테이블에서 특정 주문 상세를 삭제하세요.
delete from orderdetails where orderNumber = 1;
-- (7) **`payments`** 테이블에서 특정 지불 내역을 삭제하세요.
delete from payments where  customerNumber = 1;
-- (8) **`productlines`** 테이블에서 특정 제품 라인을 삭제하세요.
delete from productlines where productLine = '123';
-- (9) **`customers`** 테이블에서 특정 지역의 모든 고객을 삭제하세요.
delete from customers where city = 'city';
-- (10) **`products`** 테이블에서 특정 카테고리의 모든 제품을 삭제하세요.
delete from products where productLine = 'line';
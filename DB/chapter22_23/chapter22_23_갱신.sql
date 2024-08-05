-- 초급
-- (1) **`customers`** 테이블에서 특정 고객의 주소를 갱신하세요.
update customers set addressLine1 = 'dsasdaad' where customerNumber = 104;
-- (2) **`products`** 테이블에서 특정 제품의 가격을 갱신하세요.
update products set buyPrice = 1111 where productCode = 1;
-- (3) **`employees`** 테이블에서 특정 직원의 직급을 갱신하세요.
update employees set jobTitle = 'ddd' where employeeNumber = 1;
-- (4) **`offices`** 테이블에서 특정 사무실의 전화번호를 갱신하세요.
update offices set phone = '123123' where officeCode = 1;
-- (5) **`orders`** 테이블에서 특정 주문의 상태를 갱신하세요.
update orders set status = 'good' where orderNumber = 1;
-- (6) **`orderdetails`** 테이블에서 특정 주문 상세의 수량을 갱신하세요.
update orderdetails set quantityOrdered = 3 where orderNumber = 1;
-- (7) **`payments`** 테이블에서 특정 지불의 금액을 갱신하세요.
update payments set amount = 20000 where customerNumber = 1;
-- (8) **`productlines`** 테이블에서 특정 제품 라인의 설명을 갱신하세요.
update productlines set textDescription = 'Desc' where productLine = 'aa';
-- (9) **`customers`** 테이블에서 특정 고객의 이메일을 갱신하세요.
update customers set email = 'an@ddd.com' where customerNumber = 1;
-- (10) products 테이블에서 여러 제품의 가격을 한 번에 갱신하세요.
update products set buyPrice = buyPrice * 2;

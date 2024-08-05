-- 초급
use classicmodels;
select * from customers c ;
select * from products p ;
-- (1) **`customers`** 테이블에 새 고객을 추가하세요.
insert into customers (customerNumber , customerName, ... ) values (104, 'name', ...);
-- (2) **`products`** 테이블에 새 제품을 추가하세요.
insert into products (productCode, productName, ... ) values ('s10_9999', '1111', ...);
-- (3) **`employees`** 테이블에 새 직원을 추가하세요.
insert into employees (employeeNumber, lastName, ... ) values ( 10, 'abc', ...);
-- (4) **`offices`** 테이블에 새 사무실을 추가하세요.
insert into offices (officeCode, city, ... ) values ('9999', 'city', ...);
-- (5) **`orders`** 테이블에 새 주문을 추가하세요.
insert into orders (orderNumber, orderDate, ... ) values (10, '24-01-01', ...);
-- (6) **`orderdetails`** 테이블에 주문 상세 정보를 추가하세요.
insert into orderdetails (productCode, productCode, ... ) values (10, '1111', ...);
-- (7) **`payments`** 테이블에 지불 정보를 추가하세요.
insert into payments (customerNumber, checkNumber, ... ) values (10, '1111', ...);
-- (8) **`productlines`** 테이블에 제품 라인을 추가하세요.
insert into productlines (productLine, textDescription, ... ) values ('9999', 'abc', ...);
-- (9) **`customers`** 테이블에 다른 지역의 고객을 추가하세요.
insert into customers (customerNumber, customerName, city, ... ) values (105, 'name', 'city', ...);
-- (10) **`products`** 테이블에 다른 카테고리의 제품을 추가하세요.
insert into products (productCode, productName, productLine, ... ) values ('9999', '11', 'abc', ...);

-- 중급

-- (1) **`customers`** 테이블에 여러 고객을 한 번에 추가하세요.
insert into customers (customerNumber , customerName, ... ) values (104, 'name1', ...), (105, 'name2', ...);
-- (2) **`products`** 테이블에 여러 제품을 한 번에 추가하세요.
insert into products (productCode, productName, ... ) values ( 's10_1', '1111', ...), ( 's10_2', '1112', ...);
-- (3) **`employees`** 테이블에 여러 직원을 한 번에 추가하세요.
insert into employees (employeeNumber, lastName, ... ) values ( 10, 'abc', ...), (11, 'dff', ...);
-- (4) **`orders`**와 **`orderdetails`**에 연결된 주문을 한 번에 추가하세요.
insert into orders (orderNumber, orderDate, ... ) values (10, '24-01-01', ...);
insert into orderdetails (productCode, productCode, ... ) values (10, '1111', ...), (11, '1112', ...);
-- (5)**`payments`** 테이블에 여러 지불 정보를 한 번에 추가하세요.
insert into payments (customerNumber, checkNumber, ... ) values (10, '1111', ...), (11, '2222', ...);
-- (6) **`customers`** 테이블에 고객을 추가하고 바로 주문을 추가하세요.
insert into customers (customerNumber , customerName, ... ) values (104, 'name', ...);
insert into orders (orderNumber, orderDate, ... ) values (10, '24-01-01', ...);
-- (7) **`employees`** 테이블에 직원을 추가하고 바로 직급을 할당하세요.
insert into employees (employeeNumber, lastName, ... ) values ( 10, 'abc', ...);
update employees set jobTitle = "Any" where employeeNumber = 10;
-- (8) **`products`** 테이블에 제품을 추가하고 바로 재고를 업데이트하세요.
insert into products (productCode, productName, ... ) values ('s10_9999', '1111', ...);
update products set quantityInStock = 10 where productCode = 's10_9999';
-- (9) **`offices`** 테이블에 새 사무실을 추가하고 바로 직원을 할당하세요.
insert into offices (officeCode, city, ... ) values ('9999', 'city', ...);
update employees set officeCode = '9999' where lastName = 'aaa';
-- (10) **`productlines`** 테이블에 제품 라인을 추가하고 바로 여러 제품을 추가하세요.
insert into productlines (productLine, textDescription, ... ) values ('9999', 'abc', ...);
insert into products (productCode, productName, ... ) values ('123', '11', ...), ('123', 'asd', ...);
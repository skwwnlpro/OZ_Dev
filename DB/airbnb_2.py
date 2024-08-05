import pymysql

connection = pymysql.connect(
    host="localhost",
    user="",
    password="",
    db="airbnb",
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor,
)

try:
    with connection.cursor() as cursor:
        # 1번
        sql = "INSERT INTO Products (productName, price, stockQuantity) VALUES (%s, %s, %s)"
        cursor.execute(sql, ("Python", 29.99, 10))
        connection.commit()

        # 2번
        sql = "SELECT * FROM Customers"
        cursor.execute(sql)
        print("SELECT 연산 결과: ")
        for row in cursor.fetchall():
            print(row)

        # # 3번
        sql = "UPDATE Products SET stockQuantity = stockQuantity - %s WHERE productID = %s"
        cursor.execute(sql, (5, 13))
        connection.commit()

        # 4번
        sql = "SELECT customerID, SUM(totalAmount) FROM Orders Group By customerID"
        cursor.execute(sql)
        for row in cursor.fetchall():
            print(row)

        # # 5번
        sql = "UPDATE Customer SET email = '%s' where customerID = %s"
        cursor.execute(sql, ("abc", 1))
        connection.commit()

        # 6번
        sql = "DELETE FROM Orders WHERE orderID = %s"
        cursor.execute(sql, 15)
        connection.commit()

        # 7번
        sql = "SELECT * FROM Products WHERE productName LIKE %s"
        cursor.execute(sql, ("%Book%"))
        for row in cursor.fetchall():
            print(row)

        # 8번
        sql = "SELECT * FROM Orders WHERE customerID = %s"
        cursor.execute(sql, (1))
        for row in cursor.fetchall():
            print(row)

        # 9번
        sql = """
        SELECT customerID, COUNT(*)
        FROM Orders
        GROUP BY customerID
        ORDER BY orderCount DESC
        LIMIT 1
        """
        cursor.execute(sql)
        top_customer = cursor.fetchone()
        print(f"Top Customer ID: {top_customer[0]}, Orders: {top_customer[1]}")

finally:
    connection.close()

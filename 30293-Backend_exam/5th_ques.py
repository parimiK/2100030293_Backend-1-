import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Raviteja@01',
    database='exam'
)

try:
    cusor=conn.cursor()

    query="""SELECT c.FirstName,c.LastName,c.Email,sum(oi.Quantity*p.Price) as total
            from customers  c
            join orders o on o.OrderID=c.CustomerID
            join orderitems oi on o.OrderID=oi.OrderID
            join products p on p.ProductID=oi.ProductID
            GROUP BY c.FirstName,c.LastName,c.Email"""

    cusor.execute(query)

    result=cusor.fetchall()

    for row in result:
        print(row)
        
except Exception as e:
    print(e)
import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Raviteja@01',
    database='exam'
)

try:
    cusor=conn.cursor()

    query="""select monthname(o.Orderdate),count(o.orderid) as totalOrders,sum(oi.quantity*p.price) as totalSalesAmount
                from orders o
                join Orderitems as oi on oi.orderid=o.orderid
                join products as p on p.productid=oi.productid
                where year(o.orderdate)=2023
                group by monthname(o.Orderdate)
                order by monthname(o.orderdate)"""

    cusor.execute(query)

    result=cusor.fetchall()

    for row in result:
        print(row)
        
except Exception as e:
    print(e)
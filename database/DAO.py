from database.DB_connect import DBConnect
from model.store import Store
from model.order import Order
class DAO():

    @staticmethod
    def getAllStores():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        result = []

        query = """select *
            from stores"""

        cursor.execute(query, )

        for row in cursor:
            result.append(Store(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllNodes(ID):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        result = []

        query = """select *
                from orders o 
                where o.store_id = %s"""

        cursor.execute(query, (ID,))

        for row in cursor:
            result.append(Order(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllEdges(ID, u : Order, n):
        conn = DBConnect.get_connection()
        cursor = conn.cursor()

        result = []

        query = """select o1.order_id
from orders o, orders o1
where o.store_id = %s and o.order_id = %s 
and o.store_id =  o1.store_id 
and ABS(datediff(o.order_date, o1.order_date)) < %s
and datediff(o.order_date, o1.order_date) != 0"""

        cursor.execute(query, (ID, u.order_id, n))

        for row in cursor:
            result.append((row[0]))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getPeso(ID, u: Order): #salvare per ogni nodo il peso
        conn = DBConnect.get_connection()
        cursor = conn.cursor()

        result = []

        query = """select sum(oi.quantity)
from order_items oi, orders o
where oi.order_id = %s
and o.store_id = %s
and oi.order_id = o.order_id """

        cursor.execute(query, (u.order_id,ID))

        for row in cursor:
            result.append(row[0])

        cursor.close()
        conn.close()
        return result[0]

if  __name__ == "__main__":
    print(DAO.getAllStores())

    """@staticmethod
    def getAllEdges(ID, u : Order, n, Map):
        conn = DBConnect.get_connection()
        cursor = conn.cursor()

        result = []

        query = select  o.order_id, o1.order_id
from orders o, orders o1
where o.store_id = 1 #and o.order_id = 1 
and o1.order_id > o.order_id
and o.store_id =  o1.store_id 
and ABS(datediff(o.order_date, o1.order_date)) < 5
and datediff(o.order_date, o1.order_date) != 0

        cursor.execute(query, (ID, u.order_id, n))

        for row in cursor:
            nodo1 = Map[row[0]]  
            nodo2 = Map[row[1]]
            result.append(Arco(nodo1, nodo2))

        cursor.close()
        conn.close()
        return result
"""
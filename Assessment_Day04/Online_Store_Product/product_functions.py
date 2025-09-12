from db_config import get_connection
from mysql.connector import Error


class ProductCatalogDB:
    def add_category(self,category_name):
        try:
            conn=get_connection()
            cursor=conn.cursor()
            cursor.execute("insert into categories (name) values (%s)",(category_name,))
            conn.commit()
            print(f"Category '{category_name} added")
        except Error as e:
            print("Error:",e)
        finally:
            cursor.close()
            conn.close()

    
    def add_product(self,name,category_id,price,stock_quantity):
        try:
            conn=get_connection()
            cursor=conn.cursor()
            cursor.execute("SELECT category_id FROM categories WHERE category_id = %s", (category_id,))
            if cursor.fetchone() is None:
                print("Invalid category ID.")
                return
            cursor.execute(
                "INSERT INTO products (name, category_id, price, stock_quantity) VALUES (%s, %s, %s, %s)",
                (name, category_id, price, stock_quantity)
            )
            conn.commit()
            print(f"Product '{name}' added.")
        except Error as e:
            print("Error:", e)
        finally:
            cursor.close()
            conn.close()


    def update_product(product_id, price, stock):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE products SET price = %s, stock_quantity = %s WHERE product_id = %s", (price, stock, product_id))
        conn.commit()
        print("Product updated.")
        cursor.close()
        conn.close()

    def delete_product(product_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM products WHERE product_id = %s", (product_id,))
        conn.commit()
        print("Product deleted.")
        cursor.close()
        conn.close()

    def search_products(max_price):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products WHERE price <= %s", (max_price,))
        for row in cursor.fetchall():
            print(row)
        cursor.close()
        conn.close()

    def low_stock_report(threshold):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products WHERE stock_quantity < %s", (threshold,))
        for row in cursor.fetchall():
            print(row)
        cursor.close()
        conn.close()

    def show_products():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
        SELECT p.name, c.category_name, p.price, p.stock_quantity
        FROM products p
        LEFT JOIN categories c ON p.category_id = c.category_id
        """)
        for row in cursor.fetchall():
            print(row)
        cursor.close()
        conn.close()



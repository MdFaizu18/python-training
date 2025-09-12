from product_functions import ProductCatalogDB

db=ProductCatalogDB()

db.add_category("electronics")

db.add_product("Laptop",1,40000,5)
db.add_product("Mouse",1,200,3)

db.update_product(1,price=50000,stock=10)

db.delete_product(2)

db.search_products(max_price=10000)

db.low_stock_report(threshold=5)

db.show_products()



display_order_sql ="""SELECT orders.orders_id,  
customers.customers_name, 
couriers.couriers_name,
status.status  
FROM orders
JOIN customers ON customers.customers_id = orders.customers_id
JOIN couriers ON couriers.couriers_id = orders.couriers_id
JOIN status ON status.status_id = orders.status_id
JOIN order_products ON order_products.orders_id= orders.orders_id
JOIN products ON products.products_id = order_products.products_id
GROUP BY orders_id
;"""


#order_id	products_name	quantity
order_product_quantities_sql ="""SELECT order_products.orders_id, 
products.products_name,
COUNT(order_products.products_id) as Quantity
FROM order_products
JOIN products ON products.products_id = order_products.products_id
GROUP BY order_products.orders_id, order_products.products_id;"""
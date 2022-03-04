"""Module for generating games by user report"""
from django.shortcuts import render
from django.db import connection
from django.views import View

from bangazon_reports.views.helpers import dict_fetch_all


class PaidOrders(View):
    def get(self, request):
        with connection.cursor() as db_cursor:

            
            db_cursor.execute("""
            select au.first_name, au.last_name, op.order_id, p.price, pt.merchant_name
            from bangazon_api_order o
            join bangazon_api_orderproduct op on op.order_id = o.id
            join bangazon_api_product p on op.product_id = p.id
            join bangazon_api_paymenttype pt on o.payment_type_id = pt.id
            join auth_user au on au.id = o.user_id
            where o.completed_on != "null" 
            group by op.order_id
            """)
            # Pass the db_cursor to the dict_fetch_all function to turn the fetch_all() response into a dictionary
            dataset = dict_fetch_all(db_cursor)

          

            paid_order = []

            for row in dataset:
                purchase = {'order_id': row['order_id'],
                        'last_name': row['last_name'],
                        'first_name': row['first_name'],
                        'merchant_name': row['merchant_name'],
                        'price': row['price'],
                }
                
                paid_order.append(purchase)
           
              
        
        # The template string must match the file name of the html template
        template = 'users/paid_orders.html'
        
        # The context will be a dictionary that the template can access to show data
        context = {
            "paid_orders_list": paid_order
        }

        return render(request, template, context)
    
    

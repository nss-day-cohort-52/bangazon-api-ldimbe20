"""Module for generating games by user report"""
from django.shortcuts import render
from django.db import connection
from django.views import View

from bangazon_reports.views.helpers import dict_fetch_all


class ExpensiveProductList(View):
    def get(self, request):
        with connection.cursor() as db_cursor:

            
            db_cursor.execute("""
            select p.price, p.name, p.id, p.description
            from bangazon_api_product p
            where p.price > 500
            
            """)
            # Pass the db_cursor to the dict_fetch_all function to turn the fetch_all() response into a dictionary
            dataset = dict_fetch_all(db_cursor)

            
            expensive_products = []

            for row in dataset:
                # TODO: Create a dictionary called game that includes 
                # the name, description, number_of_players, maker,
                # game_type_id, and skill_level from the row dictionary
                product = { "id": row['id'],
                           "name": row['name'], 
                           "price": row['price'],
                           "description": row ['description']
                    
                }
                
                expensive_products.append(product)
                #if this is not in the proper scope, it needs to be in the four loop, 
                #it will not show all items otherwise
              
        template = 'users/product_expenses.html'
        
        
        context = {
            "productexpense_list": expensive_products
        }
        # above is what is storing all the data

        return render(request, template, context)

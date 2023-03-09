import pandas as pd
# Create a dummy dataframe
orders_df = pd.DataFrame()
orders_df['customer_id'] = [1,1,1,1,1,2,2,3,3,3,3,3]
orders_df['order_id'] = [1,1,1,2,2,3,3,4,5,6,6,6]
orders_df['item'] = ['apples', 'chocolate', 'chocolate', 'coffee', 'coffee', 'apples', 
                     'bananas', 'coffee', 'milkshake', 'chocolate', 'strawberry', 'strawberry']

def multiple_items_per_order(_items):
    

# Then, we transform each group according to the defined function
 orders_df['item_duplicated_per_order'] = (                    
                        orders_df                             
                        .groupby(['customer_id'])['item']        
                        .transform(multiple_items_per_order)) 
print(orders_df)
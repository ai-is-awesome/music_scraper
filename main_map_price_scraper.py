# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 05:37:15 2020

@author: Piyush
"""

from map_price_scraper import get_map_price
import pandas as pd
import time
import traceback

map_price_col_name = 'map_price'
read_file = 'assets/products1.csv'




def main(read_file, start_index = None, end_index = None):
    df = pd.read_csv(read_file)
    
    if start_index == None:
        start_index = 0
        
    if end_index == None:
        end_index = len(df) - 1
        
    
    for i in range(start_index, end_index + 1):
        print(i)
        try:
            row = df.iloc[i]
            url = row['product_url']
            map_price_dict = get_map_price(url)
            map_price = map_price_dict['map_price']
            df.loc[i, 'map_price'] = map_price
            
        except:
            traceback.print_exc()
            
        finally:
            time.sleep(.5)
            
        if i % 10 ==0 and i != 0:
            df.to_csv(read_file)
            print('Successfully saved %s products.' % (i))
    
    try:
        df.to_csv(read_file)
        print('Successfully saved all the products from %i to %i. ' % (start_index, end_index))
        
    except:
        traceback.print_exc()
            
            
            
    
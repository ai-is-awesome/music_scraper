# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 02:37:24 2020

@author: Piyush
"""

from halleonard_product_scraper import get_details





def main(csv_file_location, start_index = None, end_index = None, ):
    df = pd.read_csv(READ_FILE)
    
    if start_index == None:
        start_index = 0
        
    if end_index == None:
        end_index = len(df)
    
    
    for i in range(start_index, end_index):
        try:
            row = df.iloc[i]
            product_url = row['product_url']
            details = get_product_details(product_url)
            for key in details.keys():
                if key in df.columns:
                    df.loc[i, key] = details[key]
        
        
        except:
            traceback.print_exc()
            
        finally:
            time.sleep(.4)
            
            
        if i % 10 ==0 and i != 0:
            print(i, 'products scraped successfully...')
            try:
                df.to_csv(READ_FILE, index = False)
                    
            except:
                traceback.print_exc()
                
            finally:
                pass
                    
        
    df.to_csv(READ_FILE)
                
                
    
    
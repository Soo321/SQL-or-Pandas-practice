import pandas as pd

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    result = customer[(customer['referee_id']!=2) | (customer['referee_id'].isnull())] 
    return result[['name']]
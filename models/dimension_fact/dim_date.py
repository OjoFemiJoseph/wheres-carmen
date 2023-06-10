import pandas as pd

def model(dbt, session):
    dbt.config(materialized = "table")

    start_date = '1960-01-01'
    end_date = '2024-01-01'

    date_df = pd.date_range(start=start_date, end=end_date, freq='H')

    date_df_different_granularities = pd.DataFrame({
        'datetime': date_df.date,
        'year': date_df.year,
        'month': date_df.month,
        'day': date_df.day,
        'hour': date_df.hour,
        'minute': date_df.minute,
        'second': date_df.second,
        'weekday': date_df.weekday, 
        'quarter': date_df.quarter
    })
    date_df_different_granularities['date_id'] = list(range(1,date_df_different_granularities.shape[0]+1))
    
    return date_df_different_granularities
   
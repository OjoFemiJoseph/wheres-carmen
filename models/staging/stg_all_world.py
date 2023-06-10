import pandas as pd
import ast 

def model(dbt, session):
    dbt.config(materialized = "table")

    referenced_pacific = dbt.ref('stg_pacific')
    pacific_df = referenced_pacific.to_pandas()
    pacific_df['region'] = ['pacific' for _ in range(pacific_df.shape[0])]

    referenced_indian = dbt.ref('stg_indian')
    indian_df = referenced_indian.to_pandas()
    indian_df['region'] = ['indian' for _ in range(indian_df.shape[0])]

    referenced_europe = dbt.ref('stg_europe')
    europe_df = referenced_europe.to_pandas()
    europe_df['region'] = ['europe' for _ in range(europe_df.shape[0])]

    referenced_australia = dbt.ref('stg_australia')
    australia_df = referenced_australia.to_pandas()
    australia_df['region'] = ['australia' for _ in range(australia_df.shape[0])]

    referenced_atlantic = dbt.ref('stg_atlantic')
    atlantic_df = referenced_atlantic.to_pandas()
    atlantic_df['region'] = ['atlantic' for _ in range(atlantic_df.shape[0])]

    referenced_asia = dbt.ref('stg_asia')
    asia_df = referenced_asia.to_pandas()
    asia_df['region'] = ['asia' for _ in range(asia_df.shape[0])]

    referenced_america = dbt.ref('stg_america')
    america_df = referenced_america.to_pandas()
    america_df['region'] = ['america' for _ in range(america_df.shape[0])]

    referenced_africa = dbt.ref('stg_africa')
    africa_df = referenced_africa.to_pandas()
    africa_df['region'] = ['africa' for _ in range(africa_df.shape[0])]

    data = [pacific_df,
            indian_df,
            europe_df,
            australia_df,
            atlantic_df,
            asia_df,
            america_df,
            africa_df]
    
    union_df = pd.concat(data)
    union_df['sighting_id'] = list(range(1,union_df.shape[0]+1))
    
    return  union_df
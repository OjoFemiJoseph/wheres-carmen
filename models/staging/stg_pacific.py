
def model(dbt, session):
    dbt.config(materialized = "table", packages = ["pandas"])
    
    referenced_table = dbt.ref("PACIFIC")
    df = referenced_table.to_pandas()
    column_names = ['date_witness',
                    'date_agent',
                    'witness',
                    'agent',
                    'latitude',
                    'longitude',
                    'city',
                    'country',
                    'region_hq',
                    'has_weapon',
                    'has_hat',
                    'has_jacket',
                    'behavior']

    df.columns = column_names
    df.rename(columns=dict(zip(df.columns,column_names)),inplace=True)
    return df
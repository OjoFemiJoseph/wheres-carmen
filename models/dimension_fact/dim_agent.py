
def model(dbt, session):
    dbt.config(materialized = "table")

    referenced_world = dbt.ref('stg_all_world')
    all_word_df = referenced_world.to_pandas()
 
    all_word_df = all_word_df[['agent']].drop_duplicates()
    all_word_df['agent_id'] = list(range(1,all_word_df.shape[0]+1))
    
    return  all_word_df[['agent_id','agent']]
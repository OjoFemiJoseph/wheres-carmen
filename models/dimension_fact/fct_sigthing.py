
def model(dbt, session):
    dbt.config(materialized = "table")

    referenced_world = dbt.ref('stg_all_world')
    all_word_df = referenced_world.to_pandas()
    all_word_df['sighting_id'] = list(range(1,all_word_df.shape[0]+1))

    ref_dim_agency = dbt.ref('dim_agency')
    dim_agency = ref_dim_agency.to_pandas()

    ref_dim_agent = dbt.ref('dim_agent')
    dim_agent = ref_dim_agent.to_pandas()
  
    ref_dim_location = dbt.ref('dim_location')
    dim_location_df = ref_dim_location.to_pandas()

    ref_dim_perpretrator_behavior = dbt.ref('dim_perpretrator_behavior')
    dim_perpretrator_behavior = ref_dim_perpretrator_behavior.to_pandas()

    ref_dim_perpretrator = dbt.ref('dim_perpretrator')
    dim_perpretrator = ref_dim_perpretrator.to_pandas()
    
    result = all_word_df.merge(dim_agency, on=['region','region_hq'], how='left')
    result.drop(columns=['region','region_hq'], inplace=True)
    
    result = result.merge(dim_agent, on=['agent'], how='left')
    result.drop(columns=['agent'], inplace=True)
    
    result = result.merge(dim_location_df, on=['city','country'], how='left')
    result.drop(columns=['city','country'], inplace=True)

    result = result.merge(dim_perpretrator_behavior, on=['behavior'], how='left')
    result.drop(columns=['behavior'], inplace=True)
    
    result = result.merge(dim_perpretrator, on=['witness'], how='left')
    result.drop(columns=['witness'], inplace=True)
    
    return  result
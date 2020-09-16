#!/usr/bin/env python
# coding: utf-8

# In[249]:


import censusdata
import pandas as pd

pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.precision', 2)

_ACS_api_key = '90e59964dfea9641b1f356c366fbe0f49dcc794a'


# In[275]:


state_selected = 'Pennsylvania'

csv_filename = 'acs5_2018.csv'

variables_map = {"B23025_005E": "Unemployed", 
"B19052_002E": "Income", 
"B02001_002E": "WhiteRace",
"B02001_003E": "BlackRace", 
"B02001_004E": "IndianAlaskanRace", 
"B02001_005E": "AsianRace", 
"B01001_001E": "Population",
"B01001_002E": "MaleGender", 
"B01001_026E": "FemaleGender", 
"B15003_017E": "HighSchoolEducation", 
"B15003_019E": "College_Less_1yrEducation", 
"B15003_020E": "College_More_1YREducation", 
"B15003_021E": "AssociateDegreeEducation",
"B15003_022E": "BachelorDegreeEducation", 
"B15003_023E": "MasterDegreeEducation", 
"B15003_024E": "ProfessionalDegreeEducation",
"B15003_025E": "DoctorateDegreeEducation"}

variables_selected = list(variables_map.keys()) 


# In[276]:


state_geoMap = censusdata.geographies(censusdata.censusgeo([('state', '*')]), 'acs5', 2018, key=_ACS_api_key)
state_censusgeo = state_geoMap[state_selected]
state_geo_Param = state_censusgeo.params()[0]


# In[277]:


# list all counties in that state
state_counties = censusdata.censusgeo([state_geo_Param, ('county','*')])


# In[271]:

stateCounty_geoMap = censusdata.geographies(state_counties, 'acs5', 2018, key=_ACS_api_key)

acs_cumulative_dataframe = pd.DataFrame()

for key, value in stateCounty_geoMap.items():
    stateCounty_censusgeo = value
    
    # list all block groups in that state county
    state_county_block_groups = censusdata.censusgeo([stateCounty_censusgeo.params()[0], stateCounty_censusgeo.params()[1], ('block group', '*')])
    
    acs_dataFrame = censusdata.download('acs5', 2018, state_county_block_groups, variables_selected, key=_ACS_api_key)
    
    acs_cumulative_dataframe = acs_cumulative_dataframe.append(acs_dataFrame)


# In[278]:

acs_cumulative_dataframe.rename(columns = variables_map, inplace = True) 


# In[279]:


censusdata.exportcsv(csv_filename, acs_cumulative_dataframe)

print("The data has been exported to ", csv_filename)




import numpy as np
import pandas as pd
# Data cleaning for a4-remix


water_global = pd.read_csv('data/water_cleaned_2015.csv')
water_counties = pd.read_csv('data/water_counties.csv')

water_global= water_global.set_index('Country')


water_counties['id'] = water_counties['FIPS']
water_counties['county'] = water_counties['COUNTY']
water_counties_filtered = water_counties.set_index('id')[['STATE', 'TP-TotPop','DO-PSDel', 'county']]

water_counties_filtered['groundwater_per_day'] = water_counties_filtered['DO-PSDel'] * 1000000
water_counties_filtered['total_pop'] = water_counties_filtered['TP-TotPop'] * 1000

water_counties_filtered['gal_per_person'] = water_counties_filtered['groundwater_per_day'] / water_counties_filtered['total_pop']
water_counties_filtered['state'] = water_counties_filtered['STATE']

water_counties_final = water_counties_filtered[['state', 'total_pop', 'groundwater_per_day', 'gal_per_person', 'county']]
print(water_counties.head())
#print(water_counties_final.sort_values(by='gal_per_person', ascending=False).head())
print(water_counties_final[water_counties_final['state'] == 'VA'].sort_values(by='gal_per_person').head())
water_counties_final.to_csv('data/water_counties_cleaned.csv')



#calculation for


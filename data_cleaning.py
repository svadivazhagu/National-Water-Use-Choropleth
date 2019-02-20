import numpy as np
import pandas as pd

# Data cleaning for a4-remix


water_global = pd.read_csv('data/water_cleaned_2015.csv')
water_counties = pd.read_csv('data/water_counties.csv')

water_global= water_global.set_index('Country')

water_counties_filtered = water_counties.set_index('COUNTY')[['STATE', 'TP-TotPop','TO-WGWTo']]

water_counties_filtered['groundwater_per_day'] = water_counties_filtered['TO-WGWTo'] * 1000000
water_counties_filtered['total_pop'] = water_counties_filtered['TP-TotPop'] * 1000

water_counties_filtered['gal_per_person'] = water_counties_filtered['groundwater_per_day'] / water_counties_filtered['total_pop']
water_counties_filtered['state'] = water_counties_filtered['STATE']
water_counties_final = water_counties_filtered[['state', 'total_pop', 'groundwater_per_day', 'gal_per_person']]
print(water_counties.head())
print(water_counties_final.head())

water_counties_final.to_csv('data/water_counties_cleaned')

#calculation for


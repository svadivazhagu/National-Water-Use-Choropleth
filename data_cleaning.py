import numpy as np
import pandas as pd

# Data cleaning for a4-remix


water_global = pd.read_csv('data/water_cleaned_2015.csv')
water_counties = pd.read_csv('data/water_counties.csv')

water_global= water_global.set_index('Country')






print(water_counties.to_string())



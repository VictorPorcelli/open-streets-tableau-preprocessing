import pandas as pd

census_data = pd.read_csv("ACSDT5Y2019.B02001_data_with_overlays_2022-02-22T162751.csv")

def split_geoid(row):
    if len(row['GEO_ID']) > 18:
        if row['GEO_ID'].find("US36047") != -1:
            return "3"+row['GEO_ID'][len(row['GEO_ID'])-6:]
        elif row['GEO_ID'].find("US36005") != -1:
            return "2"+row['GEO_ID'][len(row['GEO_ID'])-6:]
        elif row['GEO_ID'].find("US36061") != -1:
            return "1"+row['GEO_ID'][len(row['GEO_ID'])-6:]
        elif row['GEO_ID'].find("US36081") != -1:
            return "4"+row['GEO_ID'][len(row['GEO_ID'])-6:]
        elif row['GEO_ID'].find("US36085") != -1:
            return "5"+row['GEO_ID'][len(row['GEO_ID'])-6:]
    else:
        return ""

census_data['BoroCT'] = census_data.apply(split_geoid, axis = 1)

census_data['Percent White'] = census_data['B02001_002E'] / census_data['B02001_001E']

new_df = census_data[['GEO_ID','BoroCT','Percent White']].copy()

#for median income: 'S1903_C03_001E'

new_df.to_csv("census_data.csv")

import pandas as pd

income_data = pd.read_csv("census_data_median_income.csv")
race_data = pd.read_csv("census_data_percentwhite.csv")

geojson = open("2010_census_tracts.geojson","r")
geojson_text = geojson.read()
new_geojson = open("2010_census_tracts_edited.geojson","w")

while (geojson_text.find("BoroCT2010") != -1):
    index = geojson_text.find("BoroCT2010")+15
    boro_ct = geojson_text[index:index+7]

    median_income = pd.Series(income_data['S1903_C03_001E'].loc[income_data['BoroCT'].astype('string') == boro_ct]).iloc[0]
    percent_white = pd.Series(race_data.loc[race_data['BoroCT'].astype('string') == boro_ct]['Percent White']).iloc[0]

    new_geojson.write(geojson_text[:index+9]+'\n \t\t\t\t"MedianIncome" : "'+str(median_income)+'",\n')
    new_geojson.write('\t\t\t\t"PercentWhite" : "'+str(percent_white)+'",')
    new_geojson.write(geojson_text[index+9:index+51])

    geojson_text = geojson_text[index+51:]

new_geojson.write(geojson_text)

geojson.close()
new_geojson.close()


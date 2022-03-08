import pandas as pd

accidents_data = pd.read_csv("accidents_coded_19-21.csv")
accidents_data['Lat'] = accidents_data[' Longitude ']
accidents_data['Long'] = accidents_data[' Latitude']
del accidents_data[' Longitude ']
del accidents_data[' Latitude']

accidents_sample = accidents_data.sample(1800)

accidents_sample.to_csv("sample_accidents_coded_19-21.csv")

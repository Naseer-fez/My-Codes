import pandas as pd
import numpy as np

df = pd.read_csv("Data.csv")
colums=(df.columns).tolist()
to_remove = ['PropertyID', 'ListingDate', 'Address', 'City', 'State', 'ZipCode',
             'PropertyType', 'YearBuilt', 'DaysOnMarket', 'PriceReduction', 'ViewCount', 'SavedCount', 'PreviousPrice']


df['Garage'] = np.where(df['Garage'].notna(), df['Garage'], 0).astype(str)
correct = ['YES', 'True', 'Yes', 'yes', 'Y', '1']
df['Garage'] = np.where(df['Garage'].isin(correct), 1., 0.)

df['Pool'] = np.where(((df['Pool'].notna()) | (df['Pool'].isin(correct))), 1., 0.)
df['Fireplace'] = np.where(((df['Fireplace'].notna()) | (df['Fireplace'].isin(correct))), 1., 0.)

df['Bathrooms'] = np.where(((df['Bathrooms'].notna())), df['Bathrooms'], df['Bathrooms'].std()).round()

df.groupby('City')['Bathrooms']
df['City'] = df['City'].str.lower().replace(r'\s+', '', regex=True)
df['City'] = df['City'].str.title()
allcities = df['City'].unique()
valid = df.dropna(subset=['City', 'SquareFeet'])

data = valid.groupby("City")['SalePrice'].agg(['mean', 'median', 'std'])
data = data['mean'] - data['std']
df['CityPriceMean'] = df['City'].map(data)

data_feet = valid.groupby("City")['SquareFeet'].agg(['mean', 'median', 'std'])
data_feet = data_feet['mean'] - data_feet['std']
df['CityfeetMean'] = df['City'].map(data_feet)
df['SquareFeet'] = np.where((df['SquareFeet'].notna()), df['SquareFeet'].round(1),
                            (df['CityfeetMean'].round(1))
                            )

df['PropertyType'] = df['PropertyType'].str.lower().replace(r'\s+', '', regex=True)
df['PropertyType'] = df['PropertyType'].str.title()
valid = df.dropna(subset=['PropertyType', 'HOAFees'])

data_houes = (valid.groupby('PropertyType')['HOAFees'].mean() / 10).round() * 10 + 10
df['property_type_Mean'] = df['PropertyType'].map(data_houes)
df['HOAFees'] = np.where(df['HOAFees'].notna(), df['HOAFees'], df['property_type_Mean'])

df['Condition'] = df['Condition'].str.lower().replace(r'\s+', '', regex=True)
df['Condition'] = df['Condition'].str.title()
data_condition = {'Fair': 4, 'Excellent': 5, 'Good': 3, 'Poor': 2}
df['condtion_metric'] = df['Condition'].map(data_condition)

df['Condition'] = np.where(df['Condition'].notna(), df['condtion_metric'], 1)

df['Address'] = df['Address'].str.lower().replace(r'[\d\s]+', '', regex=True)

valid = df.dropna(subset=['Condition', 'Address'])
data_adress = valid.groupby("Address")['SchoolRating'].agg(['mean', 'median', 'std'])
data_adress = data_adress['mean'] - data_adress['std']
df["School_types"] = df['Address'].map(data_adress)
df['SchoolRating'] = np.where(df['SchoolRating'].notna(), df['SchoolRating'], df['School_types'])

valid = df.dropna(subset=['CrimeRate', 'Address'])
data_crime = valid.groupby("Address")['CrimeRate'].agg(['mean', 'median', 'std'])
data_crime = data_crime['mean'] - data_crime['std']
df["crime_types"] = df['Address'].map(data_crime)
df['CrimeRate'] = np.where(df['CrimeRate'].notna(), df['CrimeRate'], df['crime_types'])

valid = df.dropna(subset=['WalkScore', 'Address'])
data_walk = valid.groupby("Address")['WalkScore'].agg(['mean', 'median', 'std'])
data_walk = data_walk['mean'] - data_walk['std']
df["walk_types"] = df['Address'].map(data_walk).round(1)
df['WalkScore'] = np.where(df['WalkScore'].notna(), df['WalkScore'], df['walk_types'])

valid = df.dropna(subset=['DistanceToCity', 'Address'])
data_tocity = valid.groupby("Address")['DistanceToCity'].agg(['mean', 'median', 'std'])
data_tocity = data_tocity['mean'] - data_tocity['std']
df["disctance_types"] = df['Address'].map(data_tocity).round(1)
df['DistanceToCity'] = np.where(df['DistanceToCity'].notna(), df['DistanceToCity'], df['walk_types'])

valid = df.dropna(subset=['PropertyTaxRate', 'Address'])
data_tax = valid.groupby("Address")['DistanceToCity'].agg(['mean', 'median', 'std'])
data_tax = data_tax['mean'] - data_tax['std']
df["tax_types"] = df['Address'].map(data_tax).round(1)
df['PropertyTaxRate'] = np.where(df['PropertyTaxRate'].notna(), df['PropertyTaxRate'], df['tax_types'])

valid = df.dropna(subset=['NeighborhoodIncome', 'Address'])
data_inc = valid.groupby("Address")['DistanceToCity'].agg(['mean', 'median', 'std'])
data_inc = data_inc['mean'] - data_inc['std']
df["inc_types"] = df['Address'].map(data_inc).round(1)
df['NeighborhoodIncome'] = np.where(df['NeighborhoodIncome'].notna(), df['NeighborhoodIncome'], df['inc_types'])

valid = df.dropna(subset=['SquareFeet', 'PropertyType', 'LotSize'])
data_size = valid.groupby("PropertyType",)['LotSize'].agg(['mean', 'median', 'std'])
data_size = data_size['mean']
df["size_types"] = df['PropertyType'].map(data_size)
df['LotSize'] = np.where(df['LotSize'].notna(), df['LotSize'], df['size_types'])

valid = df.dropna(subset=['SquareFeet', 'PropertyType', 'LotSize'])
data_basement = valid.groupby("PropertyType",)['BasementSqFt'].agg(['mean', 'median', 'std'])
data_basement = data_basement['mean']

df["basement_types"] = df['PropertyType'].map(data_basement)
df['BasementSqFt'] = np.where(df['BasementSqFt'].notna(), df['BasementSqFt'], df['basement_types'])

valid = df.dropna(subset=['SquareFeet', 'Bedrooms', 'Address', 'City', 'PropertyType'])

bedroom = valid.groupby('PropertyType')['Bedrooms'].agg(['mean', 'median', 'std', 'count'])
bedroom = (bedroom['mean'] - bedroom['std']).round()
df["bedroom_types"] = df['PropertyType'].map(bedroom)
df['Bedrooms'] = np.where(df['Bedrooms'].notna(), df['Bedrooms'], df['bedroom_types'])

valid=df.dropna(subset=['SquareFeet','Bedrooms','SalePrice','City','PropertyType'])
prices=valid.groupby('PropertyType')['SalePrice'].agg(['mean', 'median','std','count'])
prices=(prices['mean']-prices['std'])
df["sales_types"]=df['PropertyType'].map(prices)
df['SalePrice']=np.where(df['SalePrice'].notna(),df['SalePrice'],df['sales_types'])

reqcoloums = ['Bedrooms', 'Bathrooms', 'SquareFeet', 'LotSize', 'Garage', 'Pool',
              'Fireplace', 'BasementSqFt', 'Condition', 'SchoolRating',
              'CrimeRate', 'WalkScore', 'DistanceToCity', 'NeighborhoodIncome', 'PropertyTaxRate', 'HOAFees']

y = df['SalePrice'].astype(float).to_numpy().reshape(-1, 1)

x = df[reqcoloums].astype(float)

x = x.to_numpy()
df=df[colums]
df = df.dropna(axis=1)
df.to_csv("Output_data.csv")
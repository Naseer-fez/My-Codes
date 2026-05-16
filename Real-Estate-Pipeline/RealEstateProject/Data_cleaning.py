import pandas as pd
import numpy as np


df=pd.read_csv("Data.csv")
colums=(df.columns).tolist()
# print((colums))
# print(data.info())
# so first i need to extact the data from the csv file 
#this is where i need to think like an DS, i need to see which is imp for the output
to_remove=['ZipCode','YearBuilt','PriceReduction','ViewCount','SavedCount','PreviousPrice']

# df=df.drop(df[to_remove],inplace=True)
# df=df.drop('ViewCount')

# df=df.drop(columns=to_remove,inplace=False)

# i removed all the unwanted data strings 
# df=df[df['SalePrice']!=]

# df=df[df['SalePrice'].notna()]
# df = df.reset_index()


# so  now i removed all the non zero sales prices, becuase
# whatever we do we need the sales priceses to be accurate all the others this we can estimat=et them 
# result=df['SalePrice']
# now i need to find a way to fill in the rooms, this is where real data science somes in 
#i need to think somethinh to fill in the data now , 
# (np.where(df['Garage']==0,df['Garage'],1)) to check the availabe of that varaibel 

df['Garage']=np.where(df['Garage'].notna(),df['Garage'],0).astype(str) # this could be optmised better 
# now i have removed nan from garage zero means nan
#['No' 'YES' 'False' 0 'True' 'no' '0' 'N' '1' 'Yes' 'yes' 'Y'] all the options in 
# print(df['Garage'].unique())
correct=['YES','True','Yes','yes','Y','1'] # cna use thsi for all 
# wrong=['No','False','0','no','N',] not needed
df['Garage']=np.where(df['Garage'].isin(correct),1.,0.)# can combine both 
# garage is done , first priority should all be , maxiumize the boleon valesu 
df['Pool']=np.where( ((df['Pool'].notna())| (df['Pool'].isin(correct))),1.,0.)
df['Fireplace']=np.where( ((df['Fireplace'].notna())| (df['Fireplace'].isin(correct))),1.,0.)
# now i have clean all the data from booleon values, now , i need to fit all the other stuff 
# 359 so , remaing , 42 bedrooms
df['Bathrooms']=np.where( ((df['Bathrooms'].notna())),df['Bathrooms'],df['Bathrooms'].std()).round()

df.groupby('City')['Bathrooms']
# df['City'] = df['City'].astype(str).str.lower()
df['City'] = df['City'].str.lower().replace(r'\s+', '', regex=True)
df['City'] = df['City'].str.title()# both are okay just something to think about 
allcities=df['City'].unique()
valid = df.dropna(subset=['City', 'SquareFeet'])# this has all the claid data , in where both the citiesa nd square feet are availiabe l
# print(df.tail())
# data=df.groupby("City")['SalePrice'].agg(['count', 'mean', 'median'])
# check=(df['Bedrooms'].notna())&(df['SquareFeet'].notna())
# print(data['mean'])
data=valid.groupby("City")['SalePrice'].agg(['mean', 'median','std'])
data=data['mean']-data['std']
df['CityPriceMean'] = df['City'].map(data) # can be used for the prices coloum also 
#so now i have all the data of the cities mean and median claues

data_feet=valid.groupby("City")['SquareFeet'].agg(['mean', 'median','std'])
data_feet=data_feet['mean']-data_feet['std']
df['CityfeetMean'] = df['City'].map(data_feet)
df['SquareFeet']=np.where((df['SquareFeet'].notna()),df['SquareFeet'].round(1),
                            (df['CityfeetMean'].round(1))
                            )
# print(df['CityPriceMean'])
# print(df['SquareFeet'].count())
# i have inserted some squarefeet value 


df['PropertyType'] = df['PropertyType'].str.lower().replace(r'\s+', '', regex=True)
df['PropertyType'] = df['PropertyType'].str.title()# both are okay just something to think about 
valid=df.dropna(subset=['PropertyType','HOAFees'])


data_houes=(valid.groupby('PropertyType')['HOAFees'].mean()/10).round()*10+10
# data_houes=((data_houes/10).round())*10+10
# print(data_houes)
df['property_type_Mean'] = df['PropertyType'].map(data_houes)
# print(df[['property_type_Mean', 'PropertyType']])
df['HOAFees']=np.where(df['HOAFees'].notna(),df['HOAFees'],df['property_type_Mean'])

df['Condition'] = df['Condition'].str.lower().replace(r'\s+', '', regex=True)
df['Condition'] = df['Condition'].str.title()
# df['Condition']=np.where(df['Condition'].notna(),1,0)
# [nan 'Fair' 'Excellent' 'Good' 'Poor']
data_condition={'Fair':4 ,'Excellent':5 ,'Good':3 ,'Poor':2}
df['condtion_metric']=df['Condition'].map(data_condition)

df['Condition']=np.where(df['Condition'].notna(),df['condtion_metric'],1)
# print(df[['Address', 'SchoolRating']])
# print(df['Condition'].info())
df['Address'] = df['Address'].str.lower().replace(r'[\d\s]+', '', regex=True)
# print(df['Address'].unique())

valid=df.dropna(subset=['Condition','Address'])
data_adress=valid.groupby("Address")['SchoolRating'].agg(['mean', 'median','std'])
data_adress=data_adress['mean']-data_adress['std']
df["School_types"]=df['Address'].map(data_adress)
df['SchoolRating']=np.where(df['SchoolRating'].notna(),df['SchoolRating'],df['School_types'])
# print(df['CrimeRate'].unique())

valid=df.dropna(subset=['CrimeRate','Address'])
data_crime=valid.groupby("Address")['CrimeRate'].agg(['mean', 'median','std'])
data_crime=data_crime['mean']-data_crime['std']
df["crime_types"]=df['Address'].map(data_crime)
df['CrimeRate']=np.where(df['CrimeRate'].notna(),df['CrimeRate'],df['crime_types'])

valid=df.dropna(subset=['WalkScore','Address'])
data_walk=valid.groupby("Address")['WalkScore'].agg(['mean', 'median','std'])
data_walk=data_walk['mean']-data_walk['std']
df["walk_types"]=df['Address'].map(data_walk).round(1)
df['WalkScore']=np.where(df['WalkScore'].notna(),df['WalkScore'],df['walk_types'])


# print(df['DistanceToCity'].unique())
valid=df.dropna(subset=['DistanceToCity','Address'])
data_tocity=valid.groupby("Address")['DistanceToCity'].agg(['mean', 'median','std'])
data_tocity=data_tocity['mean']-data_tocity['std']
df["disctance_types"]=df['Address'].map(data_tocity).round(1)
df['DistanceToCity']=np.where(df['DistanceToCity'].notna(),df['DistanceToCity'],df['walk_types'])



valid=df.dropna(subset=['PropertyTaxRate','Address'])
data_tax=valid.groupby("Address")['DistanceToCity'].agg(['mean', 'median','std'])
data_tax=data_tax['mean']-data_tax['std']
df["tax_types"]=df['Address'].map(data_tax).round(1)
df['PropertyTaxRate']=np.where(df['PropertyTaxRate'].notna(),df['PropertyTaxRate'],df['tax_types'])
# print(df['PropertyTaxRate'])

valid=df.dropna(subset=['NeighborhoodIncome','Address'])
data_inc=valid.groupby("Address")['DistanceToCity'].agg(['mean', 'median','std'])
data_inc=data_inc['mean']-data_inc['std']
df["inc_types"]=df['Address'].map(data_inc).round(1)
df['NeighborhoodIncome']=np.where(df['NeighborhoodIncome'].notna(),df['NeighborhoodIncome'],df['inc_types'])
# print(df['NeighborhoodIncome'].describe())
# print(df['LotSize'].describe())
valid=df.dropna(subset=['SquareFeet','PropertyType','LotSize'])
data_size=valid.groupby("PropertyType",)['LotSize'].agg(['mean', 'median','std'])
data_size=data_size['mean']
df["size_types"]=df['PropertyType'].map(data_size)
df['LotSize']=np.where(df['LotSize'].notna(),df['LotSize'],df['size_types'])


valid=df.dropna(subset=['BasementSqFt','PropertyType','LotSize'])
data_basement=valid.groupby("PropertyType",)['BasementSqFt'].agg(['mean', 'median','std'])
data_basement=data_basement['mean']


df["basement_types"]=df['PropertyType'].map(data_basement)
df['BasementSqFt']=np.where(df['BasementSqFt'].notna(),df['BasementSqFt'],df['basement_types'])

# the main problem , thta is the bedrooms

valid=df.dropna(subset=['SquareFeet','Bedrooms','Address','City','PropertyType'])

bedroom=valid.groupby('PropertyType')['Bedrooms'].agg(['mean', 'median','std','count'])
bedroom=(bedroom['mean']-bedroom['std']).round()
df["bedroom_types"]=df['PropertyType'].map(bedroom)
# print(df["Bedrooms"].describe())
df['Bedrooms']=np.where(df['Bedrooms'].notna(),df['Bedrooms'],df['bedroom_types'])
valid=df.dropna(subset=['SquareFeet','Bedrooms','SalePrice','City','PropertyType'])

prices=valid.groupby('PropertyType')['SalePrice'].agg(['mean', 'median','std','count'])
prices=(prices['mean']-prices['std'])
df["sales_types"]=df['PropertyType'].map(prices)

df['SalePrice']=np.where(df['SalePrice'].notna(),df['SalePrice'],df['sales_types'])
reqcoloums=[ 'Bedrooms','Bathrooms','SquareFeet','LotSize','Garage','Pool',
'Fireplace','BasementSqFt','Condition','SchoolRating',
    'CrimeRate','WalkScore','DistanceToCity','NeighborhoodIncome','PropertyTaxRate','HOAFees']


y=df['SalePrice'].astype(float).to_numpy().reshape(-1, 1)

x=df[reqcoloums].astype(float)
x=x.to_numpy()
# print(df.info())
#an addition for output data
# df=df.drop(df[to_remove],inplace=True)
# print(to_remove)
df=df[colums]
df = df.dropna(axis=1)
print(df.info())
# df.to_csv("Output_data.csv")




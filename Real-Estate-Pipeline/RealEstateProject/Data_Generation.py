import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Set seed for reproducibility
np.random.seed(42)
random.seed(42)

# Number of rows
n_rows = 400

# Generate base data
data = {
    'PropertyID': range(1, n_rows + 1),
    'ListingDate': [],
    'Address': [],
    'City': [],
    'State': [],
    'ZipCode': [],
    'PropertyType': [],
    'Bedrooms': [],
    'Bathrooms': [],
    'SquareFeet': [],
    'LotSize': [],
    'YearBuilt': [],
    'Garage': [],
    'Pool': [],
    'Fireplace': [],
    'BasementSqFt': [],
    'Condition': [],
    'SchoolRating': [],
    'CrimeRate': [],
    'WalkScore': [],
    'DistanceToCity': [],
    'NeighborhoodIncome': [],
    'PropertyTaxRate': [],
    'HOAFees': [],
    'DaysOnMarket': [],
    'PriceReduction': [],
    'ViewCount': [],
    'SavedCount': [],
    'PreviousPrice': [],
    'SalePrice': []
}

# Cities and states
cities = ['Austin', 'Seattle', 'Denver', 'Portland', 'Boston', 'austin', 'SEATTLE', 'Denver ', ' Portland']
states = ['TX', 'WA', 'CO', 'OR', 'MA', 'tx', 'Wa', 'co']
property_types = ['Single Family', 'Condo', 'Townhouse', 'Multi-Family', 'single family', 'CONDO', 'Townhouse ', ' Condo']
conditions = ['Excellent', 'Good', 'Fair', 'Poor', 'excellent', 'GOOD', 'Fair ', None, '']

# Generate messy data
start_date = datetime(2022, 1, 1)

for i in range(n_rows):
    # Dates in various formats
    date = start_date + timedelta(days=random.randint(0, 730))
    date_formats = [
        date.strftime('%Y-%m-%d'),
        date.strftime('%m/%d/%Y'),
        date.strftime('%d-%m-%Y'),
        date.strftime('%Y/%m/%d'),
        str(date.date()),
        ''
    ]
    data['ListingDate'].append(random.choice(date_formats) if random.random() > 0.05 else np.nan)
    
    # Address
    data['Address'].append(f"{random.randint(100, 9999)} {random.choice(['Main', 'Oak', 'Maple', 'Elm', 'Pine'])} {random.choice(['St', 'Ave', 'Blvd', 'Dr'])}")
    
    # City with inconsistent formatting
    data['City'].append(random.choice(cities))
    
    # State
    data['State'].append(random.choice(states))
    
    # ZipCode (some missing, some invalid)
    if random.random() > 0.1:
        zip_code = random.randint(10000, 99999)
        if random.random() > 0.9:
            zip_code = str(zip_code) + '-' + str(random.randint(1000, 9999))
        data['ZipCode'].append(zip_code)
    else:
        data['ZipCode'].append(np.nan if random.random() > 0.5 else '')
    
    # Property Type
    data['PropertyType'].append(random.choice(property_types))
    
    # Bedrooms (with some outliers and missing)
    if random.random() > 0.08:
        beds = random.choices([2, 3, 4, 5, 6], weights=[0.2, 0.35, 0.3, 0.1, 0.05])[0]
        if random.random() > 0.95:  # Add outliers
            beds = random.choice([0, 1, 10, 12, 15])
        data['Bedrooms'].append(beds if random.random() > 0.02 else float(beds))
    else:
        data['Bedrooms'].append(np.nan)
    
    # Bathrooms (float values, some messy)
    if random.random() > 0.1:
        baths = random.choice([1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5])
        data['Bathrooms'].append(baths if random.random() > 0.05 else str(baths))
    else:
        data['Bathrooms'].append(np.nan)
    
    # SquareFeet (with outliers)
    sqft = np.random.normal(2200, 800)
    if random.random() > 0.97:  # Outliers
        sqft = random.choice([500, 8000, 10000, 300])
    data['SquareFeet'].append(max(400, int(sqft)) if random.random() > 0.06 else np.nan)
    
    # LotSize (acres)
    lot = round(np.random.exponential(0.3), 2)
    data['LotSize'].append(lot if random.random() > 0.12 else np.nan)
    
    # YearBuilt (some invalid years)
    if random.random() > 0.08:
        year = random.randint(1950, 2023)
        if random.random() > 0.95:  # Invalid years
            year = random.choice([1800, 2050, 1900])
        data['YearBuilt'].append(year)
    else:
        data['YearBuilt'].append(np.nan)
    
    # Garage (inconsistent yes/no)
    garage_values = ['Yes', 'No', 'yes', 'no', 'YES', 'Y', 'N', '1', '0', True, False, '', None]
    data['Garage'].append(random.choice(garage_values))
    
    # Pool (similar inconsistency)
    data['Pool'].append(random.choice(garage_values))
    
    # Fireplace
    data['Fireplace'].append(random.choice(garage_values))
    
    # BasementSqFt (many missing)
    if random.random() > 0.4:
        basement = random.randint(0, 1500)
        data['BasementSqFt'].append(basement if random.random() > 0.05 else str(basement))
    else:
        data['BasementSqFt'].append(np.nan)
    
    # Condition
    data['Condition'].append(random.choice(conditions))
    
    # SchoolRating (1-10, some missing)
    data['SchoolRating'].append(random.randint(1, 10) if random.random() > 0.15 else np.nan)
    
    # CrimeRate (per 1000, with outliers)
    crime = max(0, np.random.normal(25, 15))
    if random.random() > 0.98:
        crime = random.choice([0, 150, 200])
    data['CrimeRate'].append(round(crime, 2) if random.random() > 0.1 else np.nan)
    
    # WalkScore (0-100)
    data['WalkScore'].append(random.randint(0, 100) if random.random() > 0.18 else np.nan)
    
    # DistanceToCity (miles)
    dist = abs(np.random.normal(10, 8))
    data['DistanceToCity'].append(round(dist, 1) if random.random() > 0.12 else np.nan)
    
    # NeighborhoodIncome (median)
    income = np.random.normal(75000, 30000)
    data['NeighborhoodIncome'].append(max(20000, int(income)) if random.random() > 0.2 else np.nan)
    
    # PropertyTaxRate (percentage)
    tax = round(np.random.normal(1.2, 0.4), 3)
    data['PropertyTaxRate'].append(max(0.3, tax) if random.random() > 0.15 else np.nan)
    
    # HOAFees (monthly, many NA for single family)
    if random.random() > 0.5:
        hoa = random.randint(0, 500)
        data['HOAFees'].append(hoa if random.random() > 0.05 else str(hoa))
    else:
        data['HOAFees'].append(np.nan)
    
    # DaysOnMarket
    dom = random.randint(1, 180)
    data['DaysOnMarket'].append(dom if random.random() > 0.08 else np.nan)
    
    # PriceReduction (yes/no)
    data['PriceReduction'].append(random.choice(['Yes', 'No', 'yes', 'no', '1', '0', None]))
    
    # ViewCount
    data['ViewCount'].append(random.randint(50, 5000) if random.random() > 0.1 else np.nan)
    
    # SavedCount
    data['SavedCount'].append(random.randint(0, 200) if random.random() > 0.12 else np.nan)
    
    # PreviousPrice (some missing)
    if random.random() > 0.3:
        prev_price = np.random.normal(400000, 150000)
        data['PreviousPrice'].append(max(100000, int(prev_price)))
    else:
        data['PreviousPrice'].append(np.nan)
    
    # SalePrice (TARGET - with some outliers and missing)
    if random.random() > 0.03:
        # Base price calculation with noise
        base_price = 200000
        base_price += data['Bedrooms'][-1] * 50000 if pd.notna(data['Bedrooms'][-1]) else 0
        base_price += data['SquareFeet'][-1] * 150 if pd.notna(data['SquareFeet'][-1]) else 0
        base_price += np.random.normal(0, 80000)
        
        # Outliers
        if random.random() > 0.97:
            base_price = random.choice([50000, 2000000, 5000000])
        
        data['SalePrice'].append(max(50000, int(base_price)))
    else:
        data['SalePrice'].append(np.nan)

# Create DataFrame
df = pd.DataFrame(data)

# Add some duplicate rows (10-15 duplicates)
duplicate_indices = random.sample(range(len(df)), 15)
duplicate_rows = df.iloc[duplicate_indices].copy()
df = pd.concat([df, duplicate_rows], ignore_index=True)

# Shuffle the dataframe
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Save to CSV
df.to_csv('Data.csv', index=False)

print(f"Dataset created with {len(df)} rows and {len(df.columns)} columns")
print(f"\nColumn names:\n{list(df.columns)}")
print(f"\nMissing values:\n{df.isnull().sum()}")
print(f"\nFirst few rows:\n{df.head()}")
print(f"\nDataset saved as 'messy_real_estate_data.csv'")
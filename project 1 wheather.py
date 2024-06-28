# Project Weather


# %%

import pandas as pd

data = pd.read_csv(r"{Locate_Data}")
data

# %%

# How to Analyze Dataframe ?

data.head()


# .shape (number of columns and rows)
data.shape

# %%

# .index  - this attribute provides the index of the dataframe
data.index


# %%

# .columns  - show the name of each columns
data.columns


# %%

# .dtypes - it shows the data-type  of each columns
data.dtypes



# %%

# .unique - in a column, it shows all the unique values. it can be applied on a single columns only, not on the whole dataframe
data['Weather'].unique()


# %%

# .nunique() - it shows the toal no of unique values in each column. it can be applied on a single column as well as on whole dataframe
data.nunique()


# %%

# .count it shows the total no of non-null in each column. it can be applied on a single column as well as on whole dataframe
data.count()

# %%

# .values_counts() in a column, it shows all the unique values with their count. it can be applied on single column only
data['Weather'].value_counts()


# %%

# .provides basic information about dataframe
data.info()


# %% 
#  1 find all uni "Wind Speed" values in the data 
data.columns

data['Wind Speed_km/h'].unique() # Answer

# %%

# 2. Find the number of times when the "Weather is exactly clear"
data.head(2)

data.Weather.value_counts()

# filtering dataset
data[data['Weather'] == 'Clear']

# using group by - the same result filtering  
data.groupby('Weather').get_group('Clear')


# %% 
# 3 Find the number of times when the "Wind Speed was exactly 4km/h"
data.groupby('Wind Speed_km/h').get_group(4) # Answer

# %% 
# 4 Find out all the Null Values in the Data"
data.isnull().sum()
data.isna().sum()
data.notnull().sum() 


#%%

# 5 Rename the column name 'Weather' of the dataframe to 'Weather Condition'
 data.rename(columns = {'Weather': 'Weather Condition'}, inplace = True)
 data.head()

# %%

# 6 what is the mean "Visibility" ?
data['Visibility_km'].mean()

# %%

#  7 What is the Standard Deviation of 'Pressure' in this data ?
 data['Press_kPa'].std()


# %% 

# 8 what's the Variance of 'Relative humidity' in this data ?
data['Rel Hum_%'].var()


# %%

# 9 Find all instances when 'Snow' was recorded
data.groupby('Weather Condition').get_group('Snow')
# or
data['Weather Condition'] == 'Snow'

# str.contains
data[data['Weather Condition'].str.contains('Snow')]

#%%
# 10 Find all instances when 'Wind Speed is above 24' and 'Visibility is 25'
data[(data['Wind Speed_km/h'] > 24) & (data['Visibility_km'] == 25)]


# %%

# 11 what is the minimum & Maximum value of each column against each 'Weather Condition' ?
data.groupby('Weather Condition').min()
data.groupby('Weather Condition').max()


# %%
# 12 Show all the Records where Weather Condition is Fog
data.groupby('Weather Condition').get_group('Fog')


# %%
# 13 Find all Instances when 'Weather is Clear' or 'Visibility is above 40'
data[ (data['Weather Condition'] == 'Clear') | (data['Visibility_km'] > 40)]

# %%

# %%
# 14 Find all instances when :  A: 'Weather is clear' and 'Relative humidity is greater than 50
# Visibility is above 40
data[(data['Weather Condition'] == 'Clear') & (data['Rel Hum_%'] > 50) | (data['Visibility_km'] > 40)] 
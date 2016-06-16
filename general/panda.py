#!/home/ubuntu/workspace/local/bin/python
# several online videos are very helpful: https://www.youtube.com/user/dataschool/videos
# pandas introduces two data structure: Series and Data Frame. They are built on top of Numpy (fast)
import pandas as pd 
import numpy as np

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# A Series is a one-dimensional object similar to an array, list, or 'column in a table'. It will assign a labeled index to each item in the Series. 
# By default, each item will receive an index label from 0 to N, where N is the length of the Series minus one.
a = pd.Series([1, 3, 4, 77, np.nan, 32, np.nan, 8, 45]);      print("Creating a pandas series and let pandas to create default index \n", a)

# Alternatively, you can specify an index to use when creating the Series.
b = pd.Series([7, 'Heisenberg', 3.14, -1789710578, 'Happy Eating!'], index=['A', 'Z', 'C', 'Y', 'E']);    print("User defined index: \n", b)

# The Series constructor can convert a dictonary as well, using the keys of the dictionary as its index.
c = {'Chicago': 1000, 'New York': 1300, 'Portland': 900, 'San Francisco': 1100, 'Austin': 450, 'Boston': None}; d=pd.Series(c); print("Series on Dict\n", d)
print("Select a specific item from a Series: d['Chicago']\n", d['Chicago']);    d['Chicago']=2100;  print("So you could use this for setting values\n", d); 
print("Using list indexing to obtain a subset of a Series\n", d[['Chicago', 'Portland', 'San Francisco']])
print("Using boolean indexing (a list of T or F): d[d < 1000]\n", d[d < 1000]);    d[d<1000] = 750;    print("Change values using boolean indexing:\n", d)
print("To check if an item is on the list, only check the index(keys)\n", 'Seattle' in d, " and ", 'Chicago' in d)
print("Mathematical operations can be done using scalars and functions. d/3 \n", d/3, " or square ", np.square(d))

# You can add two Series together, which returns a union of the two Series with the addition occurring on the shared index values. 
# Values on either Series that did not have a shared index will produce a NULL/NaN (not a number). NULL checking is done with isnull() and notnull().
print(d[['Chicago', 'New York', 'Portland']], "\n");    print(d[['Austin', 'New York']], "\n");   
print(d[['Chicago', 'New York', 'Portland']] + d[['Austin', 'New York']])   # both Series have 'New York', so its value combined. All others will be NaN
print("Test null using isnull()\n", d[d.isnull()])
print()

# Data Frame
# A DataFrame is a tablular data structure comprised of rows and columns, akin to a spreadsheet, database table, or R's data.frame object. 
# To create a DataFrame out of common Python data structures, we can pass a dictionary of lists to the DataFrame constructor.
data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012], 'wins': [11, 8, 10, 15, 11, 6, 10, 4],
        'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions', 'Lions', 'Lions'], 'losses': [5, 8, 6, 1, 5, 10, 6, 12]}
fb = pd.DataFrame(data, columns=['year', 'team', 'wins', 'losses']);    print("Created a data frame using dictionary by user defined column order\n", fb)

# Much more often, you'll have a dataset you want to read into a DataFrame. Let's go through several common ways of doing so.
# read csv file using read_csv()
hpi = pd.read_csv('newcsv.csv');       print("Read data from a csv file hpi = pd.read_csv('newcsv.csv')\n", hpi.head())

# There's also a set of writer functions for writing to a variety of formats (CSVs, HTML tables, JSON). 
hpi.to_json('hpi.JSON');        print("Writing data frame to a file in json format pd.to_json(hpi)")
del hpi;    hpn = pd.read_json('hpi.JSON');   print("Delete the hpi file and the re-read it from the JSON file\n", hpn.tail())
print()

dates = pd.date_range('20130303', periods = 6);     print("Creating a pandas date periods, \n", dates)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'));     
print("Creating a DataFrame by passing a numpy array, with a datetime index and labeled columns::\n ");   print(df)

df2 = pd.DataFrame({ 'A' : 1., 'B' : pd.Timestamp('20130102'), 'C' : pd.Series(1,index=list(range(4)),dtype='float32'), 
                     'D' : np.array([3] * 4,dtype='int32'), 'E' : pd.Categorical(["test","train","test","train"]), 'F' : 'foo' })
print("Creating a DataFrame by passing a dict of objects that can be converted to series-like data frame: \n");   print(df2)
print("Checking data type df2.dtypes\n", df2.dtypes);      print("There are tons of attributes associated with data frame")

# there are tons of attributes and functions associated with pandas data frame
print("Print the first few rows: df.head()\n ", df.head());      print("Print the last few sample: df.tail() \n", df.tail(2))
print("Display index only df.index \n", df.index);    print("Display column names only, df.columns \n", df.columns); print("Display internal values df.vallue\n", df.values)
print("describe shows a quick summary of your data. df.describe() \n", df.describe());    print("you can transpose the data, df.T: \n", df.T)
print("sort by axis df.sort_index(axis=1, ascending=False)\n", df.sort_index(axis=1, ascending=False))
print("sorting by values df.sort_values(by='B')\n", df.sort_values(by='B'))

# data frame indexing and slicing
print("Get column 'A': df['A']\t", df['A']);    print("slicing data frame df[:3]\n", df[:2]);   
print("More splicing using row index: df['20130303':'20130305']\n", df['20130303':'20130305']);
print("To get a cross section using labels: df.loc[dates[0]]\n", df.loc[dates[0]])
print("Selection of multiple axis using label: df.loc[:,['A','C']]\n", df.loc[:,['A','C']]);
print("Reduction in the dimensions of the returned object: \n", df.loc['20130303',['A', 'D']]);
print("for getting a scalar value: df.loc[dates[0], 'A']\n", df.loc[dates[0], 'A']);    print("Or using at[], df.at[dates[0], 'A']\n", df.at[dates[0], 'A'])
print("Selecting using iloc[], indexing location using int: df.iloc[3,2]\n", df.iloc[3,2])
print("Selecting entire row: df.iloc[3]\n", df.iloc[3]);    print("or entire column: df.iloc[:, 2]\n", df.iloc[:,2])
print("Like python/numpy, using indexing slicing: df.iloc[:2, 1:3]\n", df.iloc[:2,1:3])
print("specify detailed indexing: df.iloc[[1,2,4], [0:2]]\n", df.iloc[[1,2,4], [0,2]])
print("Slicing row explicitly: df.iloc[1:3]\n", df.iloc[1:3, :]);   print("Slicing column explicitly: df.iloc[:, 0:2]\n", df.iloc[:, 0:2]);     
print("Get a value explicitly: df.iloc[1,2]\n", df.iloc[1,2]);      print("getting a value explicitly using iat(): df.iat[1,2]\n", df.iat[1,2])
print("Using Boolean value for selection: df[df.A > 0]\n", df[df.A>0]);     print("A 'where' operation for getting. df[df > 0]\n", df[df > 0])

# setting data
s1 = pd.Series([1,2,3,4,5,6], index=pd.date_range('20130303', periods=6));   print("Setting a new column automatically aligns the data by the indexes\n", s1)
df['F'] = s1;   print("Expanding the data frame df by setting 'F' column: df['F']=s1\n", df)
df.at[dates[0], 'A'] = 0;   df.iat[0,1] = 0;    df.loc[:, 'D'] = np.array([5] * len(df));   print("Different setting operations: \n", df)
df2 = df.copy;  print("Deep copy of a data frame: df2 = df.copy\n", df2);    #df2[df2 > 0] = -df2;   print("resetting df2 to negatives \n", df2)

# Missing Data: pandas primarily uses the value np.nan to represent missing data. It is by default not included in computations.
df1 = df.reindex(index=dates[0:6], columns=list(df.columns) + ['E']);    df1.loc[dates[0]:dates[1], 'E'] = 1;  print("new df with np.nan\n", df1) 
print("To drop any rows that have missing data. df.dropna(how='any')\n", df1.dropna(how='any'))
print("Filling missing data: df1.fillna(value=5)\n", df1.fillna(value=5));
print("To get the boolean mask where values are nan: pd.isnull(df1)\n", pd.isnull(df1))

# data frame operations
print("data frame mean df.mean()\n", df.mean());    print("mean in a data frame with missing data: df1.mean()\n", df1.mean())
print("Same operation in the other axis (ie row): df.mean(1)\n", df.mean(1))

# There are two way to join/merge two data frame, row combine or column combine
# 

print("")
#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd  # keywords are highlighted in green, other strings in red, etc.
import numpy as np


# In[ ]:





# In[34]:


# Reading data into a DataFrame
import pandas as pd
import numpy as np

file1 = pd.read_csv('file1.csv')
display(file1.head())
display(file1.tail())
file1.shape


# In[31]:


file1


# In[6]:


file2 = pd.read_csv('file2.txt')  # what is happening?
file2.shape


# In[7]:


file2 = pd.read_csv('file2.txt', sep='\t') # | \ / , \t
file2.head()


# In[35]:


# Data blending
column_names = file1.columns
column_names


# In[36]:


data = pd.concat([file1, file2], axis=0) #discuss axis here
data.shape
data


# In[ ]:


# weird_data = pd.concat([file1, file2], axis=1) #axis wrong
# weird_data


# In[ ]:


data.columns[16].lower()


# In[37]:


cols = []
for i in range(len(data.columns)):
    cols.append(data.columns[i].lower())
data.columns = cols

# alternative for using range(len(list)) in the for loop:
cols = []
for column in data.columns:
    cols.append(column.lower())
data.columns = cols

# renaming columns
data = data.rename(columns={'controln':'id',
                            'hv1':'median_home_val', 
                            'ic1':'median_household_income'})
data.head()
# #data.shape


# In[ ]:


#Activity 1


# In[18]:


import pandas as pd
import numpy as np

file3 = pd.read_excel('file3.xlsx')
file4 = pd.read_excel('file4.xlsx')
display(file3.head())
display(file3.tail())
file3.shape
display(file4.head())
display(file4.tail())

file4.shape


# In[17]:



file3 = pd.read_excel('file3.xlsx')
file4 = pd.read_excel('file4.xlsx')
display(file3.columns)
display(file3.columns)
#file3.shape


# In[19]:


data = pd.concat([file3, file4], axis=0) #discuss axis here
data.shape
data


# In[21]:


myCol = []
for column in data.columns:
    myCol.append(column.lower())
data.columns = myCol

# renaming columns
data = data.rename(columns={'controln':'id',
                            'hv1':'median_home_val', 
                            'ic1':'median_household_income'})
data.head()


# In[ ]:





# In[ ]:



#End of Activity 1


# In[ ]:


data.head()


# In[ ]:


#slicing
data.loc[[0,1,2],['id','state']]


# In[ ]:


#slicing
data.loc[[0,1,2],:]


# In[ ]:


#slicing
data.loc[:,['id','state']]


# In[ ]:


#slicing shortcut
data[['id','state']]


# In[ ]:


#also useful to reorder columns
data[['state','id']]


# In[ ]:


data.head()


# In[ ]:


#another shortcut
data['gender']


# In[ ]:


#watch out for mutability
just_gender = data['gender']
just_gender[1012]
#just_gender


# In[ ]:


just_gender[1012] = 'F'
just_gender


# In[ ]:


#whoah!
data


# In[ ]:


just_gender_copied = data['gender'].copy()
just_gender_copied[1014]


# In[ ]:


just_gender_copied[1014] = 'F'
just_gender_copied


# In[ ]:


#Now we have what we want:
data


# In[ ]:


#operations between columns
#% income donated
data['target_d']/data['median_household_income']


# In[ ]:


#new columns
data['percent_income_donated'] = data['target_d']/data['median_household_income']
data.head()


# In[ ]:


#boolean masks
data['very_generous'] = data['percent_income_donated']>0.25
data.head()


# In[ ]:


#filtering!
data[data['very_generous']==True]


# In[ ]:


#filtering!
data[data['target_d']==100]


# In[ ]:


#combining filters
#filtering!
data[(data['target_d']==100) & (data['very_generous']) ]


# In[ ]:


data[(data['state'].isin(['FL','Florida']))  & (data['avggift']<50)]


# In[ ]:





# In[ ]:


# deleting columns: how to
data = data.drop(['tcode','percent_income_donated','very_generous'], axis=1)
data.head()


# In[ ]:


data1 = data.copy()


# In[ ]:


data1 = data1.drop([0,1], axis=0)
data1.head()


# In[ ]:


#data1.loc[[0,1],:]


# In[ ]:


# # deleting columns: how to
# data = data.drop(['tcode'], axis =1) # Explain the argument axis, when axis is 0 and 1

# # Rearranging columns: how to
data = data[['id', 'state', 'gender', 'median_home_val', 'median_household_income', 'ic2', 'ic3', 'ic4', 'ic5', 'avggift', 'domain', 'dob', 'target_d']]


# In[ ]:


data.head()


# In[ ]:


#Activity 2
#1


# In[ ]:


# 2


# In[ ]:


# 3



# In[ ]:


# 4


# In[ ]:


# 5

# End of Activity 2


# In[ ]:


#filter and reset the index
# important to play with the code and check the output
filtered = data[data['gender']=='M']  # Lets say that we are working on this filtered data
filtered


# In[ ]:


data.loc[1]


# In[ ]:


# issue on the index
#filtered.loc[1]
filtered.loc[3]


# In[ ]:


filtered = filtered.reset_index(drop=True)
filtered= filtered.drop(['index'], axis=1)
filtered


# In[ ]:


temp = filtered.copy()
temp = temp.set_index('state') # This is a dummy case, but indexes should be unique and not nulls, usually auto-increments by 1
temp.head()


# In[ ]:


filtered[filtered['state']=='FL']


# In[ ]:


# Working with indexes
filtered[1:4]
filtered[['gender', 'ic2', 'ic3']][0:10]
filtered.loc[0:10,['gender', 'ic2', 'ic3']]
filtered.loc[1:4]
# filtered.loc[100]
filtered.iloc[1:4]


# In[ ]:


# now, working just on the indexes row,columns
filtered.iloc[0:10,0:4]
filtered.iloc[[1,2,3,4],[0,2,4]]


# In[ ]:


#Activity 3
# 1 Filter the results where the gender is F 
#   and store the results in another DataFrame filtered2


# In[ ]:


# 2 Check the first 10 rows of the DataFrame using the head() function.


# In[ ]:


# 3 Reset the index of filtered2 with and without using the parameter drop=True 
#   and check the difference in the results.


# In[ ]:


# 4 Show the rows from index number 100 to 200.


# In[ ]:


# 5 Use iloc to get the first 100 rows and columns with indexes 2,3,4,5.


#End of Activity 3


# In[ ]:


# data types
data.dtypes
# data._get_numeric_data()
# data._get_bool_data()
# data.select_dtypes(['int64','float64'])


# In[ ]:


# correcting data types
data['median_home_val'] =  pd.to_numeric(data['median_home_val'], errors='coerce')
data['ic5'] =  pd.to_numeric(data['ic5'], errors='coerce')
data.head(20)

#data._get_numeric_data() # to check if 'median_home_val' and 'ic5' are now listed as numeric data


# In[ ]:


# Removing duplicates
print(data.shape)
data2 = data.copy()
data2 = data2.drop_duplicates()  # nb keep argument
# #if we want to remove duplicates based on some specific columns
# data2 = data2.drop_duplicates(subset=['state','gender', 'ic2', 'ic3'])
data2 = data2.drop_duplicates(subset=['state','gender', 'ic2', 'ic3'],keep='last')
# #data2
print(data2.shape)


# In[ ]:


# Activity 4

# 1 Check the data types of all the columns in the DataFrame.


# In[ ]:





# In[ ]:


# 2 Use select_dtypes() to select all the numerical columns in the DataFrame (both integers and floats).


# In[ ]:


# 3 Convert the columns that have numerical values (which are now object types) to the numeric type.


# In[ ]:


# 4 Remove duplicates from the DataFrame if any.


# In[28]:



import pandas as pd

file1 = pd.read_csv('./file1.csv')
file2 = pd.read_csv('./file2.txt', sep = '\t')
file3 = pd.read_excel('./file3.xlsx', engine="openpyxl")
file4 = pd.read_excel('./file4.xlsx', engine="openpyxl")
column_names = file1.columns
donors = pd.DataFrame(columns=column_names)
donors = pd.concat([file1,file2,file3,file4], axis=0)
cols = []
for colname in donors.columns:
    cols.append(colname.lower())
donors.columns = cols
donors = donors.rename(columns={'controln':'id',
                                'hv1':'median_home_val', 
                                'ic1':'median_household_income'})
donors['median_home_val'] =  pd.to_numeric(donors['median_home_val'], errors='coerce')
donors['ic5'] =  pd.to_numeric(donors['ic5'], errors='coerce')
donors = donors.drop_duplicates()

donors.shape


# In[ ]:


donors.dtypes
donors


# In[ ]:


donors.isna().sum()
round(donors.isna().sum()/len(donors),4)*100  # shows the percentage of null values in a column
nulls_df = pd.DataFrame(round(donors.isna().sum()/len(donors),4)*100)
nulls_df
nulls_df = nulls_df.reset_index()
nulls_df
nulls_df.columns = ['header_name', 'percent_nulls']
nulls_df


# In[ ]:


columns_drop = nulls_df[nulls_df['percent_nulls']>3]['header_name']  # dummy case with 3
print(columns_drop.values)
#donors = donors.drop(columns_drop, axis=1)  # drop a list of columns DO NOT RUN THIS
#donors = donors.drop(['gender'], axis=1)  # drop a single column DO NOT RUN THIS


# In[ ]:


# Replacing/imputing null values
donors[donors['gender'].isna()==True].head(60) # checking rows that are null based on a specific column


# In[ ]:


# drop rows that have null values (only if there are very few)
donors = donors[donors['ic2'].isna()==False] # Since these nulls are not a lot, we can filter them

donors.isna().sum()


# In[ ]:


# impute a value for the missing value (fill in a value that we choose or calculate)
# import numpy
import numpy as np

mean_median_home_value = donors['median_home_val'].mean()
mean_median_home_value
donors['median_home_val'] = donors['median_home_val'].fillna(mean_median_home_value)


# In[ ]:


donors.isna().sum()


# In[ ]:


#Activity 1


# In[ ]:





# In[ ]:


#End of Activity 1


# In[ ]:


# Replacing null values for categorical variables
donors['gender'].unique()
donors['gender'].value_counts()

donors['gender'].value_counts(dropna=False)
#len(donors[donors['gender'].isna()==True])  # number of missing values


# In[ ]:


# use most common value to fillna
donors['gender'] = donors['gender'].fillna('F')
len(donors[donors['gender'].isna()==True]) # now this number is 0


# In[ ]:


# Exporting this processed data to a csv
donors.to_csv('merged_clean_ver1.csv') # you can find this file inside files_for_lesson_and_activities folder


# In[ ]:


# lambda expressions

def add_two(x):
    #some code
    return x+2

# def do_something(lst,fun):
#      #some code
#      return result

# do_something([1,2,3],add_two)

add_two(4)


# In[ ]:




y = lambda x: x+2
y(2)

square = lambda x: x*x
square(4)

addition = lambda x,y : x+y
addition(1,5)

# lst = [1,2,3,4,5,6,7,8,10]
# new_list = []
# for item in lst:
#     new_list.append(square(item))
# new_list

# new_list = [square(item) for item in lst] # list comprehension
# print(new_list)

# # new_list = [square(item) for item in lst if item%2==0]


# In[ ]:


#Activity 2


# In[ ]:


# Refer to the file files_for_activities/merged_clean_ver1.csv for this exercise.

#1 Import the data from merged_clean_ver1.csv as a dataframe. There would be a column with the sequence of numbers (to the left of column id). Drop that column(s).


# In[ ]:





# In[ ]:


# 2 Check the column state for null values. Replace those null values with the state that is represented largest number of times in that column


# In[ ]:


# 3.1 Create a simple lambda expression to add three numbers. Take those three numbers as input from the user.


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


# 3.2 Define a list as lst = [1,2,3,4,5,6,7,8,10]. 
#     Write a lambda expression to find the cube of a number.
#     Use that lambda expression to find the cube of every number in the list. 
#     Define a list comprehension for this question


# In[ ]:





# In[ ]:


#End of Activity 2


# In[ ]:


# map functions
#list(map(print, donors.columns))
#donors.columns = list(map(lambda x: x.lower(), donors.columns)) # we did this with a for loop earlier
# # donors
donors['gender'].unique() # check the unique values in the column
donors['gender'] = list(map(lambda x: x.upper(), donors['gender']))
donors['gender'].unique()


# In[ ]:


donors['gender'].unique()  # check the unique elements in the column
# Now define a function to clean the column
def clean(x):
    if x in ['M', 'MALE']:
        return 'Male'
    elif x.startswith('F'):
        return 'Female'
    else:
        return 'U'

donors['gender'] = list(map(clean, donors['gender']))
donors['gender'].unique()  # To check the results again
donors


# In[ ]:





# In[ ]:





# In[ ]:


#Activity 3



# End of Activity 3


# In[ ]:


# Examples of working with datetime format:

file = pd.read_csv('df_final_web_data_pt_1.csv')
file.dtypes

file['date_time'] = pd.to_datetime(file['date_time'], errors='coerce')
file.dtypes


# In[ ]:


file['date_time'][0].day
# file['date_time'][0].month
# file['date_time'][0].year
# file['date_time'][0].isoweekday()  # Returns 1 for Monday and so on

# file['date_time'][0].time()
# file['date_time'][0].isoweekday()
# file['date_time'][0].isoformat()
# file['date_time'][0].strftime(format='%d-%m-%Y')
file['date_time'][0].strftime(format="%A %d. %B %Y")


# In[ ]:


import time
from datetime import date

today = date.today()
today

# time.localtime(time.time())
# time.gmtime(time.time())


# In[ ]:


# Examples of working with string functions

string = " I am learning  data  analysis at Ironhack  . It is  super easy "
string.lower
string.upper()
'34'.isdigit() # does not work with decimal numbers
str2 = '42'
str2.isdigit()
string = string.lstrip()
string.rstrip()
string.split()
string.split('.')
string.replace('%', '')


# In[ ]:


#Acticity 4
# Create a user-defined method to clean the column state in the dataframe.
# Use string functions to standardize the states to uppercase and use the strip function to clean the strings as well.


# In[ ]:





# In[ ]:


#End Activity 4


# In[ ]:


# Exporting this processed data to a csv
donors.to_csv('merged_clean_ver2.csv') 


# In[ ]:





# In[ ]:





# In[ ]:





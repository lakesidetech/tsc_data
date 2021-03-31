#!/usr/bin/env python
# coding: utf-8

# In[44]:


# Import required libraries
import sqlite3
import pandas as pd
import webbrowser


# ## Steps to get from Pandas DataFrame to SQL
# 

# # Step 1: Create a DataFrame
# 

# In[63]:


# # Read data from the CSV files
# encoding="ISO-8859-1" so that pandas can properly read the CSV
tsc_data= pd.read_csv("C:\\Users\\user\\Desktop\\python-files\\teacher_by_status_and_county_for_secondary (1).csv")

print(tsc_data)


# # Step 2 Clean Up Data

# In[72]:


## Display Dataframe Columns
tsc_data.columns


# In[73]:


#access row rames
tsc_data.index


# In[74]:


## Display Dataframe Values - get Numpy Array represention of your dataset
tsc_data.values


# ## Drop a column using pandas - County (centroid)
# 

# In[64]:


tsc_data.drop('County (centroid)',axis=1,inplace=True)
tsc_data.head()


# # Step 3 Create a database in SQlite3

# In[65]:


# Connect to SQLite database
conn=sqlite3.connect('tsc_info.db')
cur = conn.cursor()
print('tsc_info.db create successfully')


# # Step 4 create a table

# In[66]:


cur.execute('CREATE TABLE TEACHERS (County text, School_type text,Employment_Body text,Num_Of_teachers int,Year date)')
conn.commit()
print('teachers table created successfully')


# ### The teachers table will be used to store the teachers information from the DataFrame.
# 
# 

# ## Step 3: Get from Pandas DataFrame to SQL
# 

# In[68]:


tsc_data.to_sql('TEACHERS', conn, if_exists='replace', index = False)
 
cur.execute('''SELECT * FROM TEACHERS''')

for row in cur.fetchall():
    print (row)


# # Step 5 Output on HTML

# In[69]:


p = []
table_data = f"<tr><td>County</td><td>School_Type</td><td>Employment_Body</td>"         f"<td>Number_Of_Teachers</td><td>County(Centroid)</td><td>Year</td></tr>"
p.append(table_data)
# Create a cursor object
cur = conn.cursor()
# Fetch and display result
x=cur.execute('SELECT * FROM teachers2')
for row in x:
	#print(row)

    a = "<tr><td>%s</td>" % row[0]
    p.append(a)
    b = "<td>%s</td>" % row[1]
    p.append(b)
    c = "<td>%s</td>" % row[2]
    p.append(c)
    d = "<td>%s</td>" % row[3]
    p.append(d)
    e = "<td>%s</td>" % row[4]
    p.append(e)
    g = "<td>%s</td></tr>" % row[5]
    p.append(g)


# In[70]:


html = tsc_data.to_html("index.html") 
# Create index.html to write html on it
tsc_f = open("index.html","r+")
tsc_f.close()

    # Open file in browser
webbrowser.open_new_tab('index.html')


# ### Display the first 5 records

# In[71]:


tsc_data.head(5)


# In[75]:


#display a single column
tsc_data['COUNTY']


# In[76]:


#place this in a variable 
our_county=tsc_data['COUNTY']
#identify type
type(our_county)


# In[77]:


#list 5  counties using a variable
our_county.head(5)


# In[ ]:





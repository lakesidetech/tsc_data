# tsc_data
## Use python pandas to read and convert to Dataframes and then stores then convert the Dataframe to SQliteDB. The Outputs renders on HTML
## Prerequisite
* Install Sqlite3
* Python 3
## import libraries
* import panda as pd
* import webbrowers

```python
# Import required libraries
import sqlite3
import pandas as pd
import webbrowser


```

## Steps to get from Pandas DataFrame to SQL


# Step 1: Create a DataFrame



```python
# # Read data from the CSV files
# encoding="ISO-8859-1" so that pandas can properly read the CSV
tsc_data= pd.read_csv("C:\\Users\\user\\Desktop\\python-files\\teacher_by_status_and_county_for_secondary (1).csv")

print(tsc_data)
```

                  COUNTY School Type Employment Body  No. of Teachers  \
    0    Baringo             Public          TSC                 1172   
    1    Bomet               Public          TSC                 1379   
    2    Bungoma             Public          TSC                 2946   
    3    Busia               Public          TSC                 1182   
    4    Elgeyo Marakwet     Public          TSC                 1087   
    ..               ...         ...             ...              ...   
    187  Uasin Gishu         Private         TSC                    0   
    188  Vihiga              Private         TSC                    0   
    189  Wajir               Private         TSC                    0   
    190  West Pokot          Private         TSC                    0   
    191  Kenya               Private         TSC                    0   
    
              County (centroid)                    Year  
    0     (0.669252, 35.946465)  12/31/2014 12:00:00 AM  
    1    (-0.726295, 35.298598)  12/31/2014 12:00:00 AM  
    2     (0.749285, 34.640461)  12/31/2014 12:00:00 AM  
    3     (0.387444, 34.193631)  12/31/2014 12:00:00 AM  
    4     (0.802219, 35.536563)  12/31/2014 12:00:00 AM  
    ..                      ...                     ...  
    187   (0.526086, 35.322012)  12/31/2014 12:00:00 AM  
    188   (0.076266, 34.722323)  12/31/2014 12:00:00 AM  
    189   (1.808138, 40.034986)  12/31/2014 12:00:00 AM  
    190   (1.740106, 35.243847)  12/31/2014 12:00:00 AM  
    191                     NaN  12/31/2014 12:00:00 AM  
    
    [192 rows x 6 columns]
    

# Step 2 Clean Up Data


```python
## Display Dataframe Columns
tsc_data.columns
```




    Index(['COUNTY', 'School Type', 'Employment Body', 'No. of Teachers', 'Year'], dtype='object')




```python
#access row rames
tsc_data.index
```




    RangeIndex(start=0, stop=192, step=1)




```python
## Display Dataframe Values - get Numpy Array represention of your dataset
tsc_data.values
```




    array([['Baringo        ', 'Public ', 'TSC    ', 1172,
            '12/31/2014 12:00:00 AM'],
           ['Bomet          ', 'Public ', 'TSC    ', 1379,
            '12/31/2014 12:00:00 AM'],
           ['Bungoma        ', 'Public ', 'TSC    ', 2946,
            '12/31/2014 12:00:00 AM'],
           ['Busia          ', 'Public ', 'TSC    ', 1182,
            '12/31/2014 12:00:00 AM'],
           ['Elgeyo Marakwet', 'Public ', 'TSC    ', 1087,
            '12/31/2014 12:00:00 AM'],
           ['Embu           ', 'Public ', 'TSC    ', 1491,
            '12/31/2014 12:00:00 AM'],
           ['Garissa        ', 'Public ', 'TSC    ', 347,
            '12/31/2014 12:00:00 AM'],
           ['Homa Bay       ', 'Public ', 'TSC    ', 2069,
            '12/31/2014 12:00:00 AM'],
           ['Isiolo         ', 'Public ', 'TSC    ', 180,
            '12/31/2014 12:00:00 AM'],
           ['Kajiado        ', 'Public ', 'TSC    ', 753,
            '12/31/2014 12:00:00 AM'],
           ['Kakamega       ', 'Public ', 'TSC    ', 3558,
            '12/31/2014 12:00:00 AM'],
           ['Kericho        ', 'Public ', 'TSC    ', 1551,
            '12/31/2014 12:00:00 AM'],
           ['Kiambu         ', 'Public ', 'TSC    ', 4288,
            '12/31/2014 12:00:00 AM'],
           ['Kilifi         ', 'Public ', 'TSC    ', 1081,
            '12/31/2014 12:00:00 AM'],
           ['Kirinyaga      ', 'Public ', 'TSC    ', 1478,
            '12/31/2014 12:00:00 AM'],
           ['Kisii          ', 'Public ', 'TSC    ', 3863,
            '12/31/2014 12:00:00 AM'],
           ['Kisumu         ', 'Public ', 'TSC    ', 2213,
            '12/31/2014 12:00:00 AM'],
           ['Kitui          ', 'Public ', 'TSC    ', 2292,
            '12/31/2014 12:00:00 AM'],
           ['Kwale          ', 'Public ', 'TSC    ', 710,
            '12/31/2014 12:00:00 AM'],
           ['Laikipia       ', 'Public ', 'TSC    ', 1029,
            '12/31/2014 12:00:00 AM'],
           ['Lamu           ', 'Public ', 'TSC    ', 210,
            '12/31/2014 12:00:00 AM'],
           ['Machakos       ', 'Public ', 'TSC    ', 2849,
            '12/31/2014 12:00:00 AM'],
           ['Makueni        ', 'Public ', 'TSC    ', 2765,
            '12/31/2014 12:00:00 AM'],
           ['Mandera        ', 'Public ', 'TSC    ', 432,
            '12/31/2014 12:00:00 AM'],
           ['Marsabit       ', 'Public ', 'TSC    ', 233,
            '12/31/2014 12:00:00 AM'],
           ['Meru           ', 'Public ', 'TSC    ', 2819,
            '12/31/2014 12:00:00 AM'],
           ['Migori         ', 'Public ', 'TSC    ', 1429,
            '12/31/2014 12:00:00 AM'],
           ['Mombasa        ', 'Public ', 'TSC    ', 648,
            '12/31/2014 12:00:00 AM'],
           ['Muranga        ', 'Public ', 'TSC    ', 3455,
            '12/31/2014 12:00:00 AM'],
           ['Nairobi        ', 'Public ', 'TSC    ', 2035,
            '12/31/2014 12:00:00 AM'],
           ['Nakuru         ', 'Public ', 'TSC    ', 3015,
            '12/31/2014 12:00:00 AM'],
           ['Nandi          ', 'Public ', 'TSC    ', 1473,
            '12/31/2014 12:00:00 AM'],
           ['Narok          ', 'Public ', 'TSC    ', 723,
            '12/31/2014 12:00:00 AM'],
           ['Nyamira        ', 'Public ', 'TSC    ', 1786,
            '12/31/2014 12:00:00 AM'],
           ['Nyandarua      ', 'Public ', 'TSC    ', 1355,
            '12/31/2014 12:00:00 AM'],
           ['Nyeri          ', 'Public ', 'TSC    ', 2501,
            '12/31/2014 12:00:00 AM'],
           ['Samburu        ', 'Public ', 'TSC    ', 288,
            '12/31/2014 12:00:00 AM'],
           ['Siaya          ', 'Public ', 'TSC    ', 1861,
            '12/31/2014 12:00:00 AM'],
           ['Taita Taveta   ', 'Public ', 'TSC    ', 707,
            '12/31/2014 12:00:00 AM'],
           ['Tana River     ', 'Public ', 'TSC    ', 183,
            '12/31/2014 12:00:00 AM'],
           ['Tharaka-Nithi  ', 'Public ', 'TSC    ', 1295,
            '12/31/2014 12:00:00 AM'],
           ['Trans Nzoia    ', 'Public ', 'TSC    ', 1340,
            '12/31/2014 12:00:00 AM'],
           ['Turkana        ', 'Public ', 'TSC    ', 255,
            '12/31/2014 12:00:00 AM'],
           ['Uasin Gishu    ', 'Public ', 'TSC    ', 1361,
            '12/31/2014 12:00:00 AM'],
           ['Vihiga         ', 'Public ', 'TSC    ', 1668,
            '12/31/2014 12:00:00 AM'],
           ['Wajir          ', 'Public ', 'TSC    ', 408,
            '12/31/2014 12:00:00 AM'],
           ['West Pokot     ', 'Public ', 'TSC    ', 431,
            '12/31/2014 12:00:00 AM'],
           ['Kenya          ', 'Public ', 'TSC    ', 72194,
            '12/31/2014 12:00:00 AM'],
           ['Baringo        ', 'Public ', 'SMC    ', 608,
            '12/31/2014 12:00:00 AM'],
           ['Bomet          ', 'Public ', 'SMC    ', 1261,
            '12/31/2014 12:00:00 AM'],
           ['Bungoma        ', 'Public ', 'SMC    ', 1745,
            '12/31/2014 12:00:00 AM'],
           ['Busia          ', 'Public ', 'SMC    ', 903,
            '12/31/2014 12:00:00 AM'],
           ['Elgeyo Marakwet', 'Public ', 'SMC    ', 454,
            '12/31/2014 12:00:00 AM'],
           ['Embu           ', 'Public ', 'SMC    ', 678,
            '12/31/2014 12:00:00 AM'],
           ['Garissa        ', 'Public ', 'SMC    ', 80,
            '12/31/2014 12:00:00 AM'],
           ['Homa Bay       ', 'Public ', 'SMC    ', 1566,
            '12/31/2014 12:00:00 AM'],
           ['Isiolo         ', 'Public ', 'SMC    ', 31,
            '12/31/2014 12:00:00 AM'],
           ['Kajiado        ', 'Public ', 'SMC    ', 210,
            '12/31/2014 12:00:00 AM'],
           ['Kakamega       ', 'Public ', 'SMC    ', 2139,
            '12/31/2014 12:00:00 AM'],
           ['Kericho        ', 'Public ', 'SMC    ', 1119,
            '12/31/2014 12:00:00 AM'],
           ['Kiambu         ', 'Public ', 'SMC    ', 882,
            '12/31/2014 12:00:00 AM'],
           ['Kilifi         ', 'Public ', 'SMC    ', 893,
            '12/31/2014 12:00:00 AM'],
           ['Kirinyaga      ', 'Public ', 'SMC    ', 508,
            '12/31/2014 12:00:00 AM'],
           ['Kisii          ', 'Public ', 'SMC    ', 1283,
            '12/31/2014 12:00:00 AM'],
           ['Kisumu         ', 'Public ', 'SMC    ', 1062,
            '12/31/2014 12:00:00 AM'],
           ['Kitui          ', 'Public ', 'SMC    ', 1544,
            '12/31/2014 12:00:00 AM'],
           ['Kwale          ', 'Public ', 'SMC    ', 414,
            '12/31/2014 12:00:00 AM'],
           ['Laikipia       ', 'Public ', 'SMC    ', 289,
            '12/31/2014 12:00:00 AM'],
           ['Lamu           ', 'Public ', 'SMC    ', 85,
            '12/31/2014 12:00:00 AM'],
           ['Machakos       ', 'Public ', 'SMC    ', 1405,
            '12/31/2014 12:00:00 AM'],
           ['Makueni        ', 'Public ', 'SMC    ', 1449,
            '12/31/2014 12:00:00 AM'],
           ['Mandera        ', 'Public ', 'SMC    ', 104,
            '12/31/2014 12:00:00 AM'],
           ['Marsabit       ', 'Public ', 'SMC    ', 50,
            '12/31/2014 12:00:00 AM'],
           ['Meru           ', 'Public ', 'SMC    ', 1470,
            '12/31/2014 12:00:00 AM'],
           ['Migori         ', 'Public ', 'SMC    ', 1375,
            '12/31/2014 12:00:00 AM'],
           ['Mombasa        ', 'Public ', 'SMC    ', 175,
            '12/31/2014 12:00:00 AM'],
           ['Muranga        ', 'Public ', 'SMC    ', 951,
            '12/31/2014 12:00:00 AM'],
           ['Nairobi        ', 'Public ', 'SMC    ', 416,
            '12/31/2014 12:00:00 AM'],
           ['Nakuru         ', 'Public ', 'SMC    ', 1387,
            '12/31/2014 12:00:00 AM'],
           ['Nandi          ', 'Public ', 'SMC    ', 1170,
            '12/31/2014 12:00:00 AM'],
           ['Narok          ', 'Public ', 'SMC    ', 472,
            '12/31/2014 12:00:00 AM'],
           ['Nyamira        ', 'Public ', 'SMC    ', 668,
            '12/31/2014 12:00:00 AM'],
           ['Nyandarua      ', 'Public ', 'SMC    ', 644,
            '12/31/2014 12:00:00 AM'],
           ['Nyeri          ', 'Public ', 'SMC    ', 640,
            '12/31/2014 12:00:00 AM'],
           ['Samburu        ', 'Public ', 'SMC    ', 42,
            '12/31/2014 12:00:00 AM'],
           ['Siaya          ', 'Public ', 'SMC    ', 1196,
            '12/31/2014 12:00:00 AM'],
           ['Taita Taveta   ', 'Public ', 'SMC    ', 300,
            '12/31/2014 12:00:00 AM'],
           ['Tana River     ', 'Public ', 'SMC    ', 75,
            '12/31/2014 12:00:00 AM'],
           ['Tharaka-Nithi  ', 'Public ', 'SMC    ', 601,
            '12/31/2014 12:00:00 AM'],
           ['Trans Nzoia    ', 'Public ', 'SMC    ', 971,
            '12/31/2014 12:00:00 AM'],
           ['Turkana        ', 'Public ', 'SMC    ', 144,
            '12/31/2014 12:00:00 AM'],
           ['Uasin Gishu    ', 'Public ', 'SMC    ', 766,
            '12/31/2014 12:00:00 AM'],
           ['Vihiga         ', 'Public ', 'SMC    ', 863,
            '12/31/2014 12:00:00 AM'],
           ['Wajir          ', 'Public ', 'SMC    ', 68,
            '12/31/2014 12:00:00 AM'],
           ['West Pokot     ', 'Public ', 'SMC    ', 368,
            '12/31/2014 12:00:00 AM'],
           ['Kenya          ', 'Public ', 'SMC    ', 35524,
            '12/31/2014 12:00:00 AM'],
           ['Baringo        ', 'Private', 'Private', 135,
            '12/31/2014 12:00:00 AM'],
           ['Bomet          ', 'Private', 'Private', 69,
            '12/31/2014 12:00:00 AM'],
           ['Bungoma        ', 'Private', 'Private', 122,
            '12/31/2014 12:00:00 AM'],
           ['Busia          ', 'Private', 'Private', 62,
            '12/31/2014 12:00:00 AM'],
           ['Elgeyo Marakwet', 'Private', 'Private', 16,
            '12/31/2014 12:00:00 AM'],
           ['Embu           ', 'Private', 'Private', 124,
            '12/31/2014 12:00:00 AM'],
           ['Garissa        ', 'Private', 'Private', 346,
            '12/31/2014 12:00:00 AM'],
           ['Homa Bay       ', 'Private', 'Private', 171,
            '12/31/2014 12:00:00 AM'],
           ['Isiolo         ', 'Private', 'Private', 68,
            '12/31/2014 12:00:00 AM'],
           ['Kajiado        ', 'Private', 'Private', 558,
            '12/31/2014 12:00:00 AM'],
           ['Kakamega       ', 'Private', 'Private', 286,
            '12/31/2014 12:00:00 AM'],
           ['Kericho        ', 'Private', 'Private', 110,
            '12/31/2014 12:00:00 AM'],
           ['Kiambu         ', 'Private', 'Private', 870,
            '12/31/2014 12:00:00 AM'],
           ['Kilifi         ', 'Private', 'Private', 439,
            '12/31/2014 12:00:00 AM'],
           ['Kirinyaga      ', 'Private', 'Private', 76,
            '12/31/2014 12:00:00 AM'],
           ['Kisii          ', 'Private', 'Private', 259,
            '12/31/2014 12:00:00 AM'],
           ['Kisumu         ', 'Private', 'Private', 220,
            '12/31/2014 12:00:00 AM'],
           ['Kitui          ', 'Private', 'Private', 81,
            '12/31/2014 12:00:00 AM'],
           ['Kwale          ', 'Private', 'Private', 49,
            '12/31/2014 12:00:00 AM'],
           ['Laikipia       ', 'Private', 'Private', 176,
            '12/31/2014 12:00:00 AM'],
           ['Lamu           ', 'Private', 'Private', 29,
            '12/31/2014 12:00:00 AM'],
           ['Machakos       ', 'Private', 'Private', 582,
            '12/31/2014 12:00:00 AM'],
           ['Makueni        ', 'Private', 'Private', 193,
            '12/31/2014 12:00:00 AM'],
           ['Mandera        ', 'Private', 'Private', 50,
            '12/31/2014 12:00:00 AM'],
           ['Marsabit       ', 'Private', 'Private', 36,
            '12/31/2014 12:00:00 AM'],
           ['Meru           ', 'Private', 'Private', 229,
            '12/31/2014 12:00:00 AM'],
           ['Migori         ', 'Private', 'Private', 196,
            '12/31/2014 12:00:00 AM'],
           ['Mombasa        ', 'Private', 'Private', 770,
            '12/31/2014 12:00:00 AM'],
           ['Muranga        ', 'Private', 'Private', 261,
            '12/31/2014 12:00:00 AM'],
           ['Nairobi        ', 'Private', 'Private', 1641,
            '12/31/2014 12:00:00 AM'],
           ['Nakuru         ', 'Private', 'Private', 1110,
            '12/31/2014 12:00:00 AM'],
           ['Nandi          ', 'Private', 'Private', 87,
            '12/31/2014 12:00:00 AM'],
           ['Narok          ', 'Private', 'Private', 65,
            '12/31/2014 12:00:00 AM'],
           ['Nyamira        ', 'Private', 'Private', 52,
            '12/31/2014 12:00:00 AM'],
           ['Nyandarua      ', 'Private', 'Private', 412,
            '12/31/2014 12:00:00 AM'],
           ['Nyeri          ', 'Private', 'Private', 233,
            '12/31/2014 12:00:00 AM'],
           ['Samburu        ', 'Private', 'Private', 38,
            '12/31/2014 12:00:00 AM'],
           ['Siaya          ', 'Private', 'Private', 39,
            '12/31/2014 12:00:00 AM'],
           ['Taita Taveta   ', 'Private', 'Private', 48,
            '12/31/2014 12:00:00 AM'],
           ['Tana River     ', 'Private', 'Private', 14,
            '12/31/2014 12:00:00 AM'],
           ['Tharaka-Nithi  ', 'Private', 'Private', 86,
            '12/31/2014 12:00:00 AM'],
           ['Trans Nzoia    ', 'Private', 'Private', 89,
            '12/31/2014 12:00:00 AM'],
           ['Turkana        ', 'Private', 'Private', 96,
            '12/31/2014 12:00:00 AM'],
           ['Uasin Gishu    ', 'Private', 'Private', 225,
            '12/31/2014 12:00:00 AM'],
           ['Vihiga         ', 'Private', 'Private', 23,
            '12/31/2014 12:00:00 AM'],
           ['Wajir          ', 'Private', 'Private', 45,
            '12/31/2014 12:00:00 AM'],
           ['West Pokot     ', 'Private', 'Private', 4,
            '12/31/2014 12:00:00 AM'],
           ['Kenya          ', 'Private', 'Private', 10890,
            '12/31/2014 12:00:00 AM'],
           ['Baringo        ', 'Private', 'TSC    ', 0,
            '12/31/2014 12:00:00 AM'],
           ['Bomet          ', 'Private', 'TSC    ', 0,
            '12/31/2014 12:00:00 AM'],
           ['Bungoma        ', 'Private', 'TSC    ', 0,
            '12/31/2014 12:00:00 AM'],
           ['Busia          ', 'Private', 'TSC    ', 0,
            '12/31/2014 12:00:00 AM'],
           ['Elgeyo Marakwet', 'Private', 'TSC    ', 0,
            '12/31/2014 12:00:00 AM'],
           ['Embu           ', 'Private', 'TSC    ', 0,
            '12/31/2014 12:00:00 AM'],
           ['Garissa        ', 'Private', 'TSC    ', 0,
            '12/31/2014 12:00:00 AM'],
           ['Homa Bay       ', 'Private', 'TSC    ', 0,
            '12/31/2014 12:00:00 AM'],
           ['Isiolo         ', 'Private', 'TSC    ', 0,
            '12/31/2014 12:00:00 AM'],
           ['Kajiado        ', 'Private', 'TSC    ', 0,
            '12/31/2014 12:00:00 AM'],
           ['Kakamega       ', 'Private', 'TSC    ', 0,
            '12/31/2014 12:00:00 AM'],
           ['Kericho        ', 'Private', 'TSC    ', 0,
            '12/31/2014 12:00:00 AM'],
           ['Kiambu         ', 'Private', 'TSC    ', 0,
            '12/31/2014 12:00:00 AM'],
           ['Kilifi         ', 'Private', 'TSC    ', 0,
            '12/31/2014 12:00:00 AM'],
           ['Kirinyaga      ', 'Private', 'TSC    ', 0,
            '12/31/2014 12:00:00 AM'],
           ['Kisii          ', 'Private', 'TSC    ', 0,
            '12/31/2014 12:00:00 AM'],
           ['Kisumu         ', 'Private', 'TSC    ', 0,
            '12/31/2014 12:00:00 AM'],
           ['Kitui          ', 'Private', 'TSC    ', 0,
            '12/31/2014 12:00:00 AM'],
           ['Kwale          ', 'Private', 'TSC    ', 0,
            '12/31/2014 12:00:00 AM'],
           ['Laikipia       ', 'Private', 'TSC    ', 0,
            '12/31/2014 12:00:00 AM'],
           ['Lamu           ', 'Private', 'TSC    ', 0,
            '12/31/2014 12:00:00 AM'],
           ['Machakos       ', 'Private', 'TSC    ', 0,
            '12/31/2014 12:00:00 AM'],
           ['Makueni        ', 'Private', 'TSC    ', 0,
            '12/31/2014 12:00:00 AM'],
           ['Mandera        ', 'Private', 'TSC    ', 0,
            '12/31/2014 12:00:00 AM'],
           ['Marsabit       ', 'Private', 'TSC    ', 0,
            '12/31/2014 12:00:00 AM'],
           ['Meru           ', 'Private', 'TSC    ', 0,
            '12/31/2014 12:00:00 AM'],
           ['Migori         ', 'Private', 'TSC    ', 0,
            '12/31/2014 12:00:00 AM'],
           ['Mombasa        ', 'Private', 'TSC    ', 0,
            '12/31/2014 12:00:00 AM'],
           ['Muranga        ', 'Private', 'TSC    ', 0,
            '12/31/2014 12:00:00 AM'],
           ['Nairobi        ', 'Private', 'TSC    ', 0,
            '12/31/2014 12:00:00 AM'],
           ['Nakuru         ', 'Private', 'TSC    ', 0,
            '12/31/2014 12:00:00 AM'],
           ['Nandi          ', 'Private', 'TSC    ', 0,
            '12/31/2014 12:00:00 AM'],
           ['Narok          ', 'Private', 'TSC    ', 0,
            '12/31/2014 12:00:00 AM'],
           ['Nyamira        ', 'Private', 'TSC    ', 0,
            '12/31/2014 12:00:00 AM'],
           ['Nyandarua      ', 'Private', 'TSC    ', 0,
            '12/31/2014 12:00:00 AM'],
           ['Nyeri          ', 'Private', 'TSC    ', 0,
            '12/31/2014 12:00:00 AM'],
           ['Samburu        ', 'Private', 'TSC    ', 0,
            '12/31/2014 12:00:00 AM'],
           ['Siaya          ', 'Private', 'TSC    ', 0,
            '12/31/2014 12:00:00 AM'],
           ['Taita Taveta   ', 'Private', 'TSC    ', 0,
            '12/31/2014 12:00:00 AM'],
           ['Tana River     ', 'Private', 'TSC    ', 0,
            '12/31/2014 12:00:00 AM'],
           ['Tharaka-Nithi  ', 'Private', 'TSC    ', 0,
            '12/31/2014 12:00:00 AM'],
           ['Trans Nzoia    ', 'Private', 'TSC    ', 0,
            '12/31/2014 12:00:00 AM'],
           ['Turkana        ', 'Private', 'TSC    ', 0,
            '12/31/2014 12:00:00 AM'],
           ['Uasin Gishu    ', 'Private', 'TSC    ', 0,
            '12/31/2014 12:00:00 AM'],
           ['Vihiga         ', 'Private', 'TSC    ', 0,
            '12/31/2014 12:00:00 AM'],
           ['Wajir          ', 'Private', 'TSC    ', 0,
            '12/31/2014 12:00:00 AM'],
           ['West Pokot     ', 'Private', 'TSC    ', 0,
            '12/31/2014 12:00:00 AM'],
           ['Kenya          ', 'Private', 'TSC    ', 0,
            '12/31/2014 12:00:00 AM']], dtype=object)



## Drop a column using pandas - County (centroid)



```python
tsc_data.drop('County (centroid)',axis=1,inplace=True)
tsc_data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>COUNTY</th>
      <th>School Type</th>
      <th>Employment Body</th>
      <th>No. of Teachers</th>
      <th>Year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Baringo</td>
      <td>Public</td>
      <td>TSC</td>
      <td>1172</td>
      <td>12/31/2014 12:00:00 AM</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Bomet</td>
      <td>Public</td>
      <td>TSC</td>
      <td>1379</td>
      <td>12/31/2014 12:00:00 AM</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Bungoma</td>
      <td>Public</td>
      <td>TSC</td>
      <td>2946</td>
      <td>12/31/2014 12:00:00 AM</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Busia</td>
      <td>Public</td>
      <td>TSC</td>
      <td>1182</td>
      <td>12/31/2014 12:00:00 AM</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Elgeyo Marakwet</td>
      <td>Public</td>
      <td>TSC</td>
      <td>1087</td>
      <td>12/31/2014 12:00:00 AM</td>
    </tr>
  </tbody>
</table>
</div>



# Step 3 Create a database in SQlite3


```python
# Connect to SQLite database
conn=sqlite3.connect('tsc_info.db')
cur = conn.cursor()
print('tsc_info.db create successfully')
```

    tsc_info.db create successfully
    

# Step 4 create a table


```python
cur.execute('CREATE TABLE TEACHERS (County text, School_type text,Employment_Body text,Num_Of_teachers int,Year date)')
conn.commit()
print('teachers table created successfully')
```

    teachers table created successfully
    

### The teachers table will be used to store the teachers information from the DataFrame.



## Step 3: Get from Pandas DataFrame to SQL



```python
tsc_data.to_sql('TEACHERS', conn, if_exists='replace', index = False)
 
cur.execute('''SELECT * FROM TEACHERS''')

for row in cur.fetchall():
    print (row)

```

    C:\ProgramData\Anaconda3\lib\site-packages\pandas\core\generic.py:2605: UserWarning: The spaces in these column names will not be changed. In pandas versions < 0.14, spaces were converted to underscores.
      sql.to_sql(
    

    ('Baringo        ', 'Public ', 'TSC    ', 1172, '12/31/2014 12:00:00 AM')
    ('Bomet          ', 'Public ', 'TSC    ', 1379, '12/31/2014 12:00:00 AM')
    ('Bungoma        ', 'Public ', 'TSC    ', 2946, '12/31/2014 12:00:00 AM')
    ('Busia          ', 'Public ', 'TSC    ', 1182, '12/31/2014 12:00:00 AM')
    ('Elgeyo Marakwet', 'Public ', 'TSC    ', 1087, '12/31/2014 12:00:00 AM')
    ('Embu           ', 'Public ', 'TSC    ', 1491, '12/31/2014 12:00:00 AM')
    ('Garissa        ', 'Public ', 'TSC    ', 347, '12/31/2014 12:00:00 AM')
    ('Homa Bay       ', 'Public ', 'TSC    ', 2069, '12/31/2014 12:00:00 AM')
    ('Isiolo         ', 'Public ', 'TSC    ', 180, '12/31/2014 12:00:00 AM')
    ('Kajiado        ', 'Public ', 'TSC    ', 753, '12/31/2014 12:00:00 AM')
    ('Kakamega       ', 'Public ', 'TSC    ', 3558, '12/31/2014 12:00:00 AM')
    ('Kericho        ', 'Public ', 'TSC    ', 1551, '12/31/2014 12:00:00 AM')
    ('Kiambu         ', 'Public ', 'TSC    ', 4288, '12/31/2014 12:00:00 AM')
    ('Kilifi         ', 'Public ', 'TSC    ', 1081, '12/31/2014 12:00:00 AM')
    ('Kirinyaga      ', 'Public ', 'TSC    ', 1478, '12/31/2014 12:00:00 AM')
    ('Kisii          ', 'Public ', 'TSC    ', 3863, '12/31/2014 12:00:00 AM')
    ('Kisumu         ', 'Public ', 'TSC    ', 2213, '12/31/2014 12:00:00 AM')
    ('Kitui          ', 'Public ', 'TSC    ', 2292, '12/31/2014 12:00:00 AM')
    ('Kwale          ', 'Public ', 'TSC    ', 710, '12/31/2014 12:00:00 AM')
    ('Laikipia       ', 'Public ', 'TSC    ', 1029, '12/31/2014 12:00:00 AM')
    ('Lamu           ', 'Public ', 'TSC    ', 210, '12/31/2014 12:00:00 AM')
    ('Machakos       ', 'Public ', 'TSC    ', 2849, '12/31/2014 12:00:00 AM')
    ('Makueni        ', 'Public ', 'TSC    ', 2765, '12/31/2014 12:00:00 AM')
    ('Mandera        ', 'Public ', 'TSC    ', 432, '12/31/2014 12:00:00 AM')
    ('Marsabit       ', 'Public ', 'TSC    ', 233, '12/31/2014 12:00:00 AM')
    ('Meru           ', 'Public ', 'TSC    ', 2819, '12/31/2014 12:00:00 AM')
    ('Migori         ', 'Public ', 'TSC    ', 1429, '12/31/2014 12:00:00 AM')
    ('Mombasa        ', 'Public ', 'TSC    ', 648, '12/31/2014 12:00:00 AM')
    ('Muranga        ', 'Public ', 'TSC    ', 3455, '12/31/2014 12:00:00 AM')
    ('Nairobi        ', 'Public ', 'TSC    ', 2035, '12/31/2014 12:00:00 AM')
    ('Nakuru         ', 'Public ', 'TSC    ', 3015, '12/31/2014 12:00:00 AM')
    ('Nandi          ', 'Public ', 'TSC    ', 1473, '12/31/2014 12:00:00 AM')
    ('Narok          ', 'Public ', 'TSC    ', 723, '12/31/2014 12:00:00 AM')
    ('Nyamira        ', 'Public ', 'TSC    ', 1786, '12/31/2014 12:00:00 AM')
    ('Nyandarua      ', 'Public ', 'TSC    ', 1355, '12/31/2014 12:00:00 AM')
    ('Nyeri          ', 'Public ', 'TSC    ', 2501, '12/31/2014 12:00:00 AM')
    ('Samburu        ', 'Public ', 'TSC    ', 288, '12/31/2014 12:00:00 AM')
    ('Siaya          ', 'Public ', 'TSC    ', 1861, '12/31/2014 12:00:00 AM')
    ('Taita Taveta   ', 'Public ', 'TSC    ', 707, '12/31/2014 12:00:00 AM')
    ('Tana River     ', 'Public ', 'TSC    ', 183, '12/31/2014 12:00:00 AM')
    ('Tharaka-Nithi  ', 'Public ', 'TSC    ', 1295, '12/31/2014 12:00:00 AM')
    ('Trans Nzoia    ', 'Public ', 'TSC    ', 1340, '12/31/2014 12:00:00 AM')
    ('Turkana        ', 'Public ', 'TSC    ', 255, '12/31/2014 12:00:00 AM')
    ('Uasin Gishu    ', 'Public ', 'TSC    ', 1361, '12/31/2014 12:00:00 AM')
    ('Vihiga         ', 'Public ', 'TSC    ', 1668, '12/31/2014 12:00:00 AM')
    ('Wajir          ', 'Public ', 'TSC    ', 408, '12/31/2014 12:00:00 AM')
    ('West Pokot     ', 'Public ', 'TSC    ', 431, '12/31/2014 12:00:00 AM')
    ('Kenya          ', 'Public ', 'TSC    ', 72194, '12/31/2014 12:00:00 AM')
    ('Baringo        ', 'Public ', 'SMC    ', 608, '12/31/2014 12:00:00 AM')
    ('Bomet          ', 'Public ', 'SMC    ', 1261, '12/31/2014 12:00:00 AM')
    ('Bungoma        ', 'Public ', 'SMC    ', 1745, '12/31/2014 12:00:00 AM')
    ('Busia          ', 'Public ', 'SMC    ', 903, '12/31/2014 12:00:00 AM')
    ('Elgeyo Marakwet', 'Public ', 'SMC    ', 454, '12/31/2014 12:00:00 AM')
    ('Embu           ', 'Public ', 'SMC    ', 678, '12/31/2014 12:00:00 AM')
    ('Garissa        ', 'Public ', 'SMC    ', 80, '12/31/2014 12:00:00 AM')
    ('Homa Bay       ', 'Public ', 'SMC    ', 1566, '12/31/2014 12:00:00 AM')
    ('Isiolo         ', 'Public ', 'SMC    ', 31, '12/31/2014 12:00:00 AM')
    ('Kajiado        ', 'Public ', 'SMC    ', 210, '12/31/2014 12:00:00 AM')
    ('Kakamega       ', 'Public ', 'SMC    ', 2139, '12/31/2014 12:00:00 AM')
    ('Kericho        ', 'Public ', 'SMC    ', 1119, '12/31/2014 12:00:00 AM')
    ('Kiambu         ', 'Public ', 'SMC    ', 882, '12/31/2014 12:00:00 AM')
    ('Kilifi         ', 'Public ', 'SMC    ', 893, '12/31/2014 12:00:00 AM')
    ('Kirinyaga      ', 'Public ', 'SMC    ', 508, '12/31/2014 12:00:00 AM')
    ('Kisii          ', 'Public ', 'SMC    ', 1283, '12/31/2014 12:00:00 AM')
    ('Kisumu         ', 'Public ', 'SMC    ', 1062, '12/31/2014 12:00:00 AM')
    ('Kitui          ', 'Public ', 'SMC    ', 1544, '12/31/2014 12:00:00 AM')
    ('Kwale          ', 'Public ', 'SMC    ', 414, '12/31/2014 12:00:00 AM')
    ('Laikipia       ', 'Public ', 'SMC    ', 289, '12/31/2014 12:00:00 AM')
    ('Lamu           ', 'Public ', 'SMC    ', 85, '12/31/2014 12:00:00 AM')
    ('Machakos       ', 'Public ', 'SMC    ', 1405, '12/31/2014 12:00:00 AM')
    ('Makueni        ', 'Public ', 'SMC    ', 1449, '12/31/2014 12:00:00 AM')
    ('Mandera        ', 'Public ', 'SMC    ', 104, '12/31/2014 12:00:00 AM')
    ('Marsabit       ', 'Public ', 'SMC    ', 50, '12/31/2014 12:00:00 AM')
    ('Meru           ', 'Public ', 'SMC    ', 1470, '12/31/2014 12:00:00 AM')
    ('Migori         ', 'Public ', 'SMC    ', 1375, '12/31/2014 12:00:00 AM')
    ('Mombasa        ', 'Public ', 'SMC    ', 175, '12/31/2014 12:00:00 AM')
    ('Muranga        ', 'Public ', 'SMC    ', 951, '12/31/2014 12:00:00 AM')
    ('Nairobi        ', 'Public ', 'SMC    ', 416, '12/31/2014 12:00:00 AM')
    ('Nakuru         ', 'Public ', 'SMC    ', 1387, '12/31/2014 12:00:00 AM')
    ('Nandi          ', 'Public ', 'SMC    ', 1170, '12/31/2014 12:00:00 AM')
    ('Narok          ', 'Public ', 'SMC    ', 472, '12/31/2014 12:00:00 AM')
    ('Nyamira        ', 'Public ', 'SMC    ', 668, '12/31/2014 12:00:00 AM')
    ('Nyandarua      ', 'Public ', 'SMC    ', 644, '12/31/2014 12:00:00 AM')
    ('Nyeri          ', 'Public ', 'SMC    ', 640, '12/31/2014 12:00:00 AM')
    ('Samburu        ', 'Public ', 'SMC    ', 42, '12/31/2014 12:00:00 AM')
    ('Siaya          ', 'Public ', 'SMC    ', 1196, '12/31/2014 12:00:00 AM')
    ('Taita Taveta   ', 'Public ', 'SMC    ', 300, '12/31/2014 12:00:00 AM')
    ('Tana River     ', 'Public ', 'SMC    ', 75, '12/31/2014 12:00:00 AM')
    ('Tharaka-Nithi  ', 'Public ', 'SMC    ', 601, '12/31/2014 12:00:00 AM')
    ('Trans Nzoia    ', 'Public ', 'SMC    ', 971, '12/31/2014 12:00:00 AM')
    ('Turkana        ', 'Public ', 'SMC    ', 144, '12/31/2014 12:00:00 AM')
    ('Uasin Gishu    ', 'Public ', 'SMC    ', 766, '12/31/2014 12:00:00 AM')
    ('Vihiga         ', 'Public ', 'SMC    ', 863, '12/31/2014 12:00:00 AM')
    ('Wajir          ', 'Public ', 'SMC    ', 68, '12/31/2014 12:00:00 AM')
    ('West Pokot     ', 'Public ', 'SMC    ', 368, '12/31/2014 12:00:00 AM')
    ('Kenya          ', 'Public ', 'SMC    ', 35524, '12/31/2014 12:00:00 AM')
    ('Baringo        ', 'Private', 'Private', 135, '12/31/2014 12:00:00 AM')
    ('Bomet          ', 'Private', 'Private', 69, '12/31/2014 12:00:00 AM')
    ('Bungoma        ', 'Private', 'Private', 122, '12/31/2014 12:00:00 AM')
    ('Busia          ', 'Private', 'Private', 62, '12/31/2014 12:00:00 AM')
    ('Elgeyo Marakwet', 'Private', 'Private', 16, '12/31/2014 12:00:00 AM')
    ('Embu           ', 'Private', 'Private', 124, '12/31/2014 12:00:00 AM')
    ('Garissa        ', 'Private', 'Private', 346, '12/31/2014 12:00:00 AM')
    ('Homa Bay       ', 'Private', 'Private', 171, '12/31/2014 12:00:00 AM')
    ('Isiolo         ', 'Private', 'Private', 68, '12/31/2014 12:00:00 AM')
    ('Kajiado        ', 'Private', 'Private', 558, '12/31/2014 12:00:00 AM')
    ('Kakamega       ', 'Private', 'Private', 286, '12/31/2014 12:00:00 AM')
    ('Kericho        ', 'Private', 'Private', 110, '12/31/2014 12:00:00 AM')
    ('Kiambu         ', 'Private', 'Private', 870, '12/31/2014 12:00:00 AM')
    ('Kilifi         ', 'Private', 'Private', 439, '12/31/2014 12:00:00 AM')
    ('Kirinyaga      ', 'Private', 'Private', 76, '12/31/2014 12:00:00 AM')
    ('Kisii          ', 'Private', 'Private', 259, '12/31/2014 12:00:00 AM')
    ('Kisumu         ', 'Private', 'Private', 220, '12/31/2014 12:00:00 AM')
    ('Kitui          ', 'Private', 'Private', 81, '12/31/2014 12:00:00 AM')
    ('Kwale          ', 'Private', 'Private', 49, '12/31/2014 12:00:00 AM')
    ('Laikipia       ', 'Private', 'Private', 176, '12/31/2014 12:00:00 AM')
    ('Lamu           ', 'Private', 'Private', 29, '12/31/2014 12:00:00 AM')
    ('Machakos       ', 'Private', 'Private', 582, '12/31/2014 12:00:00 AM')
    ('Makueni        ', 'Private', 'Private', 193, '12/31/2014 12:00:00 AM')
    ('Mandera        ', 'Private', 'Private', 50, '12/31/2014 12:00:00 AM')
    ('Marsabit       ', 'Private', 'Private', 36, '12/31/2014 12:00:00 AM')
    ('Meru           ', 'Private', 'Private', 229, '12/31/2014 12:00:00 AM')
    ('Migori         ', 'Private', 'Private', 196, '12/31/2014 12:00:00 AM')
    ('Mombasa        ', 'Private', 'Private', 770, '12/31/2014 12:00:00 AM')
    ('Muranga        ', 'Private', 'Private', 261, '12/31/2014 12:00:00 AM')
    ('Nairobi        ', 'Private', 'Private', 1641, '12/31/2014 12:00:00 AM')
    ('Nakuru         ', 'Private', 'Private', 1110, '12/31/2014 12:00:00 AM')
    ('Nandi          ', 'Private', 'Private', 87, '12/31/2014 12:00:00 AM')
    ('Narok          ', 'Private', 'Private', 65, '12/31/2014 12:00:00 AM')
    ('Nyamira        ', 'Private', 'Private', 52, '12/31/2014 12:00:00 AM')
    ('Nyandarua      ', 'Private', 'Private', 412, '12/31/2014 12:00:00 AM')
    ('Nyeri          ', 'Private', 'Private', 233, '12/31/2014 12:00:00 AM')
    ('Samburu        ', 'Private', 'Private', 38, '12/31/2014 12:00:00 AM')
    ('Siaya          ', 'Private', 'Private', 39, '12/31/2014 12:00:00 AM')
    ('Taita Taveta   ', 'Private', 'Private', 48, '12/31/2014 12:00:00 AM')
    ('Tana River     ', 'Private', 'Private', 14, '12/31/2014 12:00:00 AM')
    ('Tharaka-Nithi  ', 'Private', 'Private', 86, '12/31/2014 12:00:00 AM')
    ('Trans Nzoia    ', 'Private', 'Private', 89, '12/31/2014 12:00:00 AM')
    ('Turkana        ', 'Private', 'Private', 96, '12/31/2014 12:00:00 AM')
    ('Uasin Gishu    ', 'Private', 'Private', 225, '12/31/2014 12:00:00 AM')
    ('Vihiga         ', 'Private', 'Private', 23, '12/31/2014 12:00:00 AM')
    ('Wajir          ', 'Private', 'Private', 45, '12/31/2014 12:00:00 AM')
    ('West Pokot     ', 'Private', 'Private', 4, '12/31/2014 12:00:00 AM')
    ('Kenya          ', 'Private', 'Private', 10890, '12/31/2014 12:00:00 AM')
    ('Baringo        ', 'Private', 'TSC    ', 0, '12/31/2014 12:00:00 AM')
    ('Bomet          ', 'Private', 'TSC    ', 0, '12/31/2014 12:00:00 AM')
    ('Bungoma        ', 'Private', 'TSC    ', 0, '12/31/2014 12:00:00 AM')
    ('Busia          ', 'Private', 'TSC    ', 0, '12/31/2014 12:00:00 AM')
    ('Elgeyo Marakwet', 'Private', 'TSC    ', 0, '12/31/2014 12:00:00 AM')
    ('Embu           ', 'Private', 'TSC    ', 0, '12/31/2014 12:00:00 AM')
    ('Garissa        ', 'Private', 'TSC    ', 0, '12/31/2014 12:00:00 AM')
    ('Homa Bay       ', 'Private', 'TSC    ', 0, '12/31/2014 12:00:00 AM')
    ('Isiolo         ', 'Private', 'TSC    ', 0, '12/31/2014 12:00:00 AM')
    ('Kajiado        ', 'Private', 'TSC    ', 0, '12/31/2014 12:00:00 AM')
    ('Kakamega       ', 'Private', 'TSC    ', 0, '12/31/2014 12:00:00 AM')
    ('Kericho        ', 'Private', 'TSC    ', 0, '12/31/2014 12:00:00 AM')
    ('Kiambu         ', 'Private', 'TSC    ', 0, '12/31/2014 12:00:00 AM')
    ('Kilifi         ', 'Private', 'TSC    ', 0, '12/31/2014 12:00:00 AM')
    ('Kirinyaga      ', 'Private', 'TSC    ', 0, '12/31/2014 12:00:00 AM')
    ('Kisii          ', 'Private', 'TSC    ', 0, '12/31/2014 12:00:00 AM')
    ('Kisumu         ', 'Private', 'TSC    ', 0, '12/31/2014 12:00:00 AM')
    ('Kitui          ', 'Private', 'TSC    ', 0, '12/31/2014 12:00:00 AM')
    ('Kwale          ', 'Private', 'TSC    ', 0, '12/31/2014 12:00:00 AM')
    ('Laikipia       ', 'Private', 'TSC    ', 0, '12/31/2014 12:00:00 AM')
    ('Lamu           ', 'Private', 'TSC    ', 0, '12/31/2014 12:00:00 AM')
    ('Machakos       ', 'Private', 'TSC    ', 0, '12/31/2014 12:00:00 AM')
    ('Makueni        ', 'Private', 'TSC    ', 0, '12/31/2014 12:00:00 AM')
    ('Mandera        ', 'Private', 'TSC    ', 0, '12/31/2014 12:00:00 AM')
    ('Marsabit       ', 'Private', 'TSC    ', 0, '12/31/2014 12:00:00 AM')
    ('Meru           ', 'Private', 'TSC    ', 0, '12/31/2014 12:00:00 AM')
    ('Migori         ', 'Private', 'TSC    ', 0, '12/31/2014 12:00:00 AM')
    ('Mombasa        ', 'Private', 'TSC    ', 0, '12/31/2014 12:00:00 AM')
    ('Muranga        ', 'Private', 'TSC    ', 0, '12/31/2014 12:00:00 AM')
    ('Nairobi        ', 'Private', 'TSC    ', 0, '12/31/2014 12:00:00 AM')
    ('Nakuru         ', 'Private', 'TSC    ', 0, '12/31/2014 12:00:00 AM')
    ('Nandi          ', 'Private', 'TSC    ', 0, '12/31/2014 12:00:00 AM')
    ('Narok          ', 'Private', 'TSC    ', 0, '12/31/2014 12:00:00 AM')
    ('Nyamira        ', 'Private', 'TSC    ', 0, '12/31/2014 12:00:00 AM')
    ('Nyandarua      ', 'Private', 'TSC    ', 0, '12/31/2014 12:00:00 AM')
    ('Nyeri          ', 'Private', 'TSC    ', 0, '12/31/2014 12:00:00 AM')
    ('Samburu        ', 'Private', 'TSC    ', 0, '12/31/2014 12:00:00 AM')
    ('Siaya          ', 'Private', 'TSC    ', 0, '12/31/2014 12:00:00 AM')
    ('Taita Taveta   ', 'Private', 'TSC    ', 0, '12/31/2014 12:00:00 AM')
    ('Tana River     ', 'Private', 'TSC    ', 0, '12/31/2014 12:00:00 AM')
    ('Tharaka-Nithi  ', 'Private', 'TSC    ', 0, '12/31/2014 12:00:00 AM')
    ('Trans Nzoia    ', 'Private', 'TSC    ', 0, '12/31/2014 12:00:00 AM')
    ('Turkana        ', 'Private', 'TSC    ', 0, '12/31/2014 12:00:00 AM')
    ('Uasin Gishu    ', 'Private', 'TSC    ', 0, '12/31/2014 12:00:00 AM')
    ('Vihiga         ', 'Private', 'TSC    ', 0, '12/31/2014 12:00:00 AM')
    ('Wajir          ', 'Private', 'TSC    ', 0, '12/31/2014 12:00:00 AM')
    ('West Pokot     ', 'Private', 'TSC    ', 0, '12/31/2014 12:00:00 AM')
    ('Kenya          ', 'Private', 'TSC    ', 0, '12/31/2014 12:00:00 AM')
    

# Step 5 Output on HTML


```python
p = []
table_data = f"<tr><td>County</td><td>School_Type</td><td>Employment_Body</td>" \
        f"<td>Number_Of_Teachers</td><td>County(Centroid)</td><td>Year</td></tr>"
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

```


```python
html = tsc_data.to_html("index.html") 
# Create index.html to write html on it
tsc_f = open("index.html","r+")
tsc_f.close()

    # Open file in browser
webbrowser.open_new_tab('index.html')

```




    True



### Display the first 5 records


```python
tsc_data.head(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>COUNTY</th>
      <th>School Type</th>
      <th>Employment Body</th>
      <th>No. of Teachers</th>
      <th>Year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Baringo</td>
      <td>Public</td>
      <td>TSC</td>
      <td>1172</td>
      <td>12/31/2014 12:00:00 AM</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Bomet</td>
      <td>Public</td>
      <td>TSC</td>
      <td>1379</td>
      <td>12/31/2014 12:00:00 AM</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Bungoma</td>
      <td>Public</td>
      <td>TSC</td>
      <td>2946</td>
      <td>12/31/2014 12:00:00 AM</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Busia</td>
      <td>Public</td>
      <td>TSC</td>
      <td>1182</td>
      <td>12/31/2014 12:00:00 AM</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Elgeyo Marakwet</td>
      <td>Public</td>
      <td>TSC</td>
      <td>1087</td>
      <td>12/31/2014 12:00:00 AM</td>
    </tr>
  </tbody>
</table>
</div>




```python
#display a single column
tsc_data['COUNTY']
```




    0      Baringo        
    1      Bomet          
    2      Bungoma        
    3      Busia          
    4      Elgeyo Marakwet
                ...       
    187    Uasin Gishu    
    188    Vihiga         
    189    Wajir          
    190    West Pokot     
    191    Kenya          
    Name: COUNTY, Length: 192, dtype: object




```python
#place this in a variable 
our_county=tsc_data['COUNTY']
#identify type
type(our_county)
```




    pandas.core.series.Series




```python
#list 5  counties using a variable
our_county.head(5)

```




    0    Baringo        
    1    Bomet          
    2    Bungoma        
    3    Busia          
    4    Elgeyo Marakwet
    Name: COUNTY, dtype: object




```python

```

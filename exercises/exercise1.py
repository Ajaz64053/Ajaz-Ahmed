#installing all the libraries as mentioned in the exercise task 
!pip install attrs==22.2.0
!pip install greenlet==2.0.2
!pip install iniconfig==2.0.0
!pip install numpy==1.24.2
!pip isntall packaging==23.0
!pip install pandas==1.5.3
!pip install pluggy==1.0.0
!pip install python-dateutil==2.8.2
!pip install pytz==2022.7.1
!pip install six==1.16.0
!pip install pandas SQLAlchemy==1.4.46
!pip install typing_extensions==4.5.0


#load the data 
import pandas as pd
from sqlalchemy import create_engine 
df = pd.read_csv('rhein-kreis-neuss-flughafen-weltweit.csv', delimiter=';')
df

#The describe() method returns description of the data in the DataFrame.
df.describe()



#define the database name and table name 
database_name = "airports.sqlite"
table_name = "airports"

#the first five row of the data 
df.head(5)

#data types of all the columns
print(df.dtypes)

#define SQLite data types for each column
column_types = {
    "column_1": "BIGINT",
    "column_2":"TEXT",
    "column_3":"TEXT",
    "column_4":"TEXT",
    "column_5":"VARCHAR",
    "column_6":"TEXT",
    "column_7":"FLOAT",
    "column_8":"FLOAT",
    "column_9":"TEXT",
    "column_10":"FLOAT",
    "column_11":"TEXT",
    "column_12":"TEXT",
    "geo_punkt":"TEXT"
    
}

#create an SQLite engine 
engine= create_engine(f"sqlite:///{database_name}")


#write data to SQLite database 
df.to_sql(table_name, engine, if_exists="replace",index=False)











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

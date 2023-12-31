from sqlalchemy import create_engine
import requests
import pandas as pd
import os
from dotenv import load_dotenv
from pandas import json_normalize

# Obteniendo la variables de entorno
load_dotenv()
db_name = os.getenv("db_name") # data-engineer-database
username = os.getenv("username") # adauto_rodrigo_coderhouse
password = os.getenv("password")
table_name = os.getenv("table_name") # crypto

url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false&locale=en"
databaseURI = "postgresql://" + username + ":" + password+"@data-engineer-cluster.cyhh5bfevlmn.us-east-1.redshift.amazonaws.com:5439/" + db_name

conn = create_engine(databaseURI)
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    df = json_normalize(data)
    df = df.drop_duplicates()
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.dispose()
else:
    print("Error: ", response.status_code)

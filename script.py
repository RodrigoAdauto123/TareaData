from sqlalchemy import create_engine
import requests
import pandas as pd
from pandas import json_normalize


url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false&locale=en"
databaseURI = "postgresql://adauto_rodrigo_coderhouse:l3Fr2953aE@data-engineer-cluster.cyhh5bfevlmn.us-east-1.redshift.amazonaws.com:5439/data-engineer-database"
table_name = "crypto"

conn = create_engine(databaseURI)
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    # df = pd.DataFrame(data)
    df = json_normalize(data)
    df = df.drop_duplicates()
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.dispose()

else:
    print("Error: ", response.status_code)


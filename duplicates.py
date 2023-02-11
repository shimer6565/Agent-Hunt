import psycopg2
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt


hostname = 'localhost'
database = 'agent_hunt'
username = 'postgres'
pwd = '56565'
port_id = 5432


conn = None
cur = None

try:

    conn = psycopg2.connect(
        host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = port_id
    )

    cur = conn.cursor()
    
    
    

except Exception as error:
    print(error)

finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()


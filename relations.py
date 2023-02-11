import psycopg2
import pandas as pd

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
    
    cur.execute('SELECT a.id,b.id from agent_info a INNER JOIN brokerage b on a.brokerage_id = b.id order by b.id asc')
    agents_brokerage = cur.fetchmany(10)

    relations = []
    for i in range(len(agents_brokerage)):
        for j in range(i+1, len(agents_brokerage)):
            if agents_brokerage[i][1] == agents_brokerage[j][1]:
                relations.append([agents_brokerage[i][0], agents_brokerage[j][0]])
            else:
                break


    
    # relations = pd.DataFrame(relations)
    # relations.to_csv('relations.csv')
    

except Exception as error:
    print(error)

finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()


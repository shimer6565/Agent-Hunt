import psycopg2
import scipy
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from urllib.parse import urlparse 



hostname = 'localhost'
database = 'agent_hunt'
username = 'postgres'
pwd = '56565'
port_id = 5432


conn = None
cur = None

try:

    result = urlparse("postgres://zh_agenthunt_user:nPP2m1ElEbJSsZTTsgYdgKI4RaJiOMMA@dpg-cfjvb6ta49903flrl17g-a.singapore-postgres.render.com/zh_agenthunt")
    username = result.username
    password = result.password
    database = result.path[1:]
    hostname = result.hostname
    port = result.port
    conn = psycopg2.connect(
        database = database,
        user = username,
        password = password,
        host = hostname,
        port = port
    )

    cur = conn.cursor()
    
    #   QUERY TO CREATE AGENT_RELATIONS TABLE 
    #   create table agent_relations as (select a.id as agent_list_id, h.id as home_id, b.id as agent_sell_id from agent_listing a inner join home_info h on a.home_id = h.id inner join agent_listing b on b.home_id = h.id where a.deal_side = "LISTING" and b.deal_side = "SELLING")
    cur.execute('SELECT * FROM agent_relations')
    agents_relations = cur.fetchmany(2000)

    
    graph = nx.Graph()
 
    for relation in agents_relations:
        #print(relation[0], relation[2])
        graph.add_edge(relation[0], relation[2])
    
    nx.draw(graph, node_size=10)
    plt.savefig("relations.png")
    

except Exception as error:
    print(error)

finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()


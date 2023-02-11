import psycopg2
import scipy
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
    
    #   QUERY TO CREATE AGENT_RELATIONS TABLE 
    #   create table agent_relations as (select a.id as agent_list_id, h.id as home_id, b.id as agent_sell_id from agent_listing a inner join home_info h on a.home_id = h.id inner join agent_listing b on b.home_id = h.id where a.deal_side = "LISTING" and b.deal_side = "SELLING")
    cur.execute('SELECT * FROM agent_relations')
    agents_relations = cur.fetchmany(1000)

    
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


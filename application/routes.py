import psycopg2
import pandas as pd
from application import app
import networkx as nx
import matplotlib.pyplot as plt
from flask import Flask, render_template, request, redirect, url_for
from urllib.parse import urlparse 


hostname = ' dpg-cfjvb6ta49903flrl17g-a.singapore-postgres.render.com'
database = 'zh_agenthunt'
username = 'zh_agenthunt_user'
pwd = 'nPP2m1ElEbJSsZTTsgYdgKI4RaJiOMMA'
port_id = 5432

@app.route('/',methods=['POST','GET'])

def home():
    return render_template('home.html')

@app.route('/getN',methods=['POST','GET'])

def getValForN():
        return render_template('getN.html')

@app.route('/topn',methods=['POST','GET'])

def displayTopN():
    conn = None
    cur = None

    n = request.form['n']
    city_mid = request.form['city_mid']
    state_mid = request.form['state_mid']
    country_mid = request.form['country_mid']
    zipcode_mid = request.form['zipcode_mid']

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

        print(state_mid, country_mid, city_mid, zipcode_mid)
        cur = conn.cursor()
        cur.execute('SELECT a.id, a.first_name, count(*) FROM agent_listing al INNER JOIN home_info h ON al.home_id = h.id INNER JOIN agent_info a ON al.agent_id = a.id WHERE h.state_market_id = %s and h.county_market_id = %s and h.city_market_id = %s and h.zipcode_market_id = %s GROUP BY a.id ORDER BY COUNT(*) DESC FETCH FIRST %s ROWS ONLY',(state_mid, country_mid, city_mid, zipcode_mid, n,))
        topNagents = cur.fetchall()
        print(topNagents)


        cur.execute('SELECT b.id, b.name, count(*) FROM agent_listing al INNER JOIN home_info h ON al.home_id = h.id INNER JOIN agent_info a ON al.agent_id = a.id INNER JOIN brokerage b ON b.id = a.brokerage_id WHERE h.state_market_id = %s and h.county_market_id = %s and h.city_market_id = %s and h.zipcode_market_id = %s GROUP BY b.id ORDER BY COUNT(*) DESC FETCH FIRST %s ROWS ONLY',(state_mid, country_mid, city_mid, zipcode_mid, n,))
        topNbrokerages = cur.fetchall()



    except Exception as error:
        print(error)

    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()

    return render_template('topAgentsAndBrokerages.html', agents = topNagents, brokerages = topNbrokerages)

@app.route('/insights',methods=['POST','GET'])

def displayInsights():
    return render_template('insights.html')

@app.route('/ERDiagram',methods=['POST','GET'])

def displayERD():
    return render_template('erDiagram.html')

@app.route('/agentsRelation',methods=['POST','GET'])

def displayRelation():
    return render_template('relations.html')

@app.route('/temp',methods=['POST','GET'])

def display():
    return render_template('getMarketId.html')

@app.route('/relationByMarketID',methods=['POST'])

def displayRelationById():
    city_mid = request.form['city_mid']
    state_mid = request.form['state_mid']
    country_mid = request.form['country_mid']
    zipcode_mid = request.form['zipcode_mid']

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

        print(state_mid, country_mid, city_mid, zipcode_mid)
        cur = conn.cursor()
        cur.execute('SELECT * FROM agent_relations ar INNER JOIN home_info h ON ar.home_id = h.id WHERE h.state_market_id = %s and h.county_market_id = %s and h.city_market_id = %s and h.zipcode_market_id = %s',(state_mid, country_mid, city_mid, zipcode_mid,))
        agents_relations = cur.fetchmany(500)
        print("----------",len(agents_relations))

        graph = nx.Graph()
 
        for relation in agents_relations:
            graph.add_edge(relation[0], relation[2])
        
        nx.draw(graph, node_size=10)
        plt.savefig("application/static/relations_based_on_id.png")
        

    except Exception as error:
        print(error)

    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()

    print(city_mid)
    return render_template('relationByMarket.html')
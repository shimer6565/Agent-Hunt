import psycopg2
import pandas as pd
from application import app
from flask import Flask, render_template, request, redirect, url_for

hostname = 'localhost'
database = 'agent_hunt'
username = 'postgres'
pwd = '56565'
port_id = 5432

@app.route('/',methods=['POST','GET'])

def home():
    return render_template('home.html')

@app.route('/topn',methods=['POST','GET'])

def displayTopN(n = 10):
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
        cur.execute('SELECT a.id, a.first_name, count(*) FROM agent_listing al INNER JOIN home_info h ON al.home_id = h.id INNER JOIN agent_info a ON al.agent_id = a.id GROUP BY a.id ORDER BY COUNT(*) DESC FETCH FIRST %s ROWS ONLY',(n,))
        topNagents = cur.fetchall()


        cur.execute('SELECT b.id,b.name, count(*) FROM agent_listing al INNER JOIN home_info h ON al.home_id = h.id INNER JOIN agent_info a ON al.agent_id = a.id INNER JOIN brokerage b ON b.id = a.brokerage_id GROUP BY b.id ORDER BY COUNT(*) DESC FETCH FIRST %s ROWS ONLY',(n,))
        topNbrokerages = cur.fetchall()



    except Exception as error:
        print(error)

    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()

    return render_template('topAgentsAndBrokerages.html', agents = topNagents, brokerages = topNbrokerages)
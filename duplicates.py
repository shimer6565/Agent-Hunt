import psycopg2
from collections import Counter
from math import sqrt


hostname = 'localhost'
database = 'agent_hunt'
username = 'postgres'
pwd = '56565'
port_id = 5432


conn = None
cur = None


def word2vec(word):
    
    cw = Counter(word)
    sw = set(cw)
    lw = sqrt(sum(c*c for c in cw.values()))

    return cw, sw, lw

def cosdis(v1, v2):

    common = v1[1].intersection(v2[1])
    return sum(v1[0][ch]*v2[0][ch] for ch in common)/v1[2]/v2[2]


try:

    conn = psycopg2.connect(
        host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = port_id
    )

    cur = conn.cursor()

    cur.execute('SELECT *, concat(street, city, state, county, zipcode) as address FROM agent_info')
    agents = cur.fetchmany(1000)


    for i in range(len(agents)):
        for j in range(i+1, len(agents)):
            if (((agents[i][2] == agents[j][2]) and agents[i][2] != None) or ((agents[i][3] == agents[j][3]) and agents[i][3] != None) or 
            (((agents[i][10].strip('][').split(', ')).sort() == (agents[j][10].strip('][').split(', ')).sort()) and (agents[i][10].strip('][').split(', ')).sort() != None) or 
            (((agents[i][13] != 0 and agents[i][13] != "") and (agents[j][13] != 0 and agents[j][13] != "")) and cosdis(word2vec(agents[i][13]), word2vec(agents[j][13])) > 0.95)):

            
                cur.execute("DELETE FROM agent_listing WHERE agent_id = %s",(agents[j][0],))
                cur.execute("DELETE FROM agent_info WHERE id = %s",(agents[j][0],))

    conn.commit()

    cur.execute('SELECT *, concat(street, city, state, county, zipcode) as address FROM brokerage')
    brokerages = cur.fetchmany(1000)

    for i in range(len(brokerages)):
        for j in range(i+1, len(brokerages)):
            if ((cosdis(word2vec(brokerages[i][3]), word2vec(brokerages[j][3])) > 9.5)
            or ((brokerages[i][10].strip('][').split(', ').sort() == brokerages[j][10].strip('][').split(', ').sort()) and (brokerages[i][10].strip('][').split(', ').sort() != None))
            or (brokerages[i][13] == brokerages[j][13])):

               cur.execute("DELETE FROM agent_info WHERE brokerage_id = %s",(brokerages[j][0],))
               cur.execute("DELETE FROM brokerage WHERE id = %s",(brokerages[j][0],))

    conn.commit()



except Exception as error:
    print(error)

finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.commit()
        conn.close()


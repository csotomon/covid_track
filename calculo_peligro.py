import sqlite3
import pandas as pd
import networkx as nx
from geopy.distance import lonlat, distance

def procesar():
    conn = None
    conn = sqlite3.connect("visualizacion/db.sqlite3")
    sql = "SELECT id, name, longitude, latitude FROM covid_poi"
    cur = conn.cursor()
    cur.execute(sql)
    pois = cur.fetchall()
    
    cur.execute("SELECT id, longitude, latitude FROM covid_tracking WHERE date BETWEEN '2020-06-17' AND '2020-06-18'")
    trackings = cur.fetchall()
    
    covid_graph = nx.Graph()

    # Construimos el grafo
    for tracking in trackings:
        covid_graph.add_node(tracking, tipo='tracking')
    for poi in pois:
         covid_graph.add_node(poi, tipo='poi')
         poi_pos = (poi[2], poi[3])
         for tracking in trackings:
             distancia = distance(lonlat(*poi_pos), lonlat(tracking[1], tracking[2])).meters
             # Si la distancia es menor a 200 metros, se crea un edge entre el POI y el tranking
             if distancia<200:
                 covid_graph.add_edge(tracking,poi)

    # Calculamos el page rank
    b = nx.pagerank(covid_graph)

    # Recorremos el grafo para actualizar los pesos
    for v in covid_graph.nodes(data=True):
        atributo =  v[1]
        if atributo['tipo'] == 'poi':
            # Actualiza la base de datos con el valor del page rank
            sql = "UPDATE covid_poi SET rank = ? WHERE id=? "
            cur = conn.cursor()
            cur.execute(sql, (b[v[0]], v[0][0]))
    
    conn.commit()
    conn.close()
             
    
    

    

if __name__ == "__main__":
    procesar()
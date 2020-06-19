import sqlite3
import pandas as pd

def procesar():

    pois_df = pd.read_csv("points_from_mde.csv")
    pois_df.info()
    conn = None
    conn = sqlite3.connect("visualizacion/db.sqlite3")
    for index, registro in pois_df.iterrows():
        try:
            poi = (registro['name'], registro['lat'], registro['lon'], 0)
            sql = "INSERT INTO covid_poi (name,latitude,longitude, rank) VALUES(?,?,?, ?) "
            cur = conn.cursor()
            cur.execute(sql, poi)
            print(cur.lastrowid)
        except:
            print('error')
    conn.commit()
    conn.close()


if __name__ == "__main__":
    procesar()
import db_connect
import create_tables

#connect
conn = db_connect.db_connect()
cur = conn.cursor()

#create tables
def create_all_tables():
    #create seasons table
    cur.execute(create_tables.create_seasons_table())
    conn.commit()

    #create players table
    cur.execute(create_tables.create_players_table())
    conn.commit()

    #create forwards table
    cur.execute(create_tables.create_forwards_table())
    conn.commit()

    #create defensemen table
    cur.execute(create_tables.create_defensemen_table())
    conn.commit()

    #create goalies table
    cur.execute(create_tables.create_goalies_table())
    conn.commit()

#Function ran and tables were created on 3/30/22
#create_all_tables()


conn.close()
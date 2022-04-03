import db_connect
import create_tables
import insert_statements
import csv

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

def insert_all_seasons_data():
    path = "C:\\Users\\Work\\OneDrive\\Desktop\\CSE 460 Project\\csv_files\\seasons_csv.csv"
    with open(path) as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        for row in reader:
            mp = b'0'
            if row[7] == 'Yes':
                mp = b'1'

            cur.execute(insert_statements.seasons(row[0], row[1], row[2], row[3], row[4], row[5], row[6], mp))
            conn.commit()
            
#Function ran and seasons data added on 4/1
#insert_all_seasons_data()

def insert_all_forwards_data():
    path = "C:\\Users\\Work\\OneDrive\\Desktop\\CSE 460 Project\\csv_files\\all_sabres_player_data_csv.csv"
    with open(path) as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        for row in reader:
            if row[1] =='F':
                plusminus = row[6]
                if plusminus == '':
                    plusminus = 0
            
                name = repr(row[0])
                cur.execute(insert_statements.forwards(name, row[2], row[3], row[4], row[5], plusminus))
                conn.commit()
                
#Function ran and forwards data added on 4/3
#insert_all_forwards_data()
conn.close()
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

def insert_all_defensemen_data():
    path = "C:\\Users\\Work\\OneDrive\\Desktop\\CSE 460 Project\\csv_files\\all_sabres_player_data_csv.csv"
    with open(path) as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        for row in reader:
            if row[1] =='D':
                plusminus = row[6]
                if plusminus == '':
                    plusminus = 0
            
                name = repr(row[0])
                cur.execute(insert_statements.defensemen(name, row[2], row[3], row[4], row[5], plusminus))
                conn.commit()

#File ran and players data added on 4/13
#insert_all_players_data()
def insert_all_players_data():
    path = "C:\\Users\\Work\\OneDrive\\Desktop\\CSE 460 Project\\csv_files\\all_sabres_player_data_csv.csv"
    with open(path) as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        for row in reader:
            name = repr(row[0])
            years = repr(row[7])
            start = years[1:5]
            end = years[6:10]
            cur.execute(insert_statements.players(int(start), int(end), name))
            conn.commit()

def insert_all_goalies_data():
    '''
    Below is the order of data in the CSV file for clarity on how it is extracted from goalies.csv
    Name is row[1], GP is row[3], Wins is row[6], Losses is row[7], GAA is row[4], save_percentage  is row[5]
    '''
    path = "C:\\Users\\Work\\OneDrive\\Desktop\\CSE 460 Project\\csv_files\\goalies.csv"
    with open(path) as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        for row in reader:
            name = repr(row[1])
            GP = row[3]
            W = row[6]
            L = row[7]
            GAA = row[4]
            if GAA == '':
                GAA = 0
            SV = row[5]
            if SV == '':
                SV = 0
            cur.execute(insert_statements.goalies(name, GP, W, L, GAA, SV))
            conn.commit()

#Function ran and goalie data added on 4/15
#insert_all_goalies_data()

def testing():
    data = []
    testQuery1 = "SELECT * FROM Players WHERE name = 'RICK MARTIN'"
    cur.execute(testQuery1)
    for (starting_season, ending_season, name) in cur:
        data.append([starting_season, ending_season, name])

    if (data[0][2] != "RICK MARTIN"):
        print("testQuery1 failed.")

    data2 = []
    testQuery2 = ("INSERT INTO Players "
                "(starting_season, ending_season, name) "
                "VALUES (%s, %s, %s")
    dataQuery2 = (2010, 2011, "TEST PLAYER")
    cur.execute(testQuery1, dataQuery2)

    testQuery3 = "SELECT * FROM Players WHERE name = 'TEST PLAYER'"
    cur.execute(testQuery3)
    for (starting_season, ending_season, name) in cur: 
        data2.append([starting_season, ending_season, name])

    if (data2[0][2] != "TEST PLAYER"):
        print("testQuery3 failed.")

    data3 = []
    testQuery4 = "UPDATE Players SET starting_season = %s WHERE name = 'TEST PLAYER'"
    dataQuery4 = (2009)
    cur.execute(testQuery4, dataQuery4)

    testQuery5 = "SELECT * FROM Players WHERE name = 'TEST PLAYER'"
    cur.execute(testQuery5)
    for (starting_season, ending_season, name) in cur: 
        data3.append([starting_season, ending_season, name])
    
    if (data3[0][0] != 2009):
        print("testQuery5 failed")

    testQuery6 = "DELETE FROM Players WHERE name = 'TEST PLAYER'"
    cur.execute(testQuery6)

    data4 = []
    testQuery7 = "SELECT * FROM Players WHERE name = 'TEST PLAYER'"
    cur.execute(testQuery7)
    for (starting_season, ending_season, name) in cur:
        data4.append([starting_season, ending_season, name])
    
    if (data4 != []):
        print("testQuery6 failed")
    
    data5 = []
    testQuery8 = "SELECT MAX(goals) FROM Forwards"
    cur.execute(testQuery8)
    for (games_played) in cur: 
        data5.append(games_played)
    
    if (data5[0][0] != 512):
        print("testQuery8 has failed")

    cur.execute("SELECT * FROM Defensemen ORDER BY games_played DESC")
    cur.execute("SELECT * FROM Seasons NATURAL JOIN Players")
    cur.execute("SELECT COUNT(starting_season), starting_season FROM Players GROUP BY starting_season")
    cur.execute("SELECT * FROM Forwards WHERE name in (SELECT * FROM Seasons NATURAL JOIN Players)")
    

conn.close()
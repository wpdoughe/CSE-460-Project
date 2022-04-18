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
    # Test 1: SELECT
    data = []
    testQuery1 = "SELECT * FROM Players WHERE name = 'Rick Martin'"
    cur.execute(testQuery1)
    conn.commit()
    
    for (starting_season, ending_season, name) in cur:
        data.append([starting_season, ending_season, name])
    
    print("********************")
    if (data[0][2] == "Rick Martin"):
        print("Test 1: passed")
        print("This tested the SELECT query by verifying data we already know exists in the database")
    else:
        print("Test 1: failed")
    print("********************")

    # Test 2: INSERT
    data2 = []

    #verify TEST PLAYER is not already in the database
    test_not_already_in_db = "SELECT * FROM Players WHERE name = 'TEST PLAYER'"
    test_not_already_in_db_arr = []
    cur.execute(test_not_already_in_db)
    conn.commit()
    for i in cur:
        test_not_already_in_db_arr.append(i)


    dataQuery2 = (2010, 2011, "TEST PLAYER")
    testQuery2 = (f"INSERT INTO Players VALUES ({dataQuery2[0]}, {dataQuery2[1]}, {repr(dataQuery2[2])})")
    cur.execute(testQuery2)
    conn.commit()

    testQuery3 = "SELECT * FROM Players WHERE name = 'TEST PLAYER'"
    cur.execute(testQuery3)
    conn.commit()

    for (starting_season, ending_season, name) in cur: 
        data2.append([starting_season, ending_season, name])

    print("********************")
    if (data2[0][0] == 2010 and data2[0][1] == 2011 and data2[0][2] == "TEST PLAYER" and len(test_not_already_in_db_arr) == 0):
        print("Test 2: passed")
        print("This tested the INSERT query by verifiying that the starting year, ending year, and name all match what we inserted into the database.")
        print("(also tested that TEST PLAYER did not exist in the database before insertion)")
    else:
        print("Test 2: failed")
    print("********************")

    # Test 3: Update
    data3 = []
    dataQuery4 = [2009]
    testQuery4 = f"UPDATE Players SET starting_season = {dataQuery4[0]} WHERE name = 'TEST PLAYER'"
    cur.execute(testQuery4)
    conn.commit()

    testQuery5 = "SELECT * FROM Players WHERE name = 'TEST PLAYER'"
    cur.execute(testQuery5)
    conn.commit()
    for (starting_season, ending_season, name) in cur: 
        data3.append([starting_season, ending_season, name])
    
    print("********************")
    if (data3[0][0] == 2009 and data3[0][2] == "TEST PLAYER"):
        print("Test 3: passed")
        print("This tested the UPDATE query by verifying that the starting season for TEST PLAYER is now 2009, instead of 2010")
    else:
        print("Test 3: failed")
    print("********************")

    # Test 4: Delete
    testQuery6 = "DELETE FROM Players WHERE name = 'TEST PLAYER'"
    cur.execute(testQuery6)
    conn.commit()

    data4 = []
    testQuery7 = "SELECT * FROM Players WHERE name = 'TEST PLAYER'"
    cur.execute(testQuery7)
    conn.commit()
    for (starting_season, ending_season, name) in cur:
        data4.append([starting_season, ending_season, name])

    print("********************")
    if (len(data4) == 0):
        print("Test 4: passed")
        print("This tested the DELETE query by verifying that the entry for TEST PLAYER no longer exists in the database")
    else:
        print("Test 4: failed")
    print("********************")

    #Test 5: MAX
    data5 = []
    testQuery8 = "SELECT MAX(goals) FROM Forwards"
    cur.execute(testQuery8)
    conn.commit()
    for (games_played) in cur: 
        data5.append(games_played)
    
    print("********************")
    if (data5[0][0] == 512):
        print("Test 5: passed")
        print("This tested the MAX query by grabbing the maximun amount of goals a forward has in our database")
    else:
        print("Test 5: failed")
    print("********************")

    # cur.execute("SELECT * FROM Defensemen ORDER BY games_played DESC")
    # cur.execute("SELECT * FROM Seasons NATURAL JOIN Players")
    # cur.execute("SELECT COUNT(starting_season), starting_season FROM Players GROUP BY starting_season")
    # cur.execute("SELECT * FROM Forwards WHERE name in (SELECT * FROM Seasons NATURAL JOIN Players)")
    
testing()
conn.close()
import psycopg2


def create_seasons_table():
    return "CREATE TABLE Seasons(year INTEGER PRIMARY KEY, games_played INTEGER, wins INTEGER, loses INTEGER, overtime_loses INTEGER, shootout_loses INTEGER, points INTEGER, made_playoffs BIT);"

def create_players_table():
    return "CREATE TABLE Players(starting_season INTEGER NOT NULL, ending_season INTEGER, name VARCHAR NOT NULL);"

def create_forwards_table():
    return "CREATE TABLE Forwards(name VARCHAR NOT NULL, games_played INTEGER, goals INTEGER, assists INTEGER, points INTEGER, plus_minus INTEGER);"

def create_defensemen_table():
    return "CREATE TABLE Defensemen(name VARCHAR NOT NULL, games_played INTEGER, goals INTEGER, assists INTEGER, points INTEGER, plus_minus INTEGER);"

def create_goalies_table():
    return "CREATE TABLE Goalies(name VARCHAR NOT NULL, games_played INTEGER, wins INTEGER, loses INTEGER, goals_against_avg DECIMAL(3,2), save_percentage DECIMAL(4,3));"

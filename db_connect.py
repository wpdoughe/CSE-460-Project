import os
import psycopg2

DB_HOST = "127.0.0.1"
DB_NAME = "project"
DB_USER = "postgres"
DB_PASSWORD = "Watup202!"

def db_connect():
    return psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASSWORD)
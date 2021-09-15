#%%
import os
import sqlite3 as lite
from sqlite3.dbapi2 import Cursor, connect

# %%
# functionality goes here
#OOP
class DatabaseManage(object):
    
    def __init__(self):
        global con
        try:
            con = lite.connect('cources.db')# the database
            with con:
                cur = con.cursor()# table is course
                cur.execute("CREATE TABLE IF NOT EXISTS course(Id INTEGER PRIMARY KEY AUTOINCRIMENT, name TEXT, description TEXT, price TEXT, is_private BOOLEAN NOT NULL DEFAULT 1)")
        except Exception:
            print("unable to create a DB!")
    
    # insert data into DB
    def insert_data(self, data):
        try:
            with con:
                cur = con.cursor()
                cur.execute(
                "INSERT INTO course(name, description, price, is_private) VALUES(?,?,?,?)", data
                )
        except Exception:
            return False

    # Fetch data
    def fetch_data(self):
        try:
            with con:
                cur = con.cursor()
                cur.execute("SELECT * FROM course")
                return cur.fetchall
        except Exception:
            return False

    # Delete data
    def delete_data(self, id):
        try:
            with con:
                cur = con.cursor()
                cur
        except Exception:
            return False

# %%
# TODO: provide interface to user 


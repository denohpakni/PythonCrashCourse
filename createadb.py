
import os
import sqlite3 as lite

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
            print("SHitNuts! Unable to create a DB!")
    
    # insert data into DB
    def insert_data(self, data):
        try:
            with con:
                cur = con.cursor()
                cur.execute(
                "INSERT INTO course(name, description, price, is_private) VALUES(?,?,?,?)", data)
                return True
        except Exception:
            return False

    # Fetch data
    def fetch_data(self):
        try:
            with con:
                cur = con.cursor()
                cur.execute("SELECT * FROM course")
                return cur.fetchall()
        except Exception:
            return False

    # Delete data
    def delete_data(self, id):
        try:
            with con:
                cur = con.cursor()
                sql = "DELETE FROM course WHERE id = ?"
                cur.execute(sql, [id])
                return True
        except Exception:
            return False

#interface to user 

def main():
    print("*"*25) # START* PRINTED 40 TIMES
    print("\n:: COURSE MANAGEMENT :: \n")
    print("*"*25)
    print("\n")

    db = DatabaseManage()

    print("#\n"*10) # Print a harsh 40 times
    print("\n :: user Manual :: \n")
    print("#"*10)

    print('\nPress 1. Insert a new Course\n')
    print('Press 2. Show all Courses\n')
    print('Press 3. Delete a Course(NEED ID OF COURSE)\n')
    print("#"*40)
    print("\n")

    choice = input("\n Enter a choice: ")

    if choice =="1":
        name = input("\n Enter course name: ")
        description = input("\n Enter course description: ")
        price = input("\n Enter course price: ")
        is_private = input("\n Is this a private course? 0-Yes, 1-No: ")

        if db.insert_data([name, description, price, is_private]):
            print("Yay! Course was inserted successfully!")
        else:
            print("Yo! Something is wrong!")

    elif choice == "2":
        print("\n :: Course List")

        for index, item in enumerate(db.fetch_data()):
            print("\n Serial No: " + str(index + 1))
            print(" Course Id: " + str(item[0]))
            print(" Course Name: " + str(item[1]))
            print(" Course Description: " + str(item[2]))
            print(" Course Price: " + str(item[3]))
            is_private = 'YES' if item[4] else 'NO'
            print(" Course Privacy: " + is_private)
            print("\n")

    elif choice == "3":
        record_id = input("Enter the Course ID: ")

        if db.delete_data(record_id):
            print("Course deletded!")
        else:
            print("Opps! Something isn't OK!")

    else:
        print("\nBAD CHOICE!!!")


# Excecuting the main method only!
if __name__ == '__main__':
    main()

'''### Assignment

Create exact same application for youtube videos with:

name, 
description, 
tags(an array of tags)

'''
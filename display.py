import sqlite3 as sql
import table

table.create_table()
connection = sql.connect("hospital.sqlite", check_same_thread=False)


def display_doctor():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM doctor")
    row = cursor.fetchall()
    return row


def display_patient():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM patient")
    row = cursor.fetchall()
    return row
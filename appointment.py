import sqlite3 as sql
import table
import streamlit as st
table.create_table()
connection = sql.connect("hospital.sqlite", check_same_thread=False)

def doc_appointment(doc_id):
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(doctor_id) FROM patient WHERE doctor_id = ?", (doc_id, ))
    count = cursor.fetchone()
    return count
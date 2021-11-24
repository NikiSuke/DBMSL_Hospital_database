import sqlite3 as sql
import table
import streamlit as st
table.create_table()
connection = sql.connect("hospital.sqlite", check_same_thread=False)


def add_doctor(name, phone, branch):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO doctor (name, phone, branch) VALUES (?, ?, ?)", (name, phone, branch))
    cursor.connection.commit()
    st.write("Database Added")


def add_patient(doctor_id, name, phone):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO patient (doctor_id, name, phone) VALUES (?, ?, ?)", (doctor_id, name, phone))
    cursor.connection.commit()
    st.write("Database Added")

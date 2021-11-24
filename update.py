import sqlite3 as sql
import table
import streamlit as st
table.create_table()
connection = sql.connect("hospital.sqlite", check_same_thread=False)


def update_doctor(col_name, value, old_value):
    cursor = connection.cursor()
    query = f"SELECT doctor_id FROM doctor WHERE {col_name} = ?"
    cursor.execute(query, (old_value, ))
    row = cursor.fetchone()
    if row:
        update = f"UPDATE doctor SET {col_name} = ? WHERE doctor_id = ?"
        cursor.execute(update, (value, row[0]))
        cursor.connection.commit()
        st.write("Database updated")
    else:
        st.write("Not able to update please check")


def table_details(table_name):
    cursor = connection.cursor()
    query = f"SELECT * FROM {table_name}"
    cursor.execute(query)
    field_name = (i[0] for i in cursor.description)
    return field_name


def update_patient(col_name, new_value, old_value):
    cursor = connection.cursor()
    query = f"SELECT patient_id FROM patient WHERE {col_name} = ?"
    cursor.execute(query, (old_value,))
    row = cursor.fetchone()

    if row:
        if col_name != "doctor_id":
            update = f"UPDATE patient SET {col_name} = ? WHERE patient_id = ?"
            cursor.execute(update, (new_value, row[0]))
            cursor.connection.commit()
            st.write("Database updated")
        else:
            cursor.execute("SELECT * FROM doctor WHERE doctor_id = ?")
            id = cursor.fetchone()
            if id:
                update = f"UPDATE patient SET {col_name} = ? WHERE patient_id = ?"
                cursor.execute(update, (new_value, row[0]))
                cursor.connection.commit()
                st.write("Database updated")
            else:
                st.write("Doctor don't exist ")

    else:
        st.write("Not able to update please check")


if __name__ == "__main__":
    update_doctor("name", "pawar", "Pratiksha")
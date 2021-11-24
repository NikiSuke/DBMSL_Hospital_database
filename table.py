import sqlite3 as sql

connection = sql.connect("hospital.sqlite", check_same_thread=False)


def create_table():
    connection = sql.connect("hospital.sqlite")
    connection.execute("CREATE TABLE IF NOT EXISTS doctor (doctor_id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR, phone INTEGER, branch varchar)")
    connection.execute("CREATE TABLE IF NOT EXISTS patient (patient_id INTEGER PRIMARY KEY AUTOINCREMENT,doctor_id INTEGER, name VARCHAR, "
                       "phone INTEGER , FOREIGN KEY(doctor_id) REFERENCES doctor(doctor_id) ON DELETE SET NULL)")



if __name__ == "__main__":
    create_table()

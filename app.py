import streamlit as st
import insert
import display
import appointment
import update
side_box = st.sidebar.selectbox("Please select: ", ("Add", "Update", "Display", "Appointment"))

if side_box == "Add":
    add_choice = st.selectbox("Where you want to add: ", ("Doctor", "Patient"))
    if add_choice == "Doctor":
        with st.form("add_doctor", clear_on_submit=True):
            doc_name = st.text_input("Enter the name of the doctor")
            doc_phone = st.number_input("Enter the name number of doctor")
            doc_branch = st.text_input("Enter the branch of the doctor")
            submit_form_doc = st.form_submit_button("Submit")

            if submit_form_doc:
                insert.add_doctor(doc_name, doc_phone, doc_branch)
    elif add_choice == "Patient":
        with st.form("add_patient"):
            doc_details = st.selectbox("Select the doctor: ", display.display_doctor())
            patient_name = st.text_input("Enter the name of the patient: ")
            patient_phone = st.number_input("Enter the phone number: ")
            submit_patient = st.form_submit_button("Submit")

            if submit_patient:

                insert.add_patient(doc_details[0], patient_name, patient_phone)
elif side_box == "Display":
    choice = st.selectbox("Select the table name",("Doctor", "Patient"))
    if choice == "Doctor":
        st.write(display.display_doctor())

    elif choice == "Patient":
        st.write(display.display_patient())

elif side_box == "Appointment":
    doc_name = st.selectbox("Select the name of the doctor", (display.display_doctor()))
    count = appointment.doc_appointment(doc_name[0])
    st.write(f"The appointments taken by patients are: {count[0]}")

elif side_box == "Update":
    choice = st.selectbox("Select the table name", ("Doctor", "patient"))
    if choice == "Doctor":
        with st.form("update_doctor"):
            col_name = st.selectbox("Enter the name of the column: ", (update.table_details("doctor")))
            old_value = st.text_input("Enter the old value")
            new_value = st.text_input("Enter the new value")

            udate_submit_doctor = st.form_submit_button("submit")

            if udate_submit_doctor:
                update.update_doctor(col_name, new_value, old_value)
    elif choice == "patient":
        with st.form("Udpate_patient"):
            col_name = st.selectbox("Enter the name of the column: ", (update.table_details("patient")))
            old_value = st.text_input("Enter the old value")
            new_value = st.text_input("Enter the new value")

            update_submit_patient = st.form_submit_button("submit")

            if update_submit_patient:
                update.update_patient(col_name, new_value, old_value)

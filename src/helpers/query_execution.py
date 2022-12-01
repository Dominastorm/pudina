import streamlit as st
import pandas as pd
import mysql.connector

from sql.create import *
from sql.delete import *
from sql.display import *
from sql.update import *
from sql.insert import *


db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='bus_route_allocation_system'
)

cur = db.cursor()

def preset_query():
    operations = ["Insert", "Delete", "Update", "Display"]
    tables = ["User", "Project", "Task", "Comment"]

    operations_choice = st.selectbox("Operation", operations)
    tables_choice = st.selectbox("Table", tables)

    if operations_choice == "Insert":
        if tables_choice == "User":
            insert_user_st()
        elif tables_choice == "Project":
            insert_project_st()
        elif tables_choice == "Task":
            insert_task_st()
        elif tables_choice == "Comment":
            insert_comment_st()

    elif operations_choice == "Delete":
        if tables_choice == "User":
            delete_user_st()
        elif tables_choice == "Project":
            delete_project_st()
        elif tables_choice == "Task":
            delete_task_st()
        elif tables_choice == "Comment":
            delete_comment_st()

    elif operations_choice == "Update":
        if tables_choice == "User":
            update_user_st()
        elif tables_choice == "Project":
            update_project_st()
        elif tables_choice == "Task":
            update_task_st()
        elif tables_choice == "Comment":
            update_comment_st()

    elif operations_choice == "Display":
        if tables_choice == "User":
            display_user_st()
        elif tables_choice == "Project":
            display_project_st()
        elif tables_choice == "Task":
            display_task_st()
        elif tables_choice == "Comment":
            display_comment_st()


def excecute_query():
    st.title("SQL Query Execution")

    query_mode = ["Preset", "Manual Input"]
    query_choice = st.sidebar.selectbox("Input Method", query_mode)

    if query_choice == "Preset":
        preset_query()
    else:
        col1, col2 = st.columns(2)

        with col1:
            with st.form(key='query_form'):
                raw_code = st.text_area("Write SQL Code Here")
                submit_code = st.form_submit_button("Excecute code")

        with col2:
            if submit_code:
                st.info("Query Submitted")
                st.code(raw_code)

                cur.execute(raw_code)
                query_result = cur.fetchall()

                st.write("Results")
                with st.expander("JSON"):
                    st.write(query_result)

                with st.expander("Table"):
                    query_df = pd.DataFrame(query_result)
                    st.dataframe(query_df)

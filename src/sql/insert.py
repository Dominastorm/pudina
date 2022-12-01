import mysql.connector
from mysql.connector import IntegrityError
import streamlit as st

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pes1ug20cs127_pudina"
)

cursor = db.cursor()

'''
Function to insert values into task
'''
def insert_task(task_id, summary, status, priority, project_id, description, assignee, labels, reporter, start_date, due_date) -> None:
    try:
        cursor.execute("INSERT INTO Task VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (task_id, summary, status, priority, project_id, description, assignee, labels, reporter, start_date, due_date))
        db.commit()
        st.success("Task Created Successfully")
    except IntegrityError:
        st.error("Task ID already exists")
    except ValueError:
        st.error("Invalid data type(s)")

def insert_task_st() -> None:
    st.write("Insert Task")
    task_id = st.number_input("Task ID")
    summary = st.text_input("Summary")
    status = st.text_input("Status")
    priority = st.text_input("Priority")
    project_id = st.number_input("Project ID")
    description = st.text_input("Description")
    assignee = st.number_input("Assignee")
    labels = st.text_input("Labels")
    reporter = st.number_input("Reporter")
    start_date = st.date_input("Start Date")
    due_date = st.date_input("Due Date")
    if st.button("Insert Task"):
        insert_task(task_id, summary, status, priority, project_id, description, assignee, labels, reporter, start_date, due_date)


'''
Function to insert values into project
'''
def insert_project(project_id, name, type, lead) -> None:
    try:
        cursor.execute("INSERT INTO Project VALUES (%s, %s, %s, %s)", (project_id, name, type, lead))
        db.commit()
        st.success("Project Created Successfully")
    except IntegrityError:
        st.error("Project ID already exists")
    except ValueError:
        st.error("Invalid data type(s)")

def insert_project_st() -> None:
    st.write("Insert Project")
    project_id = st.number_input("Project ID")
    name = st.text_input("Name")
    type = st.text_input("Type")
    lead = st.number_input("Lead")
    if st.button("Insert Project"):
        insert_project(project_id, name, type, lead)


'''
Function to insert values into user
'''
def insert_user(user_id, username, password) -> None:
    try:
        cursor.execute("INSERT INTO User VALUES (%s, %s, %s)", (user_id, username, password))
        db.commit()
        st.success("User Created Successfully")
    except IntegrityError:
        st.error("User ID already exists")
    except ValueError:
        st.error("Invalid data type(s)")

def insert_user_st() -> None:
    st.write("Insert User")
    user_id = st.number_input("User ID")
    username = st.text_input("Username")
    password = st.text_input("Password")
    if st.button("Insert User"):
        insert_user(user_id, username, password)


'''
Function to insert values into comment
'''
def insert_comment(comment_id, task_id, user_id, text) -> None:
    try:
        cursor.execute("INSERT INTO Comment VALUES (%s, %s, %s, %s)", (comment_id, task_id, user_id, text))
        db.commit()
        st.success("Comment Created Successfully")
    except IntegrityError:
        st.error("Comment ID already exists")
    except ValueError:
        st.error("Invalid data type(s)")

def insert_comment_st() -> None:
    st.write("Insert Comment")
    comment_id = st.number_input("Comment ID")
    task_id = st.number_input("Task ID")
    user_id = st.number_input("User ID")
    text = st.text_input("Text")
    if st.button("Insert Comment"):
        insert_comment(comment_id, task_id, user_id, text)


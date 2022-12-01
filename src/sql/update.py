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
Function to update values in task
'''
def update_task(task_id, summary, status, priority, project_id, description, assignee, labels, reporter, start_date, due_date) -> None:
    try:
        cursor.execute("UPDATE Task SET summary = %s, status = %s, priority = %s, project_id = %s, description = %s, assignee = %s, labels = %s, reporter = %s, start_date = %s, due_date = %s WHERE task_id = %s", (summary, status, priority, project_id, description, assignee, labels, reporter, start_date, due_date, task_id))
        db.commit()
        st.success("Task Updated Successfully")
    except IntegrityError:
        st.error("Task ID does not exist")
    except ValueError:
        st.error("Invalid data type(s)")

def update_task_st() -> None:
    st.write("Update Task")
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
    if st.button("Update Task"):
        update_task(task_id, summary, status, priority, project_id, description, assignee, labels, reporter, start_date, due_date)


'''
Function to update values in project
'''
def update_project(project_id, name, type, lead) -> None:
    try:
        cursor.execute("UPDATE Project SET name = %s, type = %s, lead = %s WHERE project_id = %s", (name, type, lead, project_id))
        db.commit()
        st.success("Project Updated Successfully")
    except IntegrityError:
        st.error("Project ID does not exist")
    except ValueError:
        st.error("Invalid data type(s)")

def update_project_st() -> None:
    st.write("Update Project")
    project_id = st.number_input("Project ID")
    name = st.text_input("Name")
    type = st.text_input("Type")
    lead = st.number_input("Lead")
    if st.button("Update Project"):
        update_project(project_id, name, type, lead)


'''
Function to update values in user
'''
def update_user(user_id, username, password) -> None:
    try:
        cursor.execute("UPDATE User SET username = %s, password = %s WHERE user_id = %s", (username, password, user_id))
        db.commit()
        st.success("User Updated Successfully")
    except IntegrityError:
        st.error("User ID does not exist")
    except ValueError:
        st.error("Invalid data type(s)")

def update_user_st() -> None:
    st.write("Update User")
    user_id = st.number_input("User ID")
    username = st.text_input("Username")
    password = st.text_input("Password")
    if st.button("Update User"):
        update_user(user_id, username, password)


'''
Function to update values in comment
'''
def update_comment(comment_id, task_id, user_id, text) -> None:
    try:
        cursor.execute("UPDATE Comment SET task_id = %s, user_id = %s, text = %s WHERE comment_id = %s", (task_id, user_id, text, comment_id))
        db.commit()
        st.success("Comment Updated Successfully")
    except IntegrityError:
        st.error("Comment ID does not exist")
    except ValueError:
        st.error("Invalid data type(s)")

def update_comment_st() -> None:
    st.write("Update Comment")
    comment_id = st.number_input("Comment ID")
    task_id = st.number_input("Task ID")
    user_id = st.number_input("User ID")
    text = st.text_input("Text")
    if st.button("Update Comment"):
        update_comment(comment_id, task_id, user_id, text)

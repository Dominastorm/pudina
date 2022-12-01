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
Function to delete values from task
'''
def delete_task(task_id) -> None:
    try:
        cursor.execute("DELETE FROM Task WHERE task_id = %s", (task_id,))
        db.commit()
        st.success("Task Deleted Successfully")
    except IntegrityError:
        st.error("Task ID cannot be deleted due to integrity error")
    except ValueError:
        st.error("Invalid data type(s)")

def delete_task_st() -> None:
    st.write("Delete Task")
    task_id = st.number_input("Task ID")
    if st.button("Delete Task"):
        delete_task(task_id)


'''
Function to delete values from project
'''
def delete_project(project_id) -> None:
    try:
        cursor.execute("DELETE FROM Project WHERE project_id = %s", (project_id,))
        db.commit()
        st.success("Project Deleted Successfully")
    except IntegrityError:
        st.error("Project ID cannot be deleted due to integrity error")
    except ValueError:
        st.error("Invalid data type(s)")

def delete_project_st() -> None:
    st.write("Delete Project")
    project_id = st.number_input("Project ID")
    if st.button("Delete Project"):
        delete_project(project_id)

'''
Function to delete values from user
'''
def delete_user(user_id) -> None:
    try:
        cursor.execute("DELETE FROM User WHERE user_id = %s", (user_id,))
        db.commit()
        st.success("User Deleted Successfully")
    except IntegrityError:
        st.error("User ID cannot be deleted due to integrity error")
    except ValueError:
        st.error("Invalid data type(s)")

def delete_user_st() -> None:   
    st.write("Delete User")
    user_id = st.number_input("User ID")
    if st.button("Delete User"):
        delete_user(user_id)


'''
Function to delete values from comment
'''
def delete_comment(comment_id) -> None:
    try:
        cursor.execute("DELETE FROM Comment WHERE comment_id = %s", (comment_id,))
        db.commit()
        st.success("Comment Deleted Successfully")
    except IntegrityError:
        st.error("Comment ID cannot be deleted due to integrity error")
    except ValueError:
        st.error("Invalid data type(s)")

def delete_comment_st() -> None:
    st.write("Delete Comment")
    comment_id = st.number_input("Comment ID")
    if st.button("Delete Comment"):
        delete_comment(comment_id)

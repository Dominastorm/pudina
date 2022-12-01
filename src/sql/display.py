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
Function to display values in task
'''
def display_task() -> None:
    cursor.execute("SELECT * FROM Task")
    result = cursor.fetchall()
    st.write(result)

def display_task_st() -> None:
    st.write("Display Task")
    if st.button("Display Task"):
        display_task()


'''
Function to display values in project
'''
def display_project() -> None:
    cursor.execute("SELECT * FROM Project")
    result = cursor.fetchall()
    st.write(result)

def display_project_st() -> None:
    st.write("Display Project")
    if st.button("Display Project"):
        display_project()


'''
Function to display values in user
'''
def display_user() -> None:
    cursor.execute("SELECT * FROM User")
    result = cursor.fetchall()
    st.write(result)

def display_user_st() -> None:
    st.write("Display User")
    if st.button("Display User"):
        display_user()


'''
Function to display values in comment
'''
def display_comment() -> None:
    cursor.execute("SELECT * FROM Comment")
    result = cursor.fetchall()
    st.write(result)

def display_comment_st() -> None:
    st.write("Display Comment")
    if st.button("Display Comment"):
        display_comment()


'''
Function to display values in task
'''
def display_task() -> None:
    cursor.execute("SELECT * FROM Task")
    result = cursor.fetchall()
    st.write(result)

def display_task_st() -> None:
    st.write("Display Task")
    if st.button("Display Task"):
        display_task()


'''
Function to display values in project
'''
def display_project() -> None:
    cursor.execute("SELECT * FROM Project")
    result = cursor.fetchall()
    st.write(result)

def display_project_st() -> None:
    st.write("Display Project")
    if st.button("Display Project"):
        display_project()


'''
Function to display values in user
'''
def display_user() -> None:
    cursor.execute("SELECT * FROM User")
    result = cursor.fetchall()
    st.write(result)

def display_user_st() -> None:
    st.write("Display User")
    if st.button("Display User"):
        display_user()


'''
Function to display values in comment
'''
def display_comment() -> None:
    cursor.execute("SELECT * FROM Comment")
    result = cursor.fetchall()
    st.write(result)

def display_comment_st() -> None:
    st.write("Display Comment")
    if st.button("Display Comment"):
        display_comment()

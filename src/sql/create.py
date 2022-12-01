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
Function to create all the tables
'''
def create_tables():
    # Create User table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS User (
    user_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(255),
    password VARCHAR(255)
    );
    """)

    # Create Project table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Project (
    project_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255),
    type VARCHAR(255),
    lead INTEGER,
    FOREIGN KEY (lead) REFERENCES User(user_id)
    );
    """)

    # Create Task table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Task (
    task_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    summary VARCHAR(255),
    status VARCHAR(255),
    priority VARCHAR(255),
    project_id INTEGER,
    description VARCHAR(255),
    assignee INTEGER,
    labels VARCHAR(255),
    reporter INTEGER,
    start_date DATE,
    due_date DATE,
    FOREIGN KEY (project_id) REFERENCES Project(project_id),
    FOREIGN KEY (assignee) REFERENCES User(user_id),
    FOREIGN KEY (reporter) REFERENCES User(user_id)
    );
    """)

    # Create Comment table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Comment (
    comment_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    task_id INTEGER,
    user_id INTEGER,
    text VARCHAR(255),
    FOREIGN KEY (task_id) REFERENCES Task(task_id),
    FOREIGN KEY (user_id) REFERENCES User(user_id)
    );
    """)

    db.commit()
    
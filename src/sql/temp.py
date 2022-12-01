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

def insert_values()
    # Insert User 1
    cursor.execute("""
    INSERT INTO User (username, password)
    VALUES ("jeffrey", "pw123");
    """)

     # Insert User 2
    cursor.execute("""
    INSERT INTO User (username, password)
    VALUES ("bob", "pw456");
    """)

    # Insert User 3
    cursor.execute("""
    INSERT INTO User (username, password)
    VALUES ("michelle", "pw789");
    """)

    # Insert User 4
    cursor.execute("""
    INSERT INTO User (username, password)
    VALUES ("john", "pw101");
    """)

    # Insert User 5
    cursor.execute("""
    INSERT INTO User (username, password)
    VALUES ("sarah", "pw112");
    """)

    # Insert Project 1
    cursor.execute("""
    INSERT INTO Project (name, type, lead)
    VALUES ("website", "web development", 1);
    """)

    # Insert Project 2
    cursor.execute("""
    INSERT INTO Project (name, type, lead)
    VALUES ("e-commerce", "web development", 2);
    """)

    # Insert Project 3
    cursor.execute("""
    INSERT INTO Project (name, type, lead)
    VALUES ("app", "mobile development", 3);
    """)

    # Insert Project 4
    cursor.execute("""
    INSERT INTO Project (name, type, lead)
    VALUES ("database", "database development", 4);
    """)

    # Insert Project 5
    cursor.execute("""
    INSERT INTO Project (name, type, lead)
    VALUES ("workflow", "process automation", 5);
    """)

    # Insert Task 1
    cursor.execute("""
    INSERT INTO Task (summary, status, priority, project_id, description, assignee, labels, reporter, start_date, due_date)
    VALUES ("Create homepage", "open", "high", 1, "Create a homepage for the website", 1, "design, web development", 1, "2020-01-02", "2020-01-15");
    """)

    # Insert Task 2
    cursor.execute("""
    INSERT INTO Task (summary, status, priority, project_id, description, assignee, labels, reporter, start_date, due_date)
    VALUES ("Design login page", "open", "medium", 2, "Design the login page for the e-commerce site", 2, "design, web development", 2, "2020-01-03", "2020-01-20");
    """)

    # Insert Task 3
    cursor.execute("""
    INSERT INTO Task (summary, status, priority, project_id, description, assignee, labels, reporter, start_date, due_date)
    VALUES ("Implement login feature", "open", "low", 3, "Implement the login feature for the mobile app", 3, "mobile development, mobile app", 3, "2020-01-05", "2020-01-25");
    """)

    # Insert Task 4
    cursor.execute("""
    INSERT INTO Task (summary, status, priority, project_id, description, assignee, labels, reporter, start_date, due_date)
    VALUES ("Create database schema", "open", "high", 4, "Create a database schema for the database project", 4, "database, database development", 4, "2020-01-01", "2020-01-17");
    """)

    # Insert Task 5
    cursor.execute("""
    INSERT INTO Task (summary, status, priority, project_id, description, assignee, labels, reporter, start_date, due_date)
    VALUES ("Create workflow diagram", "open", "medium", 5, "Create a workflow diagram for the process automation project", 5, "workflow, process automation", 5, "2020-01-04", "2020-01-22");
    """)

    # Insert Comment 1
    cursor.execute("""
    INSERT INTO Comment (task_id, user_id, text)
    VALUES (1, 1, "Let's start working on this today");
    """)

    # Insert Comment 2
    cursor.execute("""
    INSERT INTO Comment (task_id, user_id, text)
    VALUES (2, 2, "I think it should look like this...");
    """)

    # Insert Comment 3
    cursor.execute("""
    INSERT INTO Comment (task_id, user_id, text)
    VALUES (3, 3, "We should use this library");
    """)

    # Insert Comment 4
    cursor.execute("""
    INSERT INTO Comment (task_id, user_id, text)
    VALUES (4, 4, "Let's make sure to index the columns");
    """)

    # Insert Comment 5
    cursor.execute("""
    INSERT INTO Comment (task_id, user_id, text)
    VALUES (5, 5, "I think this will work");
    """)

    # Commit changes
    db.commit()
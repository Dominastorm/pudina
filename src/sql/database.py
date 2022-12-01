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


'''
Function to delete values from task
'''
def delete_task(task_id) -> None:
    try:
        cursor.execute("DELETE FROM Task WHERE task_id = %s", (task_id,))
        db.commit()
        st.success("Task Deleted Successfully")
    except IntegrityError:
        st.error("Task ID does not exist")
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
        st.error("Project ID does not exist")
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
        st.error("User ID does not exist")
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
        st.error("Comment ID does not exist")
    except ValueError:
        st.error("Invalid data type(s)")

def delete_comment_st() -> None:
    st.write("Delete Comment")
    comment_id = st.number_input("Comment ID")
    if st.button("Delete Comment"):
        delete_comment(comment_id)


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


'''
Function to delete values in task
'''
def delete_task(task_id) -> None:
    try:
        cursor.execute("DELETE FROM Task WHERE task_id = %s", (task_id))
        db.commit()
        st.success("Task Deleted Successfully")
    except IntegrityError:
        st.error("Task ID does not exist")
    except ValueError:
        st.error("Invalid data type(s)")

def delete_task_st() -> None:
    st.write("Delete Task")
    task_id = st.number_input("Task ID")
    if st.button("Delete Task"):
        delete_task(task_id)


'''
Function to delete values in project
'''
def delete_project(project_id) -> None:
    try:
        cursor.execute("DELETE FROM Project WHERE project_id = %s", (project_id))
        db.commit()
        st.success("Project Deleted Successfully")
    except IntegrityError:
        st.error("Project ID does not exist")
    except ValueError:
        st.error("Invalid data type(s)")

def delete_project_st() -> None:
    st.write("Delete Project")
    project_id = st.number_input("Project ID")
    if st.button("Delete Project"):
        delete_project(project_id)


'''
Function to delete values in user
'''
def delete_user(user_id) -> None:
    try:
        cursor.execute("DELETE FROM User WHERE user_id = %s", (user_id))
        db.commit()
        st.success("User Deleted Successfully")
    except IntegrityError:
        st.error("User ID does not exist")
    except ValueError:
        st.error("Invalid data type(s)")

def delete_user_st() -> None:
    st.write("Delete User")
    user_id = st.number_input("User ID")
    if st.button("Delete User"):
        delete_user(user_id)


'''
Function to delete values in comment
'''
def delete_comment(comment_id) -> None:
    try:
        cursor.execute("DELETE FROM Comment WHERE comment_id = %s", (comment_id))
        db.commit()
        st.success("Comment Deleted Successfully")
    except IntegrityError:
        st.error("Comment ID does not exist")
    except ValueError:
        st.error("Invalid data type(s)")

def delete_comment_st() -> None:
    st.write("Delete Comment")
    comment_id = st.number_input("Comment ID")
    if st.button("Delete Comment"):
        delete_comment(comment_id)


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



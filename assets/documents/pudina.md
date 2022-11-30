ENTITITES:
-Task
-Project
-User
-Comment

ATTRIBUTES:
-Task: task_id, summary, status, priority, project_id, description, assignee, labels, reporter, start date, due date
-Project: project_id, name, type, lead
-User: user_id, username, password
-Comment: comment_id, task_id, user_id, text

DATATYPES:
-task_id: integer
-summary: string
-status: string
-priority: string
-project_id: integer
-description: string
-assignee: user_id
-labels: string
-reporter: user_id
-start date: date
-due date: date
-project_id: integer
-name: string
-type: string
-lead: user_id
-user_id: integer
-username: string
-password: string
-comment_id: integer
-task_id: integer
-user_id: integer
-text: string

RELATIONSHIPS:
-One issue can be assigned to one project (1:1)
-One project can have many issues (1:N)
-One user can be assigned to many issues (1:N)
-One issue can have many comments (1:N)
-One comment can be made by one user (1:1)
-One user can be part of many projects (M:N)
-One comment can belong to one task (1:1)
-One user can make many comments (1:N)

Write MySQL queries for implementing the above entities and relationships (e.g., to create a table for a given entity).

Task: 
CREATE TABLE Task (
task_id INTEGER,
summary VARCHAR(255),
status VARCHAR(255),
priority VARCHAR(255),
project_id INTEGER,
description VARCHAR(255),
assignee INTEGER,
labels VARCHAR(255),
reporter INTEGER,
start_date DATE,
due_date DATE
);

Project: 
CREATE TABLE Project (
project_id INTEGER,
name VARCHAR(255),
type VARCHAR(255),
lead INTEGER
);

User: 
CREATE TABLE User (
user_id INTEGER,
username VARCHAR(255),
password VARCHAR(255)
);

Comment: 
CREATE TABLE Comment (
comment_id INTEGER,
task_id INTEGER,
user_id INTEGER,
text VARCHAR(255)
);

Write different methods and statements used to populate data

INSERT INTO Task (task_id, summary, status, priority, project_id, description, assignee, labels, reporter, start_date, due_date)
VALUES (1, 'Finish project', 'In Progress', 'High', 1, 'Need to finish project by end of week', 1, 'project, finish', 1, '2018-01-01', '2018-01-05');

INSERT INTO Project (project_id, name, type, lead)
VALUES (1, 'Project 1', 'Type 1', 1);

INSERT INTO User (user_id, username, password)
VALUES (1, 'JohnDoe', 'password');

INSERT INTO Comment (comment_id, task_id, user_id, text)
VALUES (1, 1, 1, 'This is a comment.');

Write join queries to retrieve data from multiple tables

SELECT * FROM Task JOIN Project ON Task.project_id=Project.project_id;
SELECT * FROM Task JOIN User ON Task.assignee=User.user_id;
SELECT * FROM Comment JOIN User ON Comment.user_id=User.user_id;

Write aggregate functions used to calculate data across multiple rows

SELECT COUNT(*) FROM Task;
SELECT SUM(task_id) FROM Task;
SELECT AVG(task_id) FROM Task;
SELECT MAX(task_id) FROM Task;
SELECT MIN(task_id) FROM Task;

Write set operations used to combine data from multiple tables

UNION:
SELECT * FROM Task UNION SELECT * FROM Project;

INTERSECT:
SELECT * FROM Task INTERSECT SELECT * FROM Project;

EXCEPT:
SELECT * FROM Task EXCEPT SELECT * FROM Project;

Write functions and procedures to perform various operations on the data

CREATE FUNCTION getTask(id INT) RETURNS Task
BEGIN
    RETURN (SELECT * FROM Task WHERE task_id=id);
END;

CREATE PROCEDURE updateTask(id INT, summary VARCHAR(255), status VARCHAR(255), priority VARCHAR(255), project_id INTEGER, description VARCHAR(255), assignee INTEGER, labels VARCHAR(255), reporter INTEGER, start_date DATE, due_date DATE)
BEGIN
    UPDATE Task SET summary=summary, status=status, priority=priority, project_id=project_id, description=description, assignee=assignee, labels=labels, reporter=reporter, start_date=start_date, due_date=due_date WHERE task_id=id;
END;



Write triggers and cursors



A trigger is a stored procedure that is automatically executed when an event occurs in the database. A cursor is a pointer that points to a specific row in a table. 

CREATE TRIGGER tr_Task
AFTER INSERT ON Task
FOR EACH ROW
BEGIN
INSERT INTO Comment (comment_id, task_id, user_id, text)
VALUES (NULL, NEW.task_id, 1, 'This is a comment.');
END;
/

CREATE CURSOR cur_Task (task_id INTEGER)
IS
SELECT * FROM Task WHERE task_id = task_id;

OPEN cur_Task(1);
FETCH cur_Task INTO task_id, summary, status, priority, project_id, description, assignee, labels, reporter, start_date, due_date;
CLOSE cur_Task;

![pudina-erd](C:\Desktop\_MyFolders\MyProjects\pudina\assets\images\pudina-erd.png)

![image-20221117172108308](C:\Users\dchaw\AppData\Roaming\Typora\typora-user-images\image-20221117172108308.png)
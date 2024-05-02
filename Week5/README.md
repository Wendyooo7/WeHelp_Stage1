# Task 2: Create database and table in your MySQL server
### ●	Create a new database named website.
<img src="Task5_screenshots/Task2_1_create database website;.JPG">

### ●	Create a new table named member, in the website database, designed as below:
<img src="Task5_screenshots/Task2_2_create table member();.JPG">

# Task 3: SQL CRUD
### ●	INSERT a new row to the member table where name, username and password must be set to test. INSERT additional 4 rows with arbitrary data.
<img src="Task5_screenshots/Task3_1_insert 5 rows.JPG">

### ●	SELECT all rows from the member table.
<img src="Task5_screenshots/Task3_2_SELECT all FROM member;.JPG">

### ●	SELECT all rows from the member table, in descending order of time.
<img src="Task5_screenshots/Task3_3_SELECT all FROM member ORDER BY time DESC;.JPG">

### ●	SELECT total 3 rows, second to fourth, from the member table, in descending order of time. Note: it does not mean SELECT rows where id are 2, 3, or 4.
<img src="Task5_screenshots/Task3_4_SELECT all FROM member ORDER BY time DESC 選第二到四行.JPG">

### ●	SELECT rows where username equals to test.
<img src="Task5_screenshots/Task3_5_選所有username=test的row.JPG">

### ●	SELECT rows where name includes the es keyword.
<img src="Task5_screenshots/Task3_6_選所有name中包含es的row.JPG">

### ●	SELECT rows where both username and password equal to test.
<img src="Task5_screenshots/Task3_7_選取所有username和password都是test的row.JPG">

### ●	UPDATE data in name column to test2 where username equals to test.
<img src="Task5_screenshots/Task3_8_1將username為test的row的name改成test2_指令.JPG">
<img src="Task5_screenshots/Task3_8_2將username為test的row的name改成test2_結果.JPG">

# Task 4: SQL Aggregation Functions
### ●	SELECT how many rows from the member table.
<img src="Task5_screenshots/Task4_1_計算總行數.JPG">

### ●	SELECT the sum of follower_count of all the rows from the member table.
<img src="Task5_screenshots/Task4_2_計算追蹤數總和.JPG">

### ●	SELECT the average of follower_count of all the rows from the member table.
<img src="Task5_screenshots/Task4_3_計算追蹤數總平均.JPG">

### ●	SELECT the average of follower_count of the first 2 rows, in descending order of follower_count, from the member table.
<img src="Task5_screenshots/Task4_4_計算追蹤數降冪前兩row總平均.JPG">

# Task 5: SQL JOIN
### ●	Create a new table named message, in the website database. designed as below:
<img src="Task5_screenshots/Task5_1_建立message表格.JPG">

### 補充：為message table建立五筆測資 
INSERT 5 rows with assigned and arbitrary data to message table.
<img src="Task5_screenshots/Task5_1.5_為message表格建5rows.JPG">

### ●	SELECT all messages, including sender names. We have to JOIN the member table to get that.
<img src="Task5_screenshots/Task5_2.JPG">

### ●	SELECT all messages, including sender names, where sender username equals to test. We have to JOIN the member table to filter and get that.
<img src="Task5_screenshots/Task5_3.JPG">

### ●	Use SELECT, SQL Aggregation Functions with JOIN statement, get the average like count of messages where sender username equals to test.
<img src="Task5_screenshots/Task5_4.JPG">

### ●	Use SELECT, SQL Aggregation Functions with JOIN statement, get the average like count of messages GROUP BY sender username.
<img src="Task5_screenshots/Task5_5.JPG">

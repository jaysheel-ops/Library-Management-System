# Library-Management-System

To execute the following app, the following Prerequisite are required- 

1. Python Modules 

  -->tkinter – Please run below command to install tkinter
  
     pip install tkinter

  -->pillow – Please run below command to install tkinter
  
     pip install pillow

  -->pymysql – Please run below command to install tkinter
  
     pip install pymysql
  
2. MySQL Community Server
3. 
-->MySQL workbench community server has to be installed on your local computer where you aim to launch the app.

  The following lines are needed to be executed in MySQL Command Line Client before going to the app-

  create database db;
  
  create table books(bid varchar(20) primary key, title varchar(30), author varchar(30), status varchar(30));
  
  create table books_issued(bid varchar(20) primary key, issuedto varchar(30));

  -->This creates a local database,and tables within the database for our app to operate on.

After complete installation of the prerequisites you can successfully launch the app through your terminal by writing the following code - 
  -->While doing this make sure your cmd is in the current working directory
  
     python main.py 
     
     

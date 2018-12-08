# TweetScanner with MySQL and MongoDB
This is a project undertaken at Boston University in class EC601. 
## Goal
The aim of this project is to create a python program which does the following:
* Takes a twitter handle from the user
* Downloads the images from that twitter handle
* Compiles a video out of the images using FFMPEG
* Uses the google cloud intelligence API to figure out a brief description about the stuff being tweeted about.
## Setup
The project implements both MySQL and MongoDB and hence has separate requirements for the same
### MongoDB
Run the following commands in your terminal (Linux)

```sudo apt-get install mongodb```

```pip install pymongo```

This should let your computer work with the programs
### MySQL
Download the MySQL package from the following website for your particular operating system

```https://www.mysql.com/downloads```

Run the following command in your terminal

```pip install mysql-connector-python```

This should make it run with the MySQL library
## Database Structure
### MySQL
The data is stored in tables with one of them having a primary key (Cannot be repeated). The rest are dependent on the primary table.
The database consists of 3 tables
* Tweethistory
* Tags
* Images

Tweethistory has 2 columns
* UserID: primary key, unique for every entry
* LastUsed: Last time a particular UserID accessed the program (Stored in format YYYY-MM-DD HH:MM:SS)

Tags has 3 columns
* UserID
* Handle
* Tags
Each entry here contains a tag associated with a particular handle. 

Images has 3 columns
* UserID
* Handle
* Images
Each entry here contains the number of images downloaded for each session, associated with a particular handle. 
This structure is used because we cannot have multiple values for a cell in MySQL.
### MongoDB
The data in the MongoDB is stored as Documents inside collections, which is analogus to Entries inside Tables.
A sample entry is as follows:
```
{'_id': 1,
 		  'LastUsed': time,
 		  'usage' : [
 						{
 						'Tags' : ['Metropolitan', 'Cityscape', 'Urban'],
 						'Handle' : 'BUTweets',
 						'Images' : 100
 						},
 						{
 						'Tags' : ['Dogs', 'Labrador'],
 						'Handle' : 'Dogsforlife',
 						'Images' : 100
 						}
 					]
 }
 ```
 ## Running the program
 Clone the repository in your computer for using the application.
 The program is run via the command line. Use the following command in the terminal:
 
 ```python  main_program.py```
 
An addition from the previous release is the inclusion of UserID for the user. One must remember theirs after it is generated for further use of the application and the database.
## Using the database data
The database data can be accessed by either using the respective command line tools for MySQL and MongoDB, or specialised functions have been made for both

Run the following command in the terminal

```python stats.py```

and follow the on-screen instructions

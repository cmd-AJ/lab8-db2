# CSV to MongoDB Importer
This script reads data from a CSV file (sup.csv) and imports it into a MongoDB collection called sup in the lab8 database. It uses bulk operations for efficient insertion.

Features
- Reads a CSV file and parses each row.

- Converts certain fields to int or float types.

- Performs a bulk insert into MongoDB for efficiency.

- Loads MongoDB connection details securely from a .env file.

Requirements
- Python 3.7+

- MongoDB instance 

- sup.csv 

Installation
Clone the repository or copy the script to your project directory.

Install required Python packages:
  pip install python-dotenv pymongo
Create a .env file in the project directory with your MongoDB connection URL:


  Date	Product Name	Category	Units Sold	Price	Revenue	Discount	Units Returned	Location	Platform
  2025-01-01	Example Item	Toys	100	10.5	1050.0	0.1	2	New York	Amazon

To run the python file
  python main.py
If the CSV contains valid data, the script will bulk insert all rows into MongoDB and print the number of documents inserted.


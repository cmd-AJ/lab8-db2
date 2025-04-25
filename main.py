from dotenv import load_dotenv
from pymongo import MongoClient, InsertOne
import csv
import os


load_dotenv()

mongo_url = os.getenv("MONGO_URL")
# Connect to MongoDB
client = MongoClient(mongo_url)
db = client["lab8"]
collection = db["sup"]

# Prepare bulk operations
operations = [ ]

with open("sup.csv", newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Convert fields to appropriate types if needed
        doc = {
            "Date": row["Date"],
            "Product Name": row["Product Name"],
            "Category": row["Category"],
            "Units Sold": int(row["Units Sold"]),
            "Price": float(row["Price"]),
            "Revenue": float(row["Revenue"]),
            "Discount": float(row["Discount"]),
            "Units Returned": int(row["Units Returned"]),
            "Location": row["Location"],
            "Platform": row["Platform"]
        }
        operations.append(InsertOne(doc))



if operations:
    result = collection.bulk_write(operations)
    print(f"Inserted: {result.inserted_count} documents")
else:
    print("No data found to insert.")
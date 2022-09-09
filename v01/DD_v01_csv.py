import csv
from pathlib import Path

DB_PATH = Path("C:/#####################/D3Bot/v01/test_data.csv")

def create_db_list(db_file_path):

    db = []

    with open(db_file_path, newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            db.append(row)
    
    return(db)

'''
a = create_db_list(DB_PATH)
print(a)
'''

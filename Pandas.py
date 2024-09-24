import pandas as pd
import csv
import os
from pathlib import Path

current_dir = os.path.dirname(os.path.abspath(__file__))
csv_file_path_student = os.path.join(current_dir, 'student.csv')
csv_file_path_homes = os.path.join(current_dir, 'homes.csv')
downloads_folder = Path.home() / "Downloads"

df = pd.read_csv(csv_file_path_homes) 



RandB = df[["Rooms","Beds"]] 
Age1 = df[df["Age"] > 20] 
Average = df.groupby("Baths")["Taxes"].mean() 

df["Average"]= df.groupby("Baths")["Taxes"].transform("mean") 

Sort =  df.sort_values(by="Age") 
Replacing = df.replace({"Beds":{4}},7) 
Dropping = df.dropna() 
Saving = df.to_csv(os.path.join(downloads_folder, "save_new_file.csv")) 

dstudent = pd.read_csv(csv_file_path_student) 
newdf = pd.concat([df,dstudent]) 

AverageMark = dstudent.groupby("gender")["mark"].mean() 
saveAverageMark = AverageMark.to_csv(os.path.join(downloads_folder, "average_mark.csv"))


print(df)
print(RandB)
print(Age1)
print(Average)
print(df["Average"])
print(Sort)
print(dstudent)
print(newdf)
print(AverageMark)


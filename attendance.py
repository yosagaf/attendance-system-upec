
import random
import time
from datetime import datetime
import csv
import os

# Generate random list and pick a random student ID
def generate_unique_id(num_low, num_high):
    random_numbers = range(num_low, num_high)  
    list_id = list(random_numbers)    

    ID = random.choice(list_id)
    if ID in list_id:
        list_id.remove(ID)

    return ID
   
# Get date and time in string format
def generate_date_time():
    ts = time.time()
    date = datetime.fromtimestamp(ts).strftime('%m-%d-%Y')
    time_stamp = datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    time_date = [str(date), str(time_stamp)]

    return time_date

# Save recoreded informations on the csv file
def write_attendance():
    i = 0
    student_name = "Sagaf"
    student_id = str(generate_unique_id(433000, 433050))
    record_time = generate_date_time()[1]
    attendance = [student_id, student_name, record_time]
    list_students = []
    
    headers = [
        'STUDENT_ID', 
        'STUDENT_NAME', 
        'DETECTION_TIME'
    ]

    # Check if the csv file exist
    exists = os.path.isfile("attendance.csv")

    if exists:
        with open("attendance.csv", 'a+') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(attendance)
            
        f.close()
    
    else:
        with open("attendance.csv", 'a+') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(headers)
            csv_writer.writerow(attendance)
        f.close()
    
    with open('attendance.csv') as ff:
        reader = csv.reader(ff)
        line = next(reader)
        for line in reader:
            list_students.append(line)
            infos_student = line  
    return list_students 

#write_attendance()
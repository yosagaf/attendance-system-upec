
import random
import time
from datetime import datetime
import csv
import os

# Generate random list od number and pick a random student ID
def generate_unique_id(num_low, num_high):

    # num_low : low range
    # num_high : high range
    random_numbers = range(num_low, num_high)  
    list_id = list(random_numbers)    

    ID = random.choice(list_id)
    if ID in list_id:
        list_id.remove(ID) # remove used ID from the list of student ID

    return ID
   
# Get date and time in string format
def generate_date_time():

    ts = time.time()
    date = datetime.fromtimestamp(ts).strftime('%m-%d-%Y')
    time_stamp = datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    time_date = [str(date), str(time_stamp)]

    return time_date
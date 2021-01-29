
# Face recognition/identification for attendance management :

The purpose of this project is to develop a computer vision system to manage students attendance in university classroom.
Software application will be installed in classroom at UPEC and should generate statisticacs of attendance

# Requirements

Python 3.7 or later with all [requirements.txt](https://github.com/yosagaf/attendance-system-upec/blob/main/requirements.txt) dependencies installed, 
To install run :
```bash
$ pip install -r requirements.txt
```

# Instructions :
The model is already trained with for 3 persons for demo. To use the application with new persons, you need to clear attendance.csv file and leave only the header. Using the GUI or manually, create a directory with the name of the student and add around 10 images. You can train the model from the GUI with the new added person. The easiest way is to decommente line 254 to 258 and commente others line from 259. At this point, you can run : `python3 knn_classifier.py`. And the model will be generated. At this point you can run the application.

# Demo
To run the application : `./run` or `python3 app.py`

# System flow chart
![Alt text](images/system_flow_chart.png?raw=true "Results")

# Results
![Alt text](images/results.png?raw=true "Results")
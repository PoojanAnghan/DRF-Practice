import requests
import json

# URL = 'http://127.0.0.1:8000/studentInfo/'
# req = requests.get(URL)
# data = req.json()
# i = 0
# for data in data:
#     print("Student :", i+1)
#     for key in data:
#         print(f"{key} : {data[key]}")



# print(f"{'-'*15} Single Record Access {'-'*15}")
# URL = 'http://127.0.0.1:8000/studentInfo/1'
# req = requests.get(URL)
# data = req.json()

# for key in data:
#     print(f"{key} : {data[key]}")


URL = 'http://127.0.0.1:8000/studentInfo/'
def get_student_details(id = None):
    data = {}
    if id is not None:
        data = {'id' : id}
        json_data = json.dumps(data)
        res =  requests.get(url= URL, data=json_data)
        data = res.json()
        print(data)
    else:
        data = {'id' : None}
        json_data = json.dumps(data)
        res =  requests.get(url= URL, data=json_data)
        data = res.json()
        print(data)

# get_student_details()
# get_student_details(4)

URL = 'http://127.0.0.1:8000/student/opr'


def add_student():
    data = {
        'name': 'OG',
        'roll': 5,
        'city': 'Surat'
    }
    res = requests.post(url=URL, json=data)   
    print(res.json()['msg'])

def update_student():
    data = {
        'id': 13,
        'name': 'og',
        'roll': 5
    }
    res = requests.put(url=URL, json=data)  
    print(res.json()['msg'])

def delete_student():
    data = {
        'id': 15
    }
    res = requests.delete(url=URL, json=data) 
    print(res.json()['msg'])



# add_student()
# update_student()
delete_student()
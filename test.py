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
# data = req

# for key in data:
#     print(f"{key} : {data[key]}")

print(f"{'-'*15} Single Record Push {'-'*15}")
URL = 'http://127.0.0.1:8000/student/add'

data = {
    'name': 'krish',
    'roll': 4,
    'city': 'Surat'
}

res = requests.post(url=URL, json=data)

# Parse JSON response into a dict
data = res.json()

print(data['msg'])  # ✅ works fine
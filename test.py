import requests

BASE_URL = 'http://127.0.0.1:8000'


def get_student_details(id=None):
    if id:
        res = requests.get(f"{BASE_URL}/students/{id}/")
    else:
        res = requests.get(f"{BASE_URL}/students/")
    
    if res.status_code == 200:
        print(res.json())
    else:
        print(f"Error: {res.status_code} - {res.text}")


def add_student():
    data = {
        'name': 'OG',
        'roll': 5,
        'city': 'Surat'
    }
    res = requests.post(f"{BASE_URL}/students/", json=data)
    print(res.json())


def update_student():
    data = {
        'id': 13,
        'name': 'og',
        'roll': 5
    }
    res = requests.put(f"{BASE_URL}/students/", json=data)
    print(res.json())


def delete_student():
    data = {
        'id': 3
    }
    res = requests.delete(f"{BASE_URL}/students/", json=data)
    print(res.json())


# ------------------ Run ------------------
# get_student_details()
# get_student_details(4)
# add_student()
# update_student()
delete_student()

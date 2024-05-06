import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://face-attendace-realtime-default-rtdb.firebaseio.com/",
})

reference = db.reference("Students")

data = {
    "B21110106075": {
        "name": "Sheikh Ubaid Ullah",
        "major": "Software",
        "starting_year": 2022,
        "total_attendance": 10,
        "standing": "A+",
        "last_attendance_time": "2024-5-1 10:10:10",
        "year": 3
    },
    "B21110106099": {
        "name": "Elon Musk",
        "major": "Rocket Science",
        "starting_year": 2020,
        "total_attendance": 7,
        "standing": "B",
        "last_attendance_time": "2024-5-1 10:10:10",
        "year": 4
    },
    "B21110106098": {
        "name": "Emily Blunt",
        "major": "Film Making",
        "starting_year": 2021,
        "total_attendance": 4,
        "standing": "C",
        "last_attendance_time": "2024-3-1 10:10:10",
        "year": 3
    },
    "B21110106097": {
        "name": "David Goggins",
        "major": "Sports",
        "starting_year": 2017,
        "total_attendance": 0,
        "standing": "A",
        "last_attendance_time": "2024-1-1 10:10:10",
        "year": 5
    }

}

for key, value in data.items():
    reference.child(key).set(value)
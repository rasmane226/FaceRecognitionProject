import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendacerealtime-1a839-default-rtdb.firebaseio.com/"
})
ref = db.reference('Students')

data = {

    "7000":
        {
            "name": "Rasmane Yameogo",
            "major": "Computer Computer",
            "starting_year": 2020,
            "total_attendance": 0,
            "standing": "B",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "6000":
        {
            "name": "Adel Alsmail",
            "major": "Computer Computer",
            "starting_year": 2020,
            "total_attendance": 0,
            "standing": "B",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "5000":
        {
            "name": "Uğur Erkan",
            "major": "PhD (Computer Science)",
            "starting_year": 1996,
            "total_attendance": 0,
            "standing": "G",
            "year": 6,
            "last_attendance_time": "2022-12-11 00:54:34"
        },

    "852741":
        {
            "name": "Emly Blunt",
            "major": "Economics",
            "starting_year": 2021,
            "total_attendance": 12,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "963852":
        {
            "name": "Elon Musk",
            "major": "Technology entrepreneur, investor, and engineer",
            "starting_year": 1990,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        }
}
for key, value in data.items():
    ref.child(key).set(value)
courses = [
  {
    "course_code": "CS101",
    "room_number": "3004",
    "instructor": "Haynes",
    "meeting_time": "8:00 a.m."
  },
  {
    "course_code": "CS102",
    "room_number": "4501",
    "instructor": "Alvarado",
    "meeting_time": "9:00 a.m."
  },
  {
    "course_code": "CS103",
    "room_number": "6755",
    "instructor": "Rich",
    "meeting_time": "10:00 a.m."
  },
  {
    "course_code": "NT110",
    "room_number": "1244",
    "instructor": "Burke",
    "meeting_time": "11:00 a.m."
  },
  {
    "course_code": "COM241",
    "room_number": "1411",
    "instructor": "Lee",
    "meeting_time": "1:00 p.m."
  }
]

def main():
  while True:
    course_code = input("Enter a course code (or blank to quit)\n>")
    if not course_code:
      break
    for course in courses:
      if course["course_code"] == course_code:
        print("Room Number: " + course["room_number"])
        print("Instructor: " + course["instructor"])
        print("Meeting Time: " + course["meeting_time"])
        break
    else:
      print("Course not found.")

main()
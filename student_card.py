student_data : dict ={}

for i in range(1,6):
  student_name : str = input("enter the student name:")
  student_roll_no : int = int(input("enter the roll no:"))
  student_data[student_name]={
      "roll_no":student_roll_no,
      "marks":[],
      "total":(),
      "average":(),
      "grade":()

  }
  for j in range(1,6):
    student_marks : int = int(input(f"enter the marks subject {j}:"))
    student_data[student_name]["marks"].append(student_marks)

  total = sum(student_data[student_name]["marks"])
  student_data[student_name]["total"] = total

  average = total/len(student_data[student_name]["marks"])
  student_data[student_name]["average"] = average

  if average >= 90:
    grade3 = "A"
  elif average >= 80:
    grade = "B"
  elif average >= 70:
    grade = "B"
  elif average >= 60:
    grade = "C"
  elif average <= 50:
    grade = "F"

  student_data[student_name]["grade"] = grade

user_want_student_result = input("enter the student name you want to see result:")
if user_want_student_result in student_data:
  student_info = student_data[user_want_student_result]
  print("Roll Number:", student_info["roll_no"])
  print("Marks:", student_info["marks"])
  print("Total:", student_info["total"])
  print("Average:", student_info["average"])
  print("Grade:", student_info["grade"])
else:
  print("student not found")

from django.shortcuts import render, redirect

from .models import Student, Attendance

# Create your views here.

def student_home(request):

    students_data = Student.objects.all()

    attendance = Attendance.objects.all()

#students_data is a list of all the students in the database, we are passing this list 
    data = {
        "students_data": students_data,
        "attendance": attendance
    }

    return render(request, "students/student_home.html", data)


def add_student(request):


    if request.method == "POST":
        student_name = request.POST.get("input_name")
        student_email = request.POST.get("input_email")
        student_phone_number = request.POST.get("input_phone_number")

        Student.objects.create(
            name = student_name,
            email = student_email,
            phone_number = student_phone_number
        )

        return redirect("student_home")

    return render(request, "students/add_student.html")

def delete_student(request, student_id):

    my_student = Student.objects.get(id = student_id)

    my_student.delete()

    return redirect("student_home")

def update_student(request, student_id):

    student = Student.objects.get(id = student_id)

    if request.method == "POST":
        student.name = request.POST.get("name")
        student.email = request.POST.get("email")
        student.phone_number = request.POST.get("phone")
        
        student.save()

        return redirect("student_home")

    parameters = {
        "student": student
    }

    return render(request, "students/update_student.html", parameters)

# this is a line 
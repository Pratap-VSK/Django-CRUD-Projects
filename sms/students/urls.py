from django.urls import path
from . import views

urlpatterns = [
   path("", views.student_home, name="student_home"),
   path("add-student", views.add_student, name="add_student"),

   path("update_student/<int:student_id>", views.update_student, name="update_student"),

   path("delete_student/<int:student_id>", views.delete_student, name="delete_student")
]
"""
URL configuration for facerecognition project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',views.login),
    path('login_post/',views.login_post),
    path('changepassword/',views.changepassword),
    path('changepasswod_post/',views.changepassword_post),
    path('stdchangepassword/',views.stdchangepassword),
    path('stdchangepasswod_post/',views.stdchangepassword_post),
    path('adddepartment/',views.adddepartment),
    path('adddepartment_post/',views.adddepartment_post),
    path('viewdepartment/',views.viewdepartment),
    path('viewdepartment_post/',views.viewdepartment_post),
    path('editdepartment/<id>',views.editdepartment),
    path('editepartment_post/',views.editdepartment_post),
    path('addcourse/',views.addcourse),
    path('addcourse_post/',views.addcourse_post),
    path('viewcourse/',views.viewcourse),
    path('viewcourse_post/', views.viewcourse_post),

    path('editcourse/<id>',views.editcourse),
    path('editcourse_post/',views.editcourse_post),
    path('addsubject/',views.addsubject),
    path('addsubject_post/',views.addsubject_post),
    path('viewsubject/',views.viewsubject),
    path('viewsubject_post/', views.viewsubject_post),
    path('editsubject/<id>',views.editsubject),
    path('editsubject_post/',views.editsubject_post),
    path('addstudent/',views.addstudent),
    path('addstudent_post/',views.addstudent_post),
    path('viewstudent/',views.viewstudent),
    path('viewstudent_post/', views.viewstudent_post),
    path('editstudent/<id>',views.editstudent),
    path('editstudent_post/', views.editstudent_post),
    path('addtimetable/',views.addtimetable),
    path('addtimetable_post/',views.addtimetable_post),
    path('viewtimetable/',views.viewtimetable),
    path('viewtimetable_post/', views.viewtimetable_post),

    path('edittimetable/<id>',views.edittimetable),
    path('edittimetable_post/', views.edittimetable_post),
    path('attendancereport/',views.attendancereport),
    path('adminhome/',views.adminhome),
    path('deletedepartment/<id>',views.deletedepartment),
    path('deletecourse/<id>',views.deletecourse),
    path('deletesubject/<id>',views.deletesubject),
    path('deletestudent/<id>',views.deletestudent),
    path('deletetimetable/<id>',views.deletetimetable),
    path('studenthome/',views.studenthome),
    path('viewprofile/',views.viewprofile),
    path('stdattendancereport/',views.stdattendancereport),
    path('searchbyphoto/', views.searchbyphoto),
    path('searchbyphoto_post_month/', views.searchbyphoto_post_month),
    path('searchbyphoto_post_date/', views.searchbyphoto_post_date),



    path('sadm_view_timetable/', views.sadm_view_timetable),
    path('sadm_view_timetable_post/', views.sadm_view_timetable_post),
    path('sadm_view_timetable_post1/', views.sadm_view_timetable_post1),


    path('view_attendence/', views.view_attendence),
    path('view_attendence_post/', views.view_attendence_post),
    path('gettotalsembycourseid/<courseid>', views.gettotalsembycourseid),




]

from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('homeclick', views.homeclick, name = 'homeclick'),
    
    #path('adminclick', views.adminclick, name = 'adminclick'),
    #path('teacherclick', views.teacherclick, name = 'teacherclick'),
    #path('parentclick', views.parentclick, name = 'parentclick'),

    path('adminsignup', views.adminsignup, name = 'adminsignup'),
    path('adminlogin', views.adminlogin, name = 'adminlogin'),
    path('adminlogout', views.adminlogout, name = 'adminlogout'),

    path('teachersignup', views.teachersignup, name = 'teachersignup'),
    path('teacherlogin', views.teacherlogin, name = 'teacherlogin'),
    path('teacher_wait_approval/<str:first_name>/', views.teacher_wait_approval, name = 'teacher_wait_approval'),
    path('teacherlogout', views.teacherlogout, name = 'teacherlogout'),

    path('parentsignup', views.parentsignup, name = 'parentsignup'),
    path('parentlogin', views.parentlogin, name = 'parentlogin'),
    path('parent_wait_approval/<str:parent_first_name>/', views.parent_wait_approval, name = 'parent_wait_approval'),
    path('parentlogout', views.parentlogout, name = 'parentlogout'),

    path('aboutus', views.aboutus, name = 'aboutus'),
    path('contactus', views.contactus, name = 'contactus'),


    path('adminbase', views.adminbase, name = 'adminbase'),
    path('admin_dashboard', views.admin_dashboard, name = 'admin_dashboard'),
    path('admin_teacher', views.admin_teacher, name = 'admin_teacher'),
    path('admin_student', views.admin_student, name = 'admin_student'),
    path('admin_attendance', views.admin_attendance, name = 'admin_attendance'),
    path('admin_fee', views.admin_fee, name = 'admin_fee'),
    path('admin_notice', views.admin_notice, name = 'admin_notice'),
    path('admin_change_password', views.admin_change_password, name = 'admin_change_password'),
    
    path('admin_view_attendance/<str:student_class>/', views.admin_view_attendance, name = 'admin_view_attendance'),
    path('admin_view_fee', views.admin_view_fee, name = 'admin_view_fee'),
    path('admin_view_teacher', views.admin_view_teacher, name = 'admin_view_teacher'),
    path('admin_add_teacher', views.admin_add_teacher, name = 'admin_add_teacher'),
    path('delete_teacher/<str:username>/', views.delete_teacher, name = 'delete_teacher'),
    path('update_teacher/<str:username>/', views.update_teacher, name = 'update_teacher'),
    path('admin_approve_teacher', views.admin_approve_teacher, name = 'admin_approve_teacher'),
    path('approve_pending_teacher/<str:username>/', views.approve_pending_teacher, name = 'approve_pending_teacher'),
    path('delete_pending_teacher/<str:username>/', views.delete_pending_teacher, name = 'delete_pending_teacher'),
    path('admin_view_student', views.admin_view_student, name = 'admin_view_student'),
    path('admin_add_student', views.admin_add_student, name = 'admin_add_student'),
    path('update_student/<str:username>/', views.update_student, name = 'update_student'),
    path('delete_student/<str:username>/', views.delete_student, name = 'delete_student'),
    path('admin_approve_student', views.admin_approve_student, name = 'admin_approve_student'),
    path('approve_pending_student/<str:parent_username>/', views.approve_pending_student, name = 'approve_pending_student'),
    path('delete_pending_student/<str:parent_username>/', views.delete_pending_student, name = 'delete_pending_student'),
    path('admin_view_student_fee', views.admin_view_student_fee, name = 'admin_view_student_fee'),
    path('admin_view_fee/<str:student_class>/', views.admin_view_fee, name = 'admin_view_fee'),


    path('teacherbase', views.teacherbase, name = 'teacherbase'),
    path('teacher_dashboard', views.teacher_dashboard, name = 'teacher_dashboard'),
    path('teacher_attendance', views.teacher_attendance, name = 'teacher_attendance'),
    path('teacher_notice', views.teacher_notice, name = 'teacher_notice'),
    path('teacher_take_attendance/<str:student_class>/', views.teacher_take_attendance, name = 'teacher_take_attendance'),
    path('teacher_view_attendance/<str:student_class>/', views.teacher_view_attendance, name = 'teacher_view_attendance'),
    path('teacher_results', views.teacher_results, name = 'teacher_results'),
    path('teacher_post_results/<str:student_class>/', views.teacher_post_results, name = 'teacher_post_results'),
    path('teacher_view_results/<str:student_class>/', views.teacher_view_results, name = 'teacher_view_results'),
    path('teacher_change_password', views.teacher_change_password, name = 'teacher_change_password'),

    path('parentbase', views.parentbase, name = 'parentbase'),
    path('parent_dashboard', views.parent_dashboard, name = 'parent_dashboard'),
    path('parent_view_attendance', views.parent_view_attendance, name = 'parent_view_attendance'),
    path('parent_view_result', views.parent_view_result, name = 'parent_view_result'),
    path('parent_notice', views.parent_notice, name = 'parent_notice'),
    path('parent_change_password', views.parent_change_password, name = 'parent_change_password'),
    
    path('student_clearance', views.student_clearance, name = 'student_clearance'),

    
    ]
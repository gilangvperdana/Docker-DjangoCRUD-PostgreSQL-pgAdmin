from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.student_form,name='student_insert'), #GET AND POST REQ. FOR INSERT OPERATION
    path('<int:id>/', views.student_form,name='student_update'), #GET AND POST REQ. FOR UPDATE OPERATION
    path('delete/<int:id>',views.student_delete,name='student_delete'), #DELETE
    path('list/', views.student_list,name='student_list'), #GET REQ. TO RETRIEVE AND DISPLAY ALL RECORDS
]
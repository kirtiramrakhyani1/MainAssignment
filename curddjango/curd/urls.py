#from django.conf.urls import urls

from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    #path('store',views.store, name='store'),
    path('projectList',views.projectList , name ='projectList'),
    path('empList', views.empList , name='empList'),
    path('issuesList',views.issuesList,name ='issuesList'),
	path('projectDetail/<str:pk>',views.projectDetail,name='projectDetail'),
    path('empDetail/<str:pk>',views.empDetail , name='empDetail'),
    path('issuesDetail/<str:pk>', views.issuesDetail , name = 'issuesDetail'),
    path('addProject',views.addProject,name='addProject'),
    path('addEmp',views.addEmp,name='addEmp'),
    path('addIssues',views.addIssue, name='addIssues'),
	path('updateProject/<str:pk>',views.updateProject, name='updateProject'),
    path('updateEmp/<str:pk>',views.updateEmp,name='updateEmp'),
    path('updateIssue/<str:pk>', views.updateIssue , name = 'updateIssue'),
	path('deleteProject/<str:pk>', views.deleteProject , name ='deleteProject'),
    path('deleteEmp/<str:pk>', views.deleteEmp , name = 'deleteEmp'),
    path('deleteIssue/<str:pk>', views.deleteIssue, name ="deleteIssue"),
]

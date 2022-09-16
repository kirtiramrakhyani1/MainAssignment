#from django.shortcuts import render
#from email.message import _PayloadType
from django.shortcuts import render, redirect
from .models import Emp, Issues, Project
from django.contrib import messages
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializer import EmpSerializer , ProjectSerializer , IssuesSerializer
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def index(request):
    api_urls = {
		'Project List':'/projectList/',
        'Employee List':'/empList/',
        'Issues List':'/issuesList/',
		'Project View':'/projectDetail/<str:pk>/',
        'Employee View':'/empDetail/<str:pk>/',
        'Issues View':'/issuesDetail/<str:pk>/',
		'Add Project':'/addProject/',
        'Add Emp':'/addEmp/',
        'Add Issue':'/addIssues/',
		'Update Project':'/updateProject/<str:pk>/',
        'Update Emp':'/updateEmp/<str:pk>/',
        'Update Issue':'/updateIssue/<str:pk>/',
		'Delete Project':'/deleteProject/<str:pk>/',
        'Delete Emp':'/deleteEmp/<str:pk>/',
        'Delete Issue':'/deleteIssues/<str:pk>/',
		}
    return Response(api_urls)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addEmp(request):
    payload = request.data
    serializer = EmpSerializer(data = payload)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status= status.HTTP_201_CREATED)
    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def projectList(request):
	tasks = Project.objects.all().order_by('-id')
	serializer = ProjectSerializer(tasks, many=True)
	return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def empList(request):
	tasks = Emp.objects.all().order_by('-id')
	serializer = EmpSerializer(tasks, many=True)
	return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def issuesList(request):
	tasks = Issues.objects.all().order_by('-id')
	serializer = ProjectSerializer(tasks, many=True)
	return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def empDetail(request, pk):
	tasks = Emp.objects.get(id=pk)
	serializer = EmpSerializer(tasks, many=False)
	return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def projectDetail(request, pk):
	tasks = Project.objects.get(id=pk)
	serializer = ProjectSerializer(tasks, many=False)
	return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def issuesDetail(request, pk):
	tasks = Issues.objects.get(id=pk)
	serializer = IssuesSerializer(tasks, many=False)
	return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addProject(request):
	serializer = ProjectSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

# @api_view(['POST'])
# def addEmp(request):
# 	serializer = EmpSerializer(data=request.data)
# 	if serializer.is_valid():
# 		serializer.save()
# 	return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addProject(request):
    payload = request.data
    serializer = ProjectSerializer(data = payload)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status= status.HTTP_201_CREATED)
    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addIssue(request):
    payload = request.data
    serializer = IssuesSerializer(data = payload)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status= status.HTTP_201_CREATED)
    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


# @api_view(['POST'])
# def addIssue(request):
# 	serializer = IssuesSerializer(data=request.data)
# 	if serializer.is_valid():
# 		serializer.save()
# 	return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def updateProject(request, pk):
	task = Project.objects.get(id=pk)
	serializer = ProjectSerializer(instance=task, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def updateEmp(request, pk):
	task = Emp.objects.get(id=pk)
	serializer = EmpSerializer(instance=task, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def updateIssue(request, pk):
	task = Issues.objects.get(id=pk)
	serializer = IssuesSerializer(instance=task, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteProject(request, pk):
	task = Project.objects.get(id=pk)
	task.delete()

	return Response('Item succsesfully delete!')

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteEmp(request, pk):
	task = Emp.objects.get(id=pk)
	task.delete()

	return Response('Item succsesfully delete!')

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteIssue(request, pk):
	task = Issues.objects.get(id=pk)
	task.delete()

	return Response('Item succsesfully delete!')
from django.shortcuts import render, render_to_response
#from django.core.urlresolvers import reverse
from django.http import HttpResponse#, HttpResponseRedirect
#from ProjectsApp.models import tasks, projects
#import datetime

def create_project(request):
	return render_to_response('addProject.html')

def create_task(request):
	return render_to_response('newTask.html')

def projects(request):
	return render_to_response('projects.html')

def tasks(request):
	return render_to_response('tasks.html')




#def allProjects(request):
	#array_Project = projects.objects.all()
	#return render(request, 'projects.html', {'array_Project':array_Project})

#def task(request):
	#array_Project = projects.objects.all()
	#array_task = tasks.objects.all()
	#return render(request, 'tasks.html',{'array_task':array_task})

#def formProject(request):
	#return render(request,"addProject.html")

#def newProject(request):
	#project= projects(name=request.POST['addProject'],begin = datetime.date.today(), active=True)
	#project.save()
	#return HttpResponseRedirect(reverse('ProjectManagement:Projects'))

#def formTask(request):
	#return render(request,"newTask.html")

#def newTask(request):
	#task= tasks(name=request.POST['addTask'],begin = datetime.date.today(), active=True)
	#tasks.save()
	#return HttpResponseRedirect(reverse('ProjectManagement:Task'))

#def completeProject(request, id):
	#project = get_object_or_404(projects, pk=id)
	#project.completed = True
	#project.save()
	#return HttpResponseRedirect(reverse('ProjectManagement:projectsInProgress'))

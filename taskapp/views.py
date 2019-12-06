from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm


def addtask(request):

	if request.method == 'POST':
		form = ListForm(request.POST or None)

		if form.is_valid():
			form.save()
			tasklist = List.objects.all

		return render(request, 'addtask.html', {'tasklist': tasklist})

	else:
		tasklist = List.objects.all
		return render(request, 'addtask.html', {'tasklist': tasklist})
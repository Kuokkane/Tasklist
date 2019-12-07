from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.http import HttpResponseRedirect

#ottaa käyttäjän syötteen ja tallentaa sen tietokantaan
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

#poistaa tehtävän 
def delete(request, list_id):
    task = List.objects.get(pk=list_id)
    task.delete()

    return redirect('addtask')
#yliviivaa tehtävän, vaihtaa boolean-arvon Trueksi (default false) ja tallentaa tietokantaan
def mark_as_done(request, list_id):
    task = List.objects.get(pk=list_id)
    task.completed = True
    task.save()
    return redirect('addtask')
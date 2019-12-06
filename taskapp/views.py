from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.http import HttpResponseRedirect

#ottaa käyttäjän syötteen ja tallentaa sen tietokantaan ja listaa kaikki tehtävät
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

def delete(request, list_id):
    task = List.objects.get(pk=list_id)
    task.delete()

    return redirect('addtask')
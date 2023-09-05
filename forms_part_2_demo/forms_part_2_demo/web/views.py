from django.http import HttpResponse
from django.shortcuts import render

from forms_part_2_demo.web.forms import TodoCreateForm


def index(request):
    if request.method == 'GET':
        form = TodoCreateForm()
    else:
        form = TodoCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse('All is valid')

    context = {
        'form': form,
    }

    return render(request, 'index.html', context)

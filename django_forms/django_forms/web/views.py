from django import forms
from django.shortcuts import render


# Create your views here.


class NameForm(forms.Form):
    your_name = forms.CharField(
        max_length=30,
    )


def index(request):
    name = None
    if request.method == 'GET':
        form = NameForm
        pass
    else: # request.method == post:
        form = NameForm(request.POST)
        form.is_valid()
        name = form.cleaned_data['your_name']
        pass

    context = {
        'form': form,
        'name':name,

    }
    return render(request, 'index.html', context)

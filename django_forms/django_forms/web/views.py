from django import forms
from django.shortcuts import render

from django_forms.web.forms import PersonForm
from django_forms.web.models import Person


# Create your views here.


def index_form(request):
    name = None
    if request.method == 'GET':
        form = PersonForm
        pass
    else:  # request.method == post:
        form = PersonForm(request.POST)

        form.is_valid()
        name = form.cleaned_data['your_name']
        Person.objects.create(
            name=name,
        )

    context = {
        'form': form,
        'name': name,

    }
    return render(request, 'index.html', context)


class PersonCreateForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'  # or
        # fields =('name','age' ..etc) includes only the following
        # exclude = ('pets',) excludes only the following
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }
    help_text = {
        'name':'Your name',
    }
    labels = {
        'age':"THE AGE",
    }

def index_model_form(request):
    instance = Person.objects.get(pk=1)
    if request.method == 'GET':
        form = PersonCreateForm(instance=instance)
    else:
        form = PersonCreateForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()  # same as bellow
            # pets = form.cleaned_data.pop('pets')
            # person = Person.objects.create(
            #     **form.cleaned_data
            # )
            # person.pets.set(pets)
            # person.save()

    context = {
        'form': form,
    }
    return render(request, 'model_forms.html',
                  context)

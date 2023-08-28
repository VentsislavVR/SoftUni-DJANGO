from random import choice

from django.http import HttpResponse, HttpRequest, HttpResponseNotFound, HttpResponseBadRequest, Http404
from django.shortcuts import render, redirect


# Create your views here.
# wirhout render
# def show_departments(request, *args, **kwargs):
#     print(request.GET)
#     print(request.method)
#     print(request.POST)
#     print(request.get_port())
#     print(request.get_host())
#     print(request.headers)
#     order_by = request.GET.get('order_by','name')
#     body = f'path:{request.path}args={args},kwargs={kwargs},order_by:{order_by}'
#     return HttpResponse(body)

def show_departments(request, *args, **kwargs):
    context = {
        'page_title': 'Departments',
        'request': request.method,
        'order_by': request.GET.get('order_by', 'name'),

    }
    return render(request, 'departments/all.html', context)


def show_departments_details(request, department_id):
    body = f'path:{request.path},id: {department_id}'
    return HttpResponse(body)


def redirect_to_first_department(request):
    possible_order_by = ['name', "age", "id"]
    order_by = choice(possible_order_by)

    # to = f'/departments/?order_by={order_by}'
    # to = 'https://softuni.bg'

    return redirect('show department details', department_id=13)


def show_not_found(request):
    # status_code = 404
    # if status_code == 404:
        # return HttpResponseNotFound('This is not found!')
    # return HttpResponse("Error",status=status_code)
    get_object_or_404()

    raise Http404('Not found')




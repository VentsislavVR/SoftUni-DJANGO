from django.template import Library

from templates_demo.web.views import Student

register = Library()


@register.simple_tag(name='student_info')
def show_student_info(student: Student):
    return (f'Hello, My name is {student.name} '
            f'and I am {student.age}- years old.')


@register.simple_tag(name='sample_tag')
def sample_tag(*args, **kwargs):
    return ', '.join(str(x) for x in (list(args) + list(kwargs.items())))


@register.inclusion_tag('tags/nav.html', name='app_nav')
def generate_nav(*args):
    context = {
        'url_names': args,

    }
    return context

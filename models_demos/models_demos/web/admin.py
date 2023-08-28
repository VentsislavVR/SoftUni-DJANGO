from django.contrib import admin

from models_demos.web.models import Employee


# Register your models here.
# the Employeee model is enabled in django admin
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass

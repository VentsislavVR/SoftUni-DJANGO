from django.db import models


# Model fields == class attributes in Model classes
# Create your models here.


''''
PostgreSQL : varying char (30)
SQL Server : VARCHAR(30)
Other: CHARVAR(30) //demo

PostgreSQL : decimal
SQL Server: money
ko napraih e 
'''



class Employee(models.Model):
    first_name = models.CharField(
        max_length=30,
    )
    years_of_experience = models.PositiveIntegerField()
    # text with unlimited length
    review = models.TextField()

    start_date = models.DateTimeField()


    # automatically set on creation
    created_on = models.DateTimeField(
        auto_now_add=True, # optional
    )
    # automatically set on each save/update
    updated_on = models.DateTimeField(
        auto_now=True,  # optional
    )



'''
        Django-ORM 
(Object-Relational-Mapping

'''

from django.db import models


# Model fields == class attributes in Model classes
# Create your models here.


''''
PostgreSQL : varying char (30)
SQL Server : VARCHAR(30)
Other: CHARVAR(30) //demo

PostgreSQL : decimal
SQL Server: money
'''



class Employee(models.Model):
    first_name = models.CharField(
        max_length=30,
    )
    last_name = models.CharField(
        max_length=50,
        null=True
    )

    level = models.CharField(
        max_length=15,
    )
    age = models.IntegerField()

    years_of_experience = models.PositiveIntegerField()
    # text with unlimited length
    review = models.TextField()

    start_date = models.DateTimeField()
    email = models.EmailField(
        null=True
    )


    # automatically set on creation
    created_on = models.DateTimeField(
        auto_now_add=True, # optional
    )
    # automatically set on each save/update
    updated_on = models.DateTimeField(
        auto_now=True,  # optional

    )
    @property
    def fullname(self):
        return  f'{self.first_name} {self.last_name}'
    def __str__(self):
        return f'Id: {self.pk};Name: {self.fullname}'



'''
        Django-ORM 
(Object-Relational-Mapping
'''
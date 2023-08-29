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


class Department(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return f'Id: {self.pk}; Name: {self.name}'


class Project(models.Model):
    name = models.CharField(
        max_length=30
    )
    code_name = models.CharField(
        max_length=10,
        unique=True,
    )
    deadline = models.DateField(

    )

    # additional info


class Employee(models.Model):
    LEVEL_JUNIOR = 'Junior'
    LEVEL_REGULAR = 'Regular'
    LEVEL_SENIOR = 'Senior'

    LEVELS = (
        (LEVEL_JUNIOR, LEVEL_JUNIOR),
        (LEVEL_REGULAR, LEVEL_REGULAR),
        (LEVEL_SENIOR, LEVEL_SENIOR),
    )
    first_name = models.CharField(
        max_length=30,
    )
    last_name = models.CharField(
        max_length=50,
        null=True
    )

    level = models.CharField(
        verbose_name='Seniority level',
        max_length=15,
        choices=(
            LEVELS
            # ('jr','Junior'),
            # ('reg','Regular'),
            # ('sr','Senior')
        )
    )
    age = models.IntegerField(
        default=-1,
    )

    years_of_experience = models.PositiveIntegerField()
    # text with unlimited length
    review = models.TextField()

    start_date = models.DateTimeField()
    email = models.EmailField(
        unique=True,
        editable=True,
    )

    is_full_time = models.BooleanField(
        null=True
    )

    # automatically set on creation
    created_on = models.DateTimeField(
        auto_now_add=True,  # optional
    )
    # automatically set on each save/update
    updated_on = models.DateTimeField(
        auto_now=True,  # optional

    )
    # One-to-many
    department = models.ForeignKey(
        Department,
        on_delete=models.RESTRICT,

    )
    # Many-to-many
    projects = models.ManyToManyField(
        Project,
        related_name='employees',
    )

    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'Id: {self.pk};Name: {self.fullname}'


class AccessCard(models.Model):
    employee = models.OneToOneField(
        Employee,
        on_delete=models.CASCADE,
        primary_key=True
    )


class Category(models.Model):
    name = models.CharField(
        max_length=15
    )

    parent_category = models.ForeignKey(
        'Category',
        on_delete=models.RESTRICT,
        null=True,
        blank=True,

    )


'''

        Django-ORM 
(Object-Relational-Mapping
'''


class EmployeesProjects(models.Model):
    employee_id = models.ForeignKey(
        Employee,
        on_delete=models.RESTRICT)
    project_id = models.ForeignKey(
        Project,
        on_delete=models.RESTRICT)

    date_joined = models.DateField(
        auto_now_add=True
    )


class NullBlankDemo(models.Model):
    blank = models.IntegerField(
        blank=True,
        null=False,
    )

    null = models.IntegerField(
        blank=False,
        null=True,
    )

    blank_null = models.IntegerField(
        blank=True,
        null=True
    )

    default = models.IntegerField(
        blank=False,
        null=False,
    )

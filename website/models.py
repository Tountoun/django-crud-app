from django.db import models


class Employee(models.Model):
    class Domain(models.TextChoices):
        HUMAN_RESOURCES = "HR"
        INFORMATION_TECHNOLOGY = "IT"
        MARKETING = "MR"
        ACCOUNTING = "AC"

    first_name = models.CharField(max_length=40, db_column="first name")
    last_name = models.CharField(max_length=40, db_column="last name")
    email = models.EmailField(db_column="email")
    title = models.CharField(max_length=40, db_column="title")
    domain = models.CharField(max_length=22, choices=Domain.choices, db_column="domaine", default=Domain.INFORMATION_TECHNOLOGY)
    salary = models.DecimalField(max_digits=10, decimal_places=3, db_column="salary")

    class Meta:
        db_table = "employees"

    """
        class DomainEmp(models.TextChoices):
            HUMAN_RESOURCES = "HR"
            INFORMATION_TECHNOLOGY = "IT"
            MARKETING = "MR"
            ACCOUNTING = "AC"
    """


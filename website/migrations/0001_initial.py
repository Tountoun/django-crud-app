# Generated by Django 4.1.7 on 2023-04-11 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(db_column='first name', max_length=40)),
                ('last_name', models.CharField(db_column='last name', max_length=40)),
                ('email', models.EmailField(db_column='email', max_length=254)),
                ('title', models.CharField(db_column='title', max_length=40)),
                ('domain', models.CharField(choices=[('HR', 'Human Resources'), ('IT', 'Information Technology'), ('MR', 'Marketing'), ('AC', 'Accounting')], db_column='domaine', default='IT', max_length=22)),
                ('salary', models.DecimalField(db_column='salary', decimal_places=3, max_digits=10)),
            ],
            options={
                'db_table': 'employees',
            },
        ),
    ]
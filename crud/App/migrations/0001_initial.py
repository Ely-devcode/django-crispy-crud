# Generated by Django 4.0.4 on 2022-06-04 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('M', 'M'), ('F', 'F')], max_length=1, null=True)),
                ('career', models.CharField(choices=[('Frontend', 'Frontend'), ('Backend', 'Backend'), ('Fulstack', 'Fulstack'), ('Intern', 'Intern')], max_length=50, null=True)),
            ],
        ),
    ]

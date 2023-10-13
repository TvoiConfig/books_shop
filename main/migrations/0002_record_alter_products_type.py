# Generated by Django 4.2.6 on 2023-10-13 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='ФИО')),
                ('number', models.CharField(max_length=150, verbose_name='Номер телефона')),
                ('message', models.CharField(max_length=200, verbose_name='Сообщение')),
            ],
            options={
                'verbose_name': 'запись',
                'verbose_name_plural': 'Записи',
                'db_table': 'record',
            },
        ),
        migrations.AlterField(
            model_name='products',
            name='type',
            field=models.CharField(choices=[('book', 'Книга'), ('magazine', 'Журнал')], default='book', max_length=50, verbose_name='Тип'),
        ),
    ]

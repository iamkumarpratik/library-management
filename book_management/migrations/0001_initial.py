# Generated by Django 4.0.6 on 2022-07-16 11:40

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.UUIDField(auto_created=True, primary_key=True, serialize=False)),
                ('created_on', models.DateField(default=datetime.datetime.now)),
                ('created_by', models.CharField(max_length=255)),
                ('modified_on', models.DateField(default=datetime.datetime.now)),
                ('modified_by', models.CharField(max_length=255)),
                ('book_name', models.CharField(db_index=True, max_length=255)),
                ('author', models.CharField(db_index=True, max_length=255)),
                ('quantity', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Credentials',
            fields=[
                ('id', models.UUIDField(auto_created=True, primary_key=True, serialize=False)),
                ('created_on', models.DateField(default=datetime.datetime.now)),
                ('created_by', models.CharField(max_length=255)),
                ('modified_on', models.DateField(default=datetime.datetime.now)),
                ('modified_by', models.CharField(max_length=255)),
                ('username', models.CharField(db_index=True, max_length=255)),
                ('password', models.CharField(max_length=512)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.UUIDField(auto_created=True, primary_key=True, serialize=False)),
                ('created_on', models.DateField(default=datetime.datetime.now)),
                ('created_by', models.CharField(max_length=255)),
                ('modified_on', models.DateField(default=datetime.datetime.now)),
                ('modified_by', models.CharField(max_length=255)),
                ('fullname', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('status', models.BooleanField()),
                ('role', models.CharField(db_index=True, max_length=255)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='book_management.credentials')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LendingLog',
            fields=[
                ('id', models.UUIDField(auto_created=True, primary_key=True, serialize=False)),
                ('created_on', models.DateField(default=datetime.datetime.now)),
                ('created_by', models.CharField(max_length=255)),
                ('modified_on', models.DateField(default=datetime.datetime.now)),
                ('modified_by', models.CharField(max_length=255)),
                ('current_book_status', models.CharField(choices=[{'A': 'Available', 'B': 'Borrowed'}], max_length=2)),
                ('expected_return_date', models.DateField()),
                ('actual_return_date', models.DateField(default=datetime.datetime.now)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='book_management.books')),
                ('borrower_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='book_management.members')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

from django.db import models
from datetime import datetime
# Create your models here.
from django.db.models import (ForeignKey, DateField, CharField,
                              UUIDField, IntegerField, BooleanField,
                              Model)
from uuid import uuid4


class BaseModel(Model):
    id = UUIDField(default=uuid4, null=False, primary_key=True)

    class Meta:
        abstract = True


class CreateMixin(Model):
    created_on = DateField(default=datetime.now)
    created_by = CharField(max_length=255)

    class Meta:
        abstract = True


class ModifyMixin(Model):
    modified_on = DateField(default=datetime.now)
    modified_by = CharField(max_length=255)

    class Meta:
        abstract = True


class Credentials(BaseModel, CreateMixin, ModifyMixin):
    username = CharField(max_length=255, null=False, db_index=True, unique=True)
    password = CharField(max_length=512, null=False)


class Books(BaseModel, CreateMixin, ModifyMixin):
    book_name = CharField(max_length=255, db_index=True)
    author = CharField(max_length=255, db_index=True)
    quantity = IntegerField()


class Members(BaseModel, CreateMixin, ModifyMixin):
    fullname = CharField(max_length=255, null=False)
    email = CharField(max_length=255)
    username = CharField(max_length=255, null=False, db_index=True, unique=True)
    active = BooleanField(null=False)
    role = CharField(max_length=255, db_index=True)


class LendingLog(BaseModel, CreateMixin, ModifyMixin):

    status = [
        {"B": "Borrowed",
         "A": "Available"}
    ]

    book = ForeignKey(Books, on_delete=models.DO_NOTHING)
    borrower_username = CharField(max_length=255, null=False, db_index=True, unique=True)
    current_book_status = CharField(max_length=2, choices=status)
    expected_return_date = DateField()
    actual_return_date = DateField(default=datetime.now)

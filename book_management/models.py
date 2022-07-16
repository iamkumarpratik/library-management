from django.db import models

# Create your models here.
from django.db.models import (ForeignKey, DateField, CharField,
                              UUIDField, IntegerField, BooleanField,
                              Model)


class BaseModel(Model):
    id = UUIDField(auto_created=True, null=False, primary_key=True)

    class Meta:
        abstract = True


class CreateMixin(Model):
    created_on = DateField(auto_created=True)
    created_by = CharField(max_length=255)

    class Meta:
        abstract = True


class ModifyMixin(Model):
    modified_on = DateField(auto_created=True)
    modified_by = CharField(max_length=255)

    class Meta:
        abstract = True


class Books(BaseModel, CreateMixin, ModifyMixin):
    book_name = CharField(max_length=255, db_index=True)
    author = CharField(max_length=255, db_index=True)
    quantity = IntegerField()


class Members(BaseModel, CreateMixin, ModifyMixin):
    username = CharField(max_length=255, db_index=True)
    status = BooleanField()
    role = CharField(max_length=255, db_index=True)


class BorrowStatus(BaseModel, CreateMixin, ModifyMixin):

    status = [
        {"B": "Borrowed",
         "A": "Available"}
    ]

    book = ForeignKey(Books, on_delete=models.DO_NOTHING)
    borrower_name = ForeignKey(Members, on_delete=models.DO_NOTHING)
    current_book_status = CharField(max_length=2, choices=status)


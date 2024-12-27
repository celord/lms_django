from django.db import models
from lms_local.utils.models import BaseModel


class Organisation(BaseModel):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="owned_organisations",
        null=True,
    )
    admin = models.ManyToManyField(
        "users.User", related_name="admin_in_organisations", blank=True
    )
    members = models.ManyToManyField(
        "users.User", related_name="organisations", blank=True
    )
    description = models.TextField(blank=True)
    logo = models.ImageField(upload_to="organisations/logos/", blank=True)

    def all_members(self):
        return self.members.all() | self.admin.all() | [self.owner]

    def __str__(self):
        return self.name


class Airports(BaseModel):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=3)

    def __str__(self):
        return self.name

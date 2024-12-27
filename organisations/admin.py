from django.contrib import admin

from organisations.models import Organisation


# Register your models here.


@admin.register(Organisation)
class OrgaAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at"]

from pickletools import TAKEN_FROM_ARGUMENT4
from django.contrib import admin
from .models import Bill, Team
# Register your models here.
@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "amount"]

admin.site.register(Team)
from django.contrib import admin
from .models import Realtor
# Register your models here.
class RealtorAdmin(admin.ModelAdmin):
    list_display = ["id",'name',"is_mvp","email",]
    list_display_link = ["id","email"]
    list_editable = ["is_mvp"]
    search_fields = ["name",]
    list_per_page = 20

admin.site.register(Realtor)


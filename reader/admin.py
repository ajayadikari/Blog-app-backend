from django.contrib import admin
from .models import ReaderModel

class ReaderAdmin(admin.ModelAdmin):
    list_display = ["reader_name", "subscribe_limit"]

    def reader_name(self, obj):
        return obj.account.first_name + obj.account.last_name
    
admin.site.register(ReaderModel, ReaderAdmin)

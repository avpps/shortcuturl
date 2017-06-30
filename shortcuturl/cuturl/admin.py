from django.contrib import admin

from .models import userurl

class userurlAdmin(admin.ModelAdmin):
    list_display = ('id', 'url_text')

admin.site.register(userurl, userurlAdmin)

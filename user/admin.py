from django.contrib import admin

from user.models import CustomUser


@admin.register(CustomUser)
class TrackAdmin(admin.ModelAdmin):
    fields = ('groups', 'username')

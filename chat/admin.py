from django.contrib import admin
from .models import Room,Message

# Register your models here.
admin.site.register(Room)
admin.site.register(Message)

from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'role', 'college_id']
    search_fields = ['username', 'email']
    list_filter = ['role']

admin.site.register(User, UserAdmin)

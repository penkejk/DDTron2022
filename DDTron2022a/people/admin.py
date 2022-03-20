from django.contrib import admin
from .models import Group, Person
# Register your models here.


class PersonAdmin(admin.ModelAdmin):
        list_display = ['person_name', 'person_email','get_group_name', 'id']    

        def get_group_name(self, obj):
                return obj.group.group_name

class GroupAdmin(admin.ModelAdmin):
        list_display = ['group_name',  'id']    

admin.site.register(Person, PersonAdmin)
admin.site.register(Group, GroupAdmin)
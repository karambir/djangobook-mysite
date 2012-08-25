from django.contrib import admin
from mysite.colleges.models import allcollege,StudentProfile

class allcollegeAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'estd')
    search_fields = ('name', 'address', 'estd')

admin.site.register(allcollege, allcollegeAdmin)
admin.site.register(StudentProfile)

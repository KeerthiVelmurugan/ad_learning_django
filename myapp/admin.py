from django.contrib import admin
from .models import Student

# Register your models here.

class CustomStudent(admin.ModelAdmin):
    list_display = ['id','name','email','phone','age','joining_date']
    list_filter = ['age','courses','city']
    search_fields = ['name', 'email']
    ordering = ['-joining_date','age']
    date_hierarchy = 'joining_date'
    filter_horizontal = ['courses']
    list_per_page = 10
    # list_editable = ['email','name']
    list_display_links=['email']
    fields = ['name','email','age','courses','city']

admin.site.register(Student,CustomStudent)


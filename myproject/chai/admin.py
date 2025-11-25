from django.contrib import admin
from .models import Student
from .models import Emp

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'email')
    list_filter = ('age',)
    search_fields = ('name', 'email')
    ordering = ('name',)
    
# rgistering Emp model
admin.site.register(Emp)




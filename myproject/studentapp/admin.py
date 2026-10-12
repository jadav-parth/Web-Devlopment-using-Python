from django.contrib import admin
from .models import Student

# Admin Panel ને કસ્ટમાઇઝ કરવા માટે (Configuration)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'enrollment', 'department', 'semester')  # ટેબલ ફોર્મેટમાં આ કૉલમ દેખાશે
    search_fields = ('name', 'enrollment')                                # સર્ચ બાર ઉમેરવા માટે
    list_filter = ('department', 'semester')                              # સાઇડબારમાં ફિલ્ટર ઉમેરવા માટે

# મોડેલને એડમિન સાથે રજીસ્ટર કરવું
admin.site.register(Student, StudentAdmin)
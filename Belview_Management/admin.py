from django.contrib import admin

# Register your models here.
from .models import Employee
from .models import Department
from .models import Room
from .models import Location

admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(Room)
admin.site.register(Location)
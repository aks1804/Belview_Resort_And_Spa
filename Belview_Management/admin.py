from django.contrib import admin

# Register your models here.
from .models import Employee
from .models import Department
from .models import Room
from .models import Location
from .models import Guest
from .models import Event
from .models import Utility
from .models import Store
from .models import ExtEmployee

admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(Room)
admin.site.register(Location)
admin.site.register(Guest)
admin.site.register(Event)
admin.site.register(Utility)
admin.site.register(Store)
admin.site.register(ExtEmployee)

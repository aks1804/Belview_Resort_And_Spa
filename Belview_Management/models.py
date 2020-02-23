from django.db import models

class Guest(models.Model):
    reg_id = models.CharField(max_length=4)
    name = models.CharField(max_length=30)
    date_of_birth = models.DateTimeField()
    mob_no = models.CharField(max_length=15)
    email = models.EmailField(max_length=30)
    address = models.TextField(max_length=200)
    check_in_date = models.DateTimeField()
    check_out_date = models.DateTimeField()
    room_no = models.ForeignKey(Room, on_delete=models.CASCADE)

class Event(models.Model):
    event_code = models.CharField(max_length=4, primary_key = true)
    event_name = models.CharField(max_length=30)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    lname = models.ForeignKey(Department, on_delete=models.CASCADE)
    attendee = models.ManyToManyField(
        Guest, through="GuestEvent", through_fields=("guest_name", "room_no", "event_code")
    )

class Utility(models.Model):
      request_no = models.CharField(max_length=4, primary_key = true)
      utility_name = models.CharField(max_length=30)
      quantity = models.IntegerField(max_length=3)
      status = models.BooleanField()
      requested_dept =  models.ForeignKey(Department, on_delete=models.CASCADE)

class Store(models.Model):
  storeName = models.CharField(max_length=30, primary_key = true)
  last_inspection_date = models.DateTimeField()
  lname = odels.ForeignKey(Department, on_delete=models.CASCADE)


class ExtEmployee(models.Model):
  empCode = models.CharField(max_length=4, primary_key = true)
  emp_name = models.CharField(max_length=30)
  start_date = models.DateTimeField()
  last_inspection_date = models.DateTimeField()

class GuestEvent(models.Model): # Intermediate Table for M:N Relation b/w Guest and Event
    guest_name = models.OneToOneField(Guest, on_delete=models.CASCADE)
    room_no = models.OneToOneField(Guest, on_delete=models.CASCADE)
    event_code = models.ForeignKey(Event, on_delete=models.CASCADE)

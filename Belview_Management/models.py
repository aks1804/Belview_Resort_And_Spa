from django.contrib.auth.models import User
from django.db import models


class Employee(models.Model):
	ename = models.CharField(max_length=20)
	ecode = models.IntegerField(primary_key = True)
	emp_date = models.DateTimeField()
	salary = models.IntegerField()
	last_inspection_date = models.DateTimeField()
	inspected_by = models.ForeignKey("self", on_delete=models.SET_NULL, null=True)
	works_in = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True)


class Department(models.Model):
	dname = models.CharField(max_length=20)
	dcode = models.IntegerField(primary_key=True)
	number_of_employees = models.IntegerField()
	budget = models.IntegerField()
	last_inspection_date = models.DateTimeField()
	in_charge = models.ForeignKey('Employee', on_delete=models.SET_NULL, null=True)
	located_in = models.ForeignKey('Location', on_delete=models.SET_NULL, null=True)


class Room(models.Model):
	room_number = models.IntegerField()
	location = models.ForeignKey('Location', on_delete=models.SET_NULL, null=True)
	occupation_status = models.CharField(max_length=20)
	number_of_occupants = models.IntegerField()
	room_type = models.CharField(max_length=20)
	cost_per_day_peak = models.IntegerField()
	cost_per_day_non_peak = models.IntegerField()
	class Meta:
		unique_together = [["room_number", "location"]]


class Location(models.Model):
	lname = models.CharField(max_length=20)
	max_capacity = models.IntegerField()
	in_charge = models.ForeignKey('Employee', on_delete=models.SET_NULL, null=True)


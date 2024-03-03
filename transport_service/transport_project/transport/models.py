from django.db import models

# Create your models here.

class Shipment(models.Model):
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)
    vehicle = models.ForeignKey('Vehicle', on_delete=models.CASCADE, null=True, blank=True)

class Vehicle(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)
    vehicle_type = models.CharField(max_length=100, null=True, blank=True)
    registration_number = models.CharField(max_length=100, null=True, blank=True)
    # mobile number of the driver
    driver_mobile = models.CharField(max_length=15, null=True, blank=True)
    status = models.CharField(max_length=50, default='available')


# GVW	6250 kg
# Wheelbase	2815 mm
# Tipper Variants	2.8 cum FBT, CBC
# Engine	E483 4cyl 2V
# Max Power Output	70 Kw(~95 HP) @ 3200 RPM
# Max Torque Output	285 Nm @ 1440 RPM
# FIP System	Rotary Mechanical
# Emission	BSIII
# Transmission	ET 35 S5
# Gear Type	5 Speed (5 forward, 1 reverse) with hybrid GSL
# Clutch Dia	310 mm
# Gradeability (%)	42
# Steering	Tilt & telescopic power steering (vacuum assisted)
# 6 degree tilting and 30 mm telescopic movement
# Ground Clearance	210 mm
# Battery	12V - 70Ah
# Fuel Tank Capacity	60 litres
# Brakes (Service)	Hydraulic brake vacuum assisted with AWA at all wheel ends
# Suspension (Front & Rear)	Semi-elliptical laminated leaves
# Tyres	7.00 X 16 - 16PR
# Cabin	2m wide aerodynamic cabin with modern styling & PEGASUS family look
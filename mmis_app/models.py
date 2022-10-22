from django.db import models
from django.contrib.auth.models import AbstractUser


# # Create your models here.
class User(AbstractUser):
    role_choice = (
        ('admin', 'Admin'),
        ('respondent', 'Respondent')
    )

    sector_choice = (
        ('MAP', 'Mercury Added Products'),
        ('health', 'Environment & Health'),
        ('ASGM', 'Artisanal and Small Scale Gold Mining'),
        ('cement', 'Cement'),
        ('waste', 'Waste'),
        ('eAndF', 'Energy & Fuel')
    )

    gender_choice = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    role = models.CharField(max_length=10, null=True, choices=role_choice)
    sector = models.CharField(max_length=100, null=True, choices=sector_choice)
    gender = models.CharField(max_length=6, null=True, choices=gender_choice)

    def __str__(self):
        return self.username


class ContactInformation(models.Model):
    Fname = models.CharField(max_length=50, null=False, verbose_name="First Name")
    Mname = models.CharField(max_length=50, blank=True, verbose_name="Middle Name")
    Sname = models.CharField(max_length=50, null=False, verbose_name="Surname Name")
    contact = models.CharField(max_length=150, null=False, verbose_name="Organization's Name")
    ContactPhone = models.IntegerField(null=False, verbose_name="Mobile Number (Contact Person)")
    OrganizationPhone = models.IntegerField(null=False, verbose_name="Phone Number (Organization)")
    Alternate_mobile = models.IntegerField(blank=True, verbose_name="Alternate mobile number")
    Full_address = models.TextField(max_length=250, null=False, verbose_name="Organization's Address")
    email = models.EmailField(max_length=200, null=False, verbose_name="Organization's email address")
    Web_page = models.CharField(max_length=50, blank=True, verbose_name="Web address")

    def __str__(self):
        return f'{self.Sname} {self.Fname}'


class MercuryAddedProducts(models.Model):
    mercury_compound_Choice=(

        ('Mercury Product', 'Mercury Product'),
        ('Commodity Chemical', 'Commodity Chemical'),
        ('Disposed Mercury Products', 'Disposed Mercury Products'),
        ('Thermometers', 'Thermometers'),
        ('Light Fittings', 'Light Fittings'),
        ('Cosmetics', 'Cosmetics'),
        ('Batteries', 'Batteries'),
        ('Paint', 'Paint'),
        ('Polyurethane', 'Polyurethane')
    )

    map_id = models.IntegerField(primary_key=True)
    # user = models.OneToOneField(User, on_delete=models.CASCADE, default='')
    mercury_compound = models.CharField(max_length=300, null=True, choices=mercury_compound_Choice, default='')
    item = models.CharField(max_length=250)
    imported = models.CharField(max_length=200)
    consumption_or_production = models.CharField(max_length=200)
    year = models.DateField(max_length=4)
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class EnergyConsumptionAndFuelProduction(models.Model):

    energy_fuel_Choice=(

        ('Coal Combustion in Large Power Plants', 'Coal Combustion in Large Power Plants'),
        ('Other Coal Uses', 'Other Coal Uses'),
        ('Combustion/Use of Petroleum Coke and Heavy Oil', 'Combustion/Use of Petroleum Coke and Heavy Oil'),
        ('Use of Raw or Pre-cleaned Natural Gas', 'Use of Raw or Pre-cleaned Natural Gas'),
        ('Use of Pipeline Gas (Consumer quality)', 'Use of Pipeline Gas (Consumer quality)'),
        ('Biomass Fired Power & Heat Production', 'Biomass Fired Power & Heat Production'),
        ('Charcoal Combustion', 'Charcoal Combustion'),
        ('Oil Extraction', 'Oil Extraction'),
        ('Oil Refining', 'Oil Refining'),
        ('Extraction & Processing of Natural Gas', 'Extraction & Processing of Natural Gas'),
    )

    ecfp_id = models.IntegerField(primary_key=True)
    energy_fuel = models.CharField(max_length=300, null=True, choices=energy_fuel_Choice, default='')
    imported = models.CharField(max_length=200, default='')
    consumption_or_production = models.CharField(max_length=200, default='')
    year = models.DateField(max_length=4, default='')
    note = models.TextField(max_length=200, default='')
    created_at = models.DateTimeField(auto_now_add=True)


# class Cement(models.Model):
#     yes_choices = (
#         ('Yes', 'Yes'),
#         ('No', 'No'),
#     )
#     operation_cover_Choice = (
#
#         ('Cement Production', 'Cement Production'),
#         ('Cement Production/without Co-incineration of Waste', 'Cement Production/without Co-incineration of Waste'),
#         ('With no filters', 'With no filters'),
#         ('With filters and no filter dust recycling: Simple particle control (ESP / PS / FF)\
# Optimized particle control (FF+SNCR / FF+WS / ESP+FGD / optimized FF)', 'With filters an no filter dust recycling: Simple particle control (ESP / PS / FF)\
# Optimized particle control (FF+SNCR / FF+WS / ESP+FGD / optimized FF)'),
#         ('With filters and filter dust recycling *2:\
# Simple particle control (ESP / PS / FF) Optimized particle control (FF+SNCR / FF+WS / ESP+FGD / optimized FF)\
# ', 'With filters and filter dust recycling *2:\
# Simple particle control (ESP / PS / FF) Optimized particle control (FF+SNCR / FF+WS / ESP+FGD / optimized FF)\
# '),
#         ('Production of Lime', 'Production of Lime'),
#         ('Production of lime and lightweight aggregates', 'Production of lime and lightweight aggregates'),
#         ('Production of light weight aggregate using kiln', 'Production of light weight aggregate using kiln'),
#         ('Other minerals and materials', 'Other minerals and materials')
#
#     )
#
#     cem_id = models.IntegerField(primary_key=True)
#     operation_cover = models.CharField(max_length=300, null=True, choices=operation_cover_Choice, default='')
#     yes = models.CharField(max_length=3, null=True, choices=yes_choices, default='')
#     consumption_or_production = models.CharField(max_length=200, default='')
#     year = models.DateField(max_length=4, default='')
#     note = models.TextField(max_length=200, default='')
#     created_at = models.DateTimeField(auto_now_add=True)


class EnvironmentAndHealth(models.Model):
    pass


class ASGMining(models.Model):
    pass


class Waste(models.Model):
    pass


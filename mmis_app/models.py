from django.db import models
from django.contrib.auth.models import AbstractUser


# # Create your models here.
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


class User(AbstractUser):
    is_admin = models.BooleanField('Is Admin', default=False)
    is_cement = models.BooleanField('Cement Sector', default=False)
    is_health = models.BooleanField('Health Sector', default=False)
    is_waste = models.BooleanField('Waste Sector', default=False)
    is_asgm = models.BooleanField('ASGM Sector', default=False)
    is_map = models.BooleanField('MAP Sector', default=False)
    is_EandF = models.BooleanField('Energy & Fuel Sector', default=False)

    gender_choice = (
        ('M', 'Male'),
        ('F', 'Female')
    )

    gender = models.CharField(max_length=6, null=True, choices=gender_choice)
    # contact = models.ForeignKey(ContactInformation, models.OneToOneField, default='')


class MercuryAddedProducts(models.Model):
    mercury_compound_Choice = (

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
    mercury_compound = models.CharField(max_length=300, null=True, choices=mercury_compound_Choice, default='')
    item = models.CharField(max_length=250)
    imported = models.CharField(max_length=200)
    consumption_or_production = models.CharField(max_length=200)
    year = models.DateField(max_length=4)
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)


class EnergyConsumptionAndFuelProduction(models.Model):
    energy_fuel_Choice = (

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
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)


class Cement(models.Model):
    yes_choices = (
        ('Select', 'Select'),
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    operation_cover_Choice = (

        ('Cement Production', 'Cement Production'),
        ('Cement Production/without Co-incineration of Waste', 'Cement Production/without Co-incineration of Waste'),
        ('With no filters', 'With no filters'),
        ('With filters and no filter dust recycling: Simple particle control (ESP / PS / FF)\
Optimized particle control (FF+SNCR / FF+WS / ESP+FGD / optimized FF)', 'With filters an no filter dust recycling: Simple particle control (ESP / PS / FF)\
Optimized particle control (FF+SNCR / FF+WS / ESP+FGD / optimized FF)'),
        ('With filters and filter dust recycling *2:\
Simple particle control (ESP / PS / FF) Optimized particle control (FF+SNCR / FF+WS / ESP+FGD / optimized FF)\
', 'With filters and filter dust recycling *2:\
Simple particle control (ESP / PS / FF) Optimized particle control (FF+SNCR / FF+WS / ESP+FGD / optimized FF)\
'),
        ('Production of Lime', 'Production of Lime'),
        ('Production of lime and lightweight aggregates', 'Production of lime and lightweight aggregates'),
        ('Production of light weight aggregate using kiln', 'Production of light weight aggregate using kiln'),
        ('Other minerals and materials', 'Other minerals and materials')

    )

    cem_id = models.IntegerField(primary_key=True)
    operation_cover = models.CharField(max_length=300, null=True, choices=operation_cover_Choice, default='')
    yes = models.CharField(max_length=6, null=True, choices=yes_choices, default='')
    consumption_or_production = models.CharField(max_length=200, default='')
    year = models.DateField(max_length=4, default='')
    note = models.TextField(max_length=200, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)


# class EnvironmentAndHealth(models.Model):
#     option1 = (("z)", "select"), ("a)", "Domestic"), ("b)", "Hazardous/Industrial"), ("d)", "Not applicable"))
#     option2 = (("z)", "select"), ("a)", "Daily (Kg)"), ("b)", "Weekly (Kg)"), ("c)", "Monthly (Kg)"), ("d)", "Yearly "
#                                                                                                              "(Kg)"))
#     option3 = (("z)", "select"), ("a)", "Yes"), ("b)", "No"))
#     option4 = (("z)", "select"), ("a)", "Yes"), ("b)", "No"),)
#     option5 = (("z)", "select"), ("a)", "Incineration"), ("b)", "Sewage Effluent treatment"), ("c)", "Dumping on "
#                                                                                                      "landfill"),
#                ("d)", "Controlled Dump sites"))
#     option6 = (("z)", "select"), ("a)", "Yes"), ("b)", "No"))
#
#     option8 = (("z)", "select"), ("a)", "Yes"), ("b)", "No"))
#     option9 = (("z)", "select"), ("a)", "Yes"), ("b)", "No"))
#     option10 = (("z)", "select"), ("a)", "Yes"), ("b)", "No"))
#
#     option12 = (("a)", "Yes"), ("b)", "No"))
#
#     one = models.CharField(verbose_name="1.	Types of Waste Collected: ",
#                            max_length=300, default='', choices=option1, null=True)
#     two = models.CharField(
#         verbose_name="2. What is the volume of waste disposed in (Kg) and the frequency: ",max_length=300,
#         default='', choices=option2, null=True)
#     three = models.CharField(verbose_name="3.	Are the waste sorted: ",
#                              max_length=300, default='', choices=option3, null=True)
#     four = models.CharField(verbose_name="4.	Are there mercury products in contained in the waste e.g Electric bulbs "
#                                          "florescent tubes, thermometers etc  ",
#                             max_length=300, default='', choices=option4, null=True)
#     five = models.CharField(verbose_name="5.	What method of disposal/recycling is carried: ",
#                             max_length=300, default='', choices=option5, null=True)
#     six = models.CharField(verbose_name="6.	Is there any control measures in place to mitigate against or reduce the "
#                                         "environmental hazards/degradation from the mercury contained waste "
#                                         "available:  ",
#                            max_length=300, default='', choices=option6, null=True)
#     seven = models.CharField(
#         verbose_name="7.	If yes, Kindly indicate what control measure is available, if No state 'N/A'  ",
#         max_length=3000, default='fill here')
#     eight = models.CharField(
#         verbose_name="8.	Is there any measurement of Mercury in your waste collected and in Kg? ",
#         max_length=300, default='', choices=option8, null=True)
#     nine = models.CharField(verbose_name=".	Is there any emission reduction devices? ",
#                             max_length=300, default='', choices=option9, null=True)
#     ten = models.CharField(verbose_name="10.	Is there any form of Particulate Matter (PM) Reduction?",
#                            max_length=300, default='', choices=option10, null=True)
#     eleven = models.CharField(
#         verbose_name="11.  If yes above, do you use acid gas control with Limestone or any similar acid "
#                      "gas absorbent? ", max_length=300, default='')
#     twelve = models.CharField(verbose_name="12.	Do you use mercury specific absorbent? (Kg Hg/Year) ",
#                               max_length=300, default='', choices=option12, null=True)
#     thirteen = models.CharField(
#         verbose_name="13. Kindly state other necessary information below that can help this research work: ",
#         max_length=3000, default='fill here')
#     fourteen = models.CharField(verbose_name="14.	Tonnes/year of municipal waste incinerated ", max_length=3000,
#                                 default='fill here')
#     fifteen = models.CharField(verbose_name="15.	Tonnes/year of hazardous waste incinerated", max_length=3000,
#                                default='fill here')
#     sixteen = models.CharField(verbose_name="16.	Tonnes/year of medical waste incinerated ", max_length=3000,
#                                default='fill here')
#     seventeen = models.CharField(verbose_name="17.	Tonnes/year of sewage sludge incinerated ", max_length=3000,
#                                  default='fill here')
#     eighteen = models.CharField(verbose_name="18.	Tonnes/year of domestic waste disposed off at dumpsite",
#                                 max_length=3000, default='fill here')
#     nineteen = models.CharField(verbose_name="19.	Tonnes/year waste burned", max_length=3000, default='fill here')
#     twenty = models.CharField(verbose_name="20.	Tonnes/year Sewage sludge incinerated ", max_length=3000,
#                               default='fill here')
#     twenty_one = models.CharField(
#         verbose_name="21.	Tonnes/year of Open fire waste burning (on landfills and informally)", max_length=3000,
#         default='fill here')
#     twenty_two = models.CharField(verbose_name="22.	What other technology do you use in treating waste?",
#                                   max_length=3000, default='fill here')
#     twenty_three = models.CharField(verbose_name="23.	What other pollution control mechanisms do you have in place?",
#                                     max_length=3000, default='fill here')
#     twenty_four = models.CharField(verbose_name="24.	What are your challenges?", max_length=3000,
#                                    default='fill here')
#     twenty_five = models.CharField(verbose_name="25.	What are your Suggestions/Recommendation?", max_length=3000,
#                                    default='fill here')


class ASGMining(models.Model):
    pass


class Waste(models.Model):
    pass

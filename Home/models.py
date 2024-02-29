import uuid
from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField


class Slider(models.Model):
    image = models.ImageField(upload_to='home/slider')
    title = models.TextField(max_length=100)
    description = models.TextField(max_length=200)


class Category(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class OurActivity(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='recent/activity')
    description = RichTextField(max_length=1000, null=True, blank=True)
    image2 = models.ImageField(upload_to='recent/activity', null=True, blank=True)
    image3 = models.ImageField(upload_to='recent/activity', null=True, blank=True)
    description2 = RichTextField(max_length=1000, null=True, blank=True)


class Event(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='recent/activity')
    description = RichTextField(max_length=1000, null=True, blank=True)
    date = models.DateField()
    time = models.CharField(max_length=12)


class MedicalCamp(models.Model):
    districtName = models.CharField(max_length=100, blank=True, null=True)
    policeStation = models.CharField(max_length=100, blank=True, null=True)
    campDate = models.CharField(max_length=100, blank=True, null=True)
    hostName = models.CharField(max_length=100, blank=True, null=True)
    Org_reg_Number = models.CharField(max_length=100, blank=True, null=True)
    org_est_date = models.CharField(max_length=100, blank=True, null=True)
    org_total_Member = models.CharField(max_length=10, blank=True, null=True)
    org_active_Members = models.CharField(max_length=100, blank=True, null=True)
    purpose = models.TextField(max_length=5000, blank=True, null=True)
    incidental_camp = models.CharField(max_length=100)
    incidental_camp_longTerm = models.TextField(blank=True, null=True)
    before_medical_camp = models.CharField(max_length=100)
    Long_term_work_plan = models.CharField(max_length=100, blank=True, null=True)
    Previous_Camp_Date = models.CharField(max_length=100, blank=True, null=True)
    Previous_Camp_with_whichOrg = models.CharField(max_length=100, blank=True, null=True)
    regFee_per_person = models.CharField(max_length=100, blank=True, null=True)
    include_local_diagnostic_center = models.CharField(max_length=100, blank=True, null=True)
    include_local_farma = models.CharField(max_length=100, blank=True, null=True)
    expected_Patient = models.IntegerField(blank=True, null=True)
    camp_Vanue = models.CharField(max_length=100, blank=True, null=True)
    local_unionCouncil = models.CharField(max_length=100, blank=True, null=True)
    police = models.CharField(max_length=100, blank=True, null=True)
    local_community_leader = models.CharField(max_length=100, blank=True, null=True)
    local_upazila = models.CharField(max_length=100, blank=True, null=True)
    patient_advanced_reg = models.CharField(max_length=100, blank=True, null=True)
    percentage_patient_advanced_reg = models.CharField(max_length=100, blank=True, null=True)
    provide_medicine = models.CharField(max_length=100, blank=True, null=True)
    amount_of_spendMoney_for_medicine = models.CharField(max_length=100, blank=True, null=True)
    volunteer_attend_for_camp = models.IntegerField()
    medical_team_want_to_take = models.CharField(max_length=100, blank=True, null=True)
    volunterr_conduct = models.CharField(max_length=100, blank=True, null=True)
    doctor_eat_Vanue = models.CharField(max_length=100, blank=True, null=True)
    away_from_the_campsite = models.CharField(max_length=100, blank=True, null=True)
    site_seeing_plans = models.CharField(max_length=100, blank=True, null=True)
    spotName = models.CharField(max_length=100, blank=True, null=True)
    one_night_accommodation = models.CharField(max_length=100, blank=True, null=True)
    blood_grouping = models.CharField(max_length=10, blank=True, null=True)
    eye_examination = models.CharField(max_length=10, blank=True, null=True)
    ear_examination = models.CharField(max_length=10, blank=True, null=True)
    diabetes_checkup = models.CharField(max_length=10, blank=True, null=True)
    urine_test = models.CharField(max_length=10, blank=True, null=True)
    ecg = models.CharField(max_length=10, default=False, blank=True, null=True)
    ultrasonogram = models.CharField(max_length=10, default=False, blank=True, null=True)
    weight_height_measurement = models.CharField(max_length=10,  blank=True, null=True)
    pulse_check_up_blood_oxygen_measurement = models.CharField(max_length=10, blank=True, null=True)
    blood_pressure_check_up = models.CharField(max_length=10, blank=True, null=True)
    heart_lung_check_up = models.CharField(max_length=10, blank=True, null=True)
    chief_executive_profession = models.CharField(max_length=100, blank=True, null=True)
    chief_executive_facebook = models.CharField(max_length=100, blank=True, null=True)
    chief_executive_mobilenumber = models.CharField(max_length=100, blank=True, null=True)
    communication_coordinator_profession = models.CharField(max_length=100, blank=True, null=True)
    communication_coordinator_facebook = models.CharField(max_length=100, blank=True, null=True)
    communication_coordinator_mobilenumber = models.CharField(max_length=100, blank=True, null=True)
    decoration_discipline_coordinator_profession = models.CharField(max_length=100, blank=True, null=True)
    decoration_discipline_coordinator_facebook = models.CharField(max_length=100, blank=True, null=True)
    decoration_discipline_coordinator_mobilenumber = models.CharField(max_length=100, blank=True, null=True)
    event_management_coordinator_profession = models.CharField(max_length=100, blank=True, null=True)
    event_management_coordinator_facebook = models.CharField(max_length=100, blank=True, null=True)
    event_management_coordinator_mobilenumber = models.CharField(max_length=100, blank=True, null=True)
    Food_hospitality_coordinator_profession = models.CharField(max_length=100, blank=True, null=True)
    Food_hospitality_coordinator_facebook = models.CharField(max_length=100, blank=True, null=True)
    Food_hospitality_coordinator_mobilenumber = models.CharField(max_length=100, blank=True, null=True)
    publicity_coordinator_profession = models.CharField(max_length=100, blank=True, null=True)
    publicity_coordinator_facebook = models.CharField(max_length=100, blank=True, null=True)
    publicity_coordinator_mobilenumber = models.CharField(max_length=100, blank=True, null=True)



from django.contrib import admin
from .models import Slider, Category, OurActivity, Event, MedicalCamp


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(OurActivity)
class OurActivityAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    search_fields = ('title',)


@admin.register(Event)
class EnevtAdmin(admin.ModelAdmin):
    list_display = ['uid', 'title', 'date', 'time', 'image']
    readonly_fields = ['uid']
    search_fields = ['title', 'description']


@admin.register(MedicalCamp)
class MedicalCampAdmin(admin.ModelAdmin):
    list_display = ('districtName', 'policeStation', 'campDate', 'hostName', 'Org_reg_Number', 'org_est_date', 'org_total_Member', 'org_active_Members', 'purpose', 'incidental_camp', 'incidental_camp_longTerm', 'before_medical_camp', 'Long_term_work_plan', 'Previous_Camp_Date', 'Previous_Camp_with_whichOrg', 'regFee_per_person', 'include_local_diagnostic_center', 'include_local_farma', 'expected_Patient', 'camp_Vanue', 'local_unionCouncil', 'police', 'local_community_leader', 'local_upazila', 'patient_advanced_reg', 'percentage_patient_advanced_reg', 'provide_medicine', 'amount_of_spendMoney_for_medicine', 'volunteer_attend_for_camp', 'medical_team_want_to_take', 'volunterr_conduct', 'doctor_eat_Vanue', 'away_from_the_campsite', 'site_seeing_plans', 'spotName', 'one_night_accommodation')
    search_fields = ('districtName', 'policeStation', 'campDate', 'hostName', 'Org_reg_Number', 'org_est_date', 'purpose', 'incidental_camp', 'incidental_camp_longTerm', 'before_medical_camp', 'Long_term_work_plan', 'Previous_Camp_Date', 'Previous_Camp_with_whichOrg', 'regFee_per_person', 'include_local_diagnostic_center', 'include_local_farma', 'camp_Vanue', 'local_unionCouncil', 'police', 'local_community_leader', 'local_upazila', 'patient_advanced_reg', 'percentage_patient_advanced_reg', 'provide_medicine', 'amount_of_spendMoney_for_medicine', 'medical_team_want_to_take', 'volunterr_conduct', 'doctor_eat_Vanue', 'away_from_the_campsite', 'site_seeing_plans', 'spotName', 'one_night_accommodation')

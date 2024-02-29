from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from .models import Event, Category, OurActivity, MedicalCamp, Slider


def Home(request):
    sliders = Slider.objects.all()
    cat = Category.objects.all()
    activity = OurActivity.objects.all().order_by('-id')
    return render(request, 'index.html', {'cat': cat, 'sliders': sliders,'activity':activity})


def event_list(request):
    events = Event.objects.all().order_by('-date')
    return render(request, 'events.html', {'events': events})


def event_detail(request, uid):
    event = get_object_or_404(Event, uid=uid)
    return render(request, 'event-single.html', {'event': event})


def recent_activaties(request):
    activity = OurActivity.objects.all()
    return render(request, 'all_recent.html', {'activity': activity})


def activity_details(request, uid):
    activity = get_object_or_404(OurActivity, uid=uid)
    return render(request, 'recent-single.html', {'activity': activity})


def category_detail(request, slug):
    category = Category.objects.get(slug=slug)
    activities = OurActivity.objects.filter(category=category)
    return render(request, 'recents.html', {'category': category, 'activities': activities})


def volunteer(request):
    return render(request, 'volunteer.html')


def medical_camp(request):
    if request.method == 'POST':
        # Retrieve data from the POST request
        district_name = request.POST.get('districtName')
        police_station = request.POST.get('policeStation')
        camp_date = request.POST.get('campDate')
        host_name = request.POST.get('hostName')
        org_reg_number = request.POST.get('Org_reg_Number')
        org_est_date = request.POST.get('org_est_date')
        org_total_member = request.POST.get('org_total_Member')
        org_active_members = request.POST.get('org_active_Members')
        purpose = request.POST.get('purpose')
        incidental_camp = request.POST.get('incidental_camp')
        incidental_camp_long_term = request.POST.get('incidental_camp_longTerm')
        before_medical_camp = request.POST.get('before_medical_camp')
        long_term_work_plan = request.POST.get('Long_term_work_plan')
        previous_camp_date = request.POST.get('Previous_Camp_Date')
        previous_camp_with_whichorg = request.POST.get('Previous_Camp_with_whichOrg')
        reg_fee_per_person = request.POST.get('regFee_per_person')
        include_local_diagnostic_center = request.POST.get('include_local_diagnostic_center')
        include_local_farma = request.POST.get('include_local_farma')
        expected_patient = request.POST.get('expected_Patient')
        camp_venue = request.POST.get('camp_Vanue')
        local_union_council = request.POST.get('local_unionCouncil')
        police = request.POST.get('police')
        local_community_leader = request.POST.get('local_community_leader')
        local_upazila = request.POST.get('local_upazila')
        patient_advanced_reg = request.POST.get('patient_advanced_reg')
        percentage_patient_advanced_reg = request.POST.get('percentage_patient_advanced_reg')
        provide_medicine = request.POST.get('provide_medicine')
        amount_of_spend_money_for_medicine = request.POST.get('amount_of_spendMoney_for_medicine')
        volunteer_attend_for_camp = request.POST.get('volunteer_attend_for_camp')
        medical_team_want_to_take = request.POST.get('medical_team_want_to_take')
        volunteer_conduct = request.POST.get('volunterr_conduct')
        doctor_eat_venue = request.POST.get('doctor_eat_Vanue')
        away_from_the_campsite = request.POST.get('away_from_the_campsite')
        site_seeing_plans = request.POST.get('site_seeing_plans')
        spot_name = request.POST.get('spotName')
        one_night_accommodation = request.POST.get('one_night_accommodation')
        blood_grouping = request.POST.get('blood_grouping')
        eye_examination = request.POST.get('eye_examination')
        ear_examination = request.POST.get('ear_examination')
        diabetes_checkup = request.POST.get('diabetes_checkup')
        urine_test = request.POST.get('urine_test')
        ecg = request.POST.get('ecg')
        ultrasonogram = request.POST.get('ultrasonogram')
        weight_height_measurement = request.POST.get('weight_height_measurement')
        pulse_check_up_blood_oxygen_measurement = request.POST.get('pulse_check_up_blood_oxygen_measurement')
        blood_pressure_check_up = request.POST.get('blood_pressure_check_up')
        heart_lung_check_up = request.POST.get('heart_lung_check_up')
        chief_executive_profession = request.POST.get('chief_executive_profession')
        chief_executive_facebook = request.POST.get('chief_executive_facebook')
        chief_executive_mobilenumber = request.POST.get('chief_executive_mobilenumber')
        communication_coordinator_profession = request.POST.get('communication_coordinator_profession')
        communication_coordinator_facebook = request.POST.get('communication_coordinator_facebook')
        communication_coordinator_mobilenumber = request.POST.get('communication_coordinator_mobilenumber')
        decoration_discipline_coordinator_profession = request.POST.get('decoration_discipline_coordinator_profession')
        decoration_discipline_coordinator_facebook = request.POST.get('decoration_discipline_coordinator_facebook')
        decoration_discipline_coordinator_mobilenumber = request.POST.get(
            'decoration_discipline_coordinator_mobilenumber')
        event_management_coordinator_profession = request.POST.get('event_management_coordinator_profession')
        event_management_coordinator_facebook = request.POST.get('event_management_coordinator_facebook')
        event_management_coordinator_mobilenumber = request.POST.get('event_management_coordinator_mobilenumber')
        food_hospitality_coordinator_profession = request.POST.get('Food_hospitality_coordinator_profession')
        food_hospitality_coordinator_facebook = request.POST.get('Food_hospitality_coordinator_facebook')
        food_hospitality_coordinator_mobilenumber = request.POST.get('Food_hospitality_coordinator_mobilenumber')
        publicity_coordinator_profession = request.POST.get('publicity_coordinator_profession')
        publicity_coordinator_facebook = request.POST.get('publicity_coordinator_facebook')
        publicity_coordinator_mobilenumber = request.POST.get('publicity_coordinator_mobilenumber')

        # Create a new MedicalCamp instance with the retrieved data
        medicalcamp = MedicalCamp.objects.create(
            districtName=district_name,
            policeStation=police_station,
            campDate=camp_date,
            hostName=host_name,
            Org_reg_Number=org_reg_number,
            org_est_date=org_est_date,
            org_total_Member=org_total_member,
            org_active_Members=org_active_members,
            purpose=purpose,
            incidental_camp=incidental_camp,
            incidental_camp_longTerm=incidental_camp_long_term,
            before_medical_camp=before_medical_camp,
            Long_term_work_plan=long_term_work_plan,
            Previous_Camp_Date=previous_camp_date,
            Previous_Camp_with_whichOrg=previous_camp_with_whichorg,
            regFee_per_person=reg_fee_per_person,
            include_local_diagnostic_center=include_local_diagnostic_center,
            include_local_farma=include_local_farma,
            expected_Patient=expected_patient,
            camp_Vanue=camp_venue,
            local_unionCouncil=local_union_council,
            police=police,
            local_community_leader=local_community_leader,
            local_upazila=local_upazila,
            patient_advanced_reg=patient_advanced_reg,
            percentage_patient_advanced_reg=percentage_patient_advanced_reg,
            provide_medicine=provide_medicine,
            amount_of_spendMoney_for_medicine=amount_of_spend_money_for_medicine,
            volunteer_attend_for_camp=volunteer_attend_for_camp,
            medical_team_want_to_take=medical_team_want_to_take,
            volunterr_conduct=volunteer_conduct,
            doctor_eat_Vanue=doctor_eat_venue,
            away_from_the_campsite=away_from_the_campsite,
            site_seeing_plans=site_seeing_plans,
            spotName=spot_name,
            one_night_accommodation=one_night_accommodation,
            blood_grouping=blood_grouping,
            eye_examination=eye_examination,
            ear_examination=ear_examination,
            diabetes_checkup=diabetes_checkup,
            urine_test=urine_test,
            ecg=ecg,
            ultrasonogram=ultrasonogram,
            weight_height_measurement=weight_height_measurement,
            pulse_check_up_blood_oxygen_measurement=pulse_check_up_blood_oxygen_measurement,
            blood_pressure_check_up=blood_pressure_check_up,
            heart_lung_check_up=heart_lung_check_up,
            chief_executive_profession=chief_executive_profession,
            chief_executive_facebook=chief_executive_facebook,
            chief_executive_mobilenumber=chief_executive_mobilenumber,
            communication_coordinator_profession=communication_coordinator_profession,
            communication_coordinator_facebook=communication_coordinator_facebook,
            communication_coordinator_mobilenumber=communication_coordinator_mobilenumber,
            decoration_discipline_coordinator_profession=decoration_discipline_coordinator_profession,
            decoration_discipline_coordinator_facebook=decoration_discipline_coordinator_facebook,
            decoration_discipline_coordinator_mobilenumber=decoration_discipline_coordinator_mobilenumber,
            event_management_coordinator_profession=event_management_coordinator_profession,
            event_management_coordinator_facebook=event_management_coordinator_facebook,
            event_management_coordinator_mobilenumber=event_management_coordinator_mobilenumber,
            Food_hospitality_coordinator_profession=food_hospitality_coordinator_profession,
            Food_hospitality_coordinator_facebook=food_hospitality_coordinator_facebook,
            Food_hospitality_coordinator_mobilenumber=food_hospitality_coordinator_mobilenumber,
            publicity_coordinator_profession=publicity_coordinator_profession,
            publicity_coordinator_facebook=publicity_coordinator_facebook,
            publicity_coordinator_mobilenumber=publicity_coordinator_mobilenumber
        )

        # Optionally, you can perform validation checks on the data before saving

        # Save the instance to the database
        medicalcamp.save()

        return redirect('/')  # Redirect to a success page after saving
    else:
        return render(request, 'host.html')

from django.shortcuts import render, get_object_or_404, redirect

from Home.models import Category
from .models import Volunteer


def add_volunteer(request):
    cat = Category.objects.all()
    if request.method == 'POST':
        volunteer_id = request.POST.get('volunteer_id')
        name = request.POST.get('name')
        email = request.POST.get('email')
        date_of_birth = request.POST.get('date_of_birth')
        permanent_address = request.POST.get('permanent_address')
        present_address = request.POST.get('present_address')
        profession = request.POST.get('profession')
        running_degree = request.POST.get('running_degree')
        leftest_degree = request.POST.get('leftest_degree')
        passing_year = request.POST.get('passing_year')
        institute = request.POST.get('institute')
        company_name = request.POST.get('company_name')
        designation = request.POST.get('designation')
        other_description = request.POST.get('other_description')
        blood_group = request.POST.get('blood_group')
        previous_organization = request.POST.get('previous_organization')
        organization_duty = request.POST.get('organization_duty')
        present_organization = request.POST.get('present_organization')
        interested_charity_work = request.POST.get('interested_charity_work')

        # Create a new Volunteer instance
        volunteer = Volunteer(
            volunteer_id=volunteer_id,
            name=name,
            email=email,
            date_of_birth=date_of_birth,
            permanentAddress=permanent_address,
            present_address=present_address,
            profession=profession,
            running_degree=running_degree,
            leftest_degree=leftest_degree,
            passing_year=passing_year,
            institute=institute,
            designation=designation,
            company_name=company_name,
            other_description=other_description,
            blood_group=blood_group,
            previous_organization=previous_organization,
            organization_duty=organization_duty,
            present_organization=present_organization,
            interested_charity_work=interested_charity_work
        )
        volunteer.save()
        return redirect('/contact')  # Redirect after successful form submission
    return render(request, 'volunteer.html', {'cat': cat})

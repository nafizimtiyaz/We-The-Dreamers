from django.shortcuts import render, get_object_or_404
from AboutUs.models import AboutUs, OurMission, Review, MedicalWings, DisasterManagementWig, EducationWing


def AboutView(request):
    about_info = AboutUs.objects.all()
    mission = OurMission.objects.all()
    reviews = Review.objects.all()
    return render(request, 'About.html',
                  {'about_info': about_info, 'mission': mission, 'reviews': reviews})  # only mision only loop.


# def about_us_detail(request, uid):
#     about_info = get_object_or_404(AboutUs, uid=uid)
#     return render(request, 'about_us_detail.html', {'about_info': about_info})

def medical_wings(request):
    medi = MedicalWings.objects.all()
    return render(request, 'medicalwings-single.html', {'medi': medi})


def education_wings(request):
    medi = EducationWing.objects.all()
    return render(request, 'medicalwings-single.html', {'medi': medi})


def disaster_wings(request):
    medi = DisasterManagementWig.objects.all()
    return render(request, 'diseterwings.html', {'medi': medi})

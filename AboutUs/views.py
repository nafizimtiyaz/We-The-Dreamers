from django.shortcuts import render, get_object_or_404

from AboutUs.models import AboutUs


def AboutView(request):
    about_info = AboutUs.objects.all()
    return render(request, 'About.html', {'about_info': about_info})


# def about_us_detail(request, uid):
#     about_info = get_object_or_404(AboutUs, uid=uid)
#     return render(request, 'about_us_detail.html', {'about_info': about_info})

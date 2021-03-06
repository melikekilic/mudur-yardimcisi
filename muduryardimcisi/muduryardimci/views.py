from django.shortcuts import render, redirect
from django_otp.oath import hotp
from .models import Courses,Profile,Check,Site
import random
from time import localtime, strftime

def generate_token(request):
	if request.method = 'POST':
		
    key = bytes(random.randint(1000000,99999999))
    for i in range(1):
        token = hotp(key=key, counter=i, digits=6)
        if len(str(token)) < 6:
            token = (6 - len(str(token))) * str(random.randint(1, 9)) + str(token)
    get_course_id = Profile.objects.get(user=request.user,is_trainer=True).course_id
    get_course_token = Courses.objects.filter(course_name=get_course_id).update(course_token=token)
    return render(request, 'auth.html', {"token": token})

def stundent_check(request):
    main_site_name = "2018 kamp"
    get_start_time = Site.objects.get(is_active=True,name=main_site_name).course_start
    get_total_morning_date = float(Site.objects.get(is_active=True, name=main_site_name).total_morning_date)
    get_total_afternoon_date = float(Site.objects.get(is_active=True, name=main_site_name).total_afternoon_date)

    def calucate_time(time):
        try:
            start_hour, start_min = str(get_start_time).split(":")
        except TypeError:
            return ("Fatal Error... ")
        if time == "evening":
            find_time = int(start_hour) + get_total_morning_date + get_total_afternoon_date
        elif time == "afternoon":
            find_time = int(start_hour) + get_total_morning_date
        elif time == "morning":
            find_time = float(start_hour)
        number_dec = int(str(find_time - int(find_time))[2:])
        number_dec = (number_dec / 10)
        find_hour = find_time - number_dec
        number_dec = number_dec *60
        find_start_min = int(start_min) + number_dec
        if find_start_min >= 60.0:
            find_start_min -= 60
            find_hour += 1
        start_min = float(find_start_min) / 100.0
        find_time = float(find_hour) + start_min
        return(find_time)
    afternoon = calucate_time("afternoon")
    evening = calucate_time("evening")
    morning = calucate_time("morning")
    print(morning,afternoon,evening)
    hour_now, min_now = str(strftime("%H:%M", localtime())).split(":")
    min_now = float(min_now) /100
    hour_now = float(hour_now)
    time_now = hour_now + min_now
    if time_now > morning and time_now < afternoon and time_now < evening:
        check_time = "morning"
    elif time_now > morning and time_now > afternoon and time_now < evening:
        check_time = "afternoon"
    elif time_now > morning and time_now > afternoon and time_now > evening:
        check_time = "evening"
    print(check_time)
    #get_course_id = Profile.objects.get(user=request.user, is_trainer=False).course_id
    #get_or_create_check_id = Check.objects.get_or_create(course_id = get_course_id,user_id=request.user)
    #get_or_create_check_id.save()
    return render(request, 'check_stundent.html',)
def dashboard(request):
    check = Check.objects.all()
    return render(request, 'accounts/dashboard.html',{"check": check})


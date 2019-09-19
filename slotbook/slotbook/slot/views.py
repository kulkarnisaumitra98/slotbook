# Create your views here.
from django.db import IntegrityError
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, HttpResponse, HttpResponseRedirect, reverse
from django.http import JsonResponse
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from django.core.mail import send_mail
from smtplib import SMTP, SMTPException
# Create your views here.
from .models import *
import json

# def index(request):
#     return render(request, 'login.html', {})


def login_func(request):
    if request.method == "POST":
        reg_id = request.POST.get('reg_id')
        email = request.POST.get('email')
        print(reg_id)
        try:
            user = Register.objects.get(receipt_no=reg_id)
            print(user)
        except MultipleObjectsReturned:
            return render(request, 'login.html', {'msg': "Please Contact us at clash.credenz19@gmail.com !"})
        except ObjectDoesNotExist:
            return render(request, 'login.html', {'msg': "Not Registered"})

        slots = SlotsTiming.objects.all()
        event_list = user.events.split(',')
        if user.email1 == email or user.email2 == email:
            if "CLASH" in event_list or "RC" in event_list or "ENIGMA" in event_list:
                if user.session == "true":
                    return render(request, 'slot.html', {'user': user, 'events': event_list, 'slots': slots})
                return render(request, 'login.html', {'msg': "You can book the slot only once !"})
            return render(request, 'login.html', {'msg': "Register for Clash or RC to book a slot !"})
        return render(request, 'login.html', {'msg': "Not Matched !"})
    else:
        return render(request, 'login.html')


def book(request):
    if request.method == 'POST':
        reg_id = request.POST.get('user')
        events = request.POST.get('events')
        events = events.replace("'", "")
        events = events.replace(" ", "")
        events = events.strip('][').split(',')
        event = request.POST.get('category')
        day = request.POST.get('daycat')
        time = request.POST.get('timecat')

        try:
            user = Register.objects.get(receipt_no=reg_id)
        except ObjectDoesNotExist:
            return render(request, 'login.html', {'msg': "Please Contact us at clash.credenz19@gmail.com !"})

        user.save()

        try:
            booking = Booking.objects.get(user=reg_id)
        except ObjectDoesNotExist:
            booking = Booking.objects.create(user=reg_id)

        msg = ''
        if event == "CLASH":
            booking.clash = time
            booking.c_day = day
            booking.email_response = booking.email_response + ' CLASH:' + '\n' + ' Day: '+str(day) + '\n' + ' Time: ' + str(time) + '\n'
            events.remove('CLASH')
            print("clash" + booking.email_response)
            msg = "Response saved for Clash"

        elif event == "RC":
            booking.rc = time
            booking.r_day = day
            booking.email_response = booking.email_response + ' REVERSE CODING:' + '\n' + ' Day: '+str(day) + '\n' + ' Time: ' + str(time)+'\n'
            events.remove('RC')
            print("rc" + booking.email_response)
            msg = "Response saved for Reverse Coding"

        elif event == "ENIGMA":
            booking.enigma = time
            booking.e_day = day
            booking.email_response = booking.email_response + ' ENIGMA: ' + '\n' + ' Day: '+str(day) + '\n' + ' Time: ' + str(time)+'\n'
            events.remove('ENIGMA')
            msg = "Response saved for Enigma"

        booking.save()
        if events:
            return render(request, 'slot.html', context={'events': events, 'user': user, 'msg': msg})

        user.session = "false"
        user.save()
        print("email_response:\n"+booking.email_response)

        # try:
        #     subject = 'Thank you for Booking the Slots'
        #     message = booking.email_response
        #     email_from = settings.EMAIL_HOST_USER
        #     recipient_list = [user.email1, user.email2]
        #     # recipient_list = ['clashrc2k19@gmail.com']
        #     send_mail(subject, message, email_from, recipient_list, fail_silently=False)
        #     # send_mail(
        #     #     'Successfully booked',
        #     #     str(booking.email_response),
        #     #     'from@example.com',
        #     #     ['to@example.com'],
        #     #     fail_silently=False,
        #     # )
        #     # context = {'msg': "Email has been sent"}
        #     # context = {'msg': "Successfully Booked"}
        #     print('success->email')
        # except SMTPException:
        #     print('email sending failed')

        # messages.success(request, 'Successfully Booked')
        return HttpResponseRedirect(reverse('log'))
    else:
        pass


# def script(request):
#     if request.method == "POST":
#         password = request.POST.get('password')
#         if password == '7':
#             f = open('register.csv', 'r')
#             # f = open('test.txt', 'r')
#             for line in f:
#                 line = line.split(';')
#                 print(line[1])
#                 Register.objects.create(receipt_no=2)
#                 break
#             print("done")
#             return HttpResponse("Good_to_go")
#         else:
#             return HttpResponse("invalid_password")
#     else:
#         return render(request, 'log.html', {'msg': "script"})


def script(request):
    f = open('regf.csv', 'r')
    # f = open('test.txt', 'r')
    a = 0
    for line in f:
        if a != 0:
            line = line.split(';')
            # print(line)
            Register.objects.create(college=line[1],
                                    date=line[2],
                                    email1=line[3],
                                    email2=line[4],
                                    events=line[5],
                                    field_id=line[6],
                                    name1=line[7],
                                    name2=line[8],
                                    name3=line[9],
                                    name4=line[10],
                                    phone1=line[11],
                                    phone2=line[12],
                                    receipt_no=line[13],
                                    total=line[14],
                                    year=line[15])
            print("f")
        else:
            a = a + 1
            print('ff')

    return HttpResponse("Good_to_go")


def change_drop(request):
    print(request.POST)
    return JsonResponse({"status":"OK"})

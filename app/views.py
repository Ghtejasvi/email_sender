from django.shortcuts import render,redirect
from rest_framework import viewsets
from rest_framework.decorators import api_view,permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
import json
from django.http import Http404,HttpResponseBadRequest,JsonResponse,HttpResponse
from django.core import serializers
from rest_framework import status,generics
import traceback
from django.core.mail import send_mail
from django.template import loader

def mail(request):
    if request.method == 'POST':
        mail_id = []
        description = loader.render_to_string("mail/mail.html",{'name':'hello','body':'how are you??','sign':'tejasvi'})
        send_mail('Congratulation','you are lucky resive this mail','tejasvighoniya2610@gmail.com',['drashtikumbhani23@gmail.com'],html_message= description,fail_silently=False)
        return HttpResponse("send it...")
    else:
        return render(request,'btn.html')
    
# 'deepsojitra336@gmail.com','talaviyashikha@gmail.com','bhaktivaghasiya.bv98@gmail.com','diptidudhat71@gmail.com'
# return HttpResponse("Email send it..")
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore , register_events , register_job

# scheduler = BackgroundScheduler()
# scheduler.add_jobstore(DjangoJobStore(),'default')

# @register_job(scheduler,"interval",seconds=1)
# def test():
#     print("test !!")

# register_events(scheduler)
# scheduler.start()

def hello(request):
    data = []
    datajson = {"Hello":"World"}
    data.append(datajson)
    return JsonResponse({"data":data})

# def 
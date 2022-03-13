from django.http import HttpResponse
from django.shortcuts import render
import django_rq
import json
from rq import Queue
from rq.job import Job
from .tasks import espeak_task, redis_conn

def home(request):
	return render(request, "django_rq_espeak_app/espeak.html")

def espeak(request):
	q = Queue(connection=redis_conn)
	ret = {'id': ''}
	txt = request.GET['txt']
	job = django_rq.enqueue(espeak_task, txt)
	ret['id'] = job.id
	return HttpResponse(json.dumps(ret))	

def checkstatus(request):
	job = Job.fetch(request.GET['id'], connection=redis_conn)
	ret = { 'mp3url' : ''}
	if job:
		if job.get_status() == 'finished':
			ret['mp3url'] = job.result
	return HttpResponse(json.dumps(ret))




	

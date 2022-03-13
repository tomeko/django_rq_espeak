from django_rq import job
from time import sleep
import django_rq
import os
from rq import get_current_job
from django.conf import settings

# host,pw, etc are in settings
redis_conn = django_rq.get_connection()

@job
def espeak_task(txt):
	id = get_current_job().id
	oscmd = f"espeak \"{txt}\"  --stdout | ffmpeg -i - -ar 44100 -ac 2 -ab 192k -f mp3 \"{settings.BASE_DIR}/static/ttsout/{id}.mp3\""
	print(oscmd)
	os.system(oscmd)
	mp3url_rel = f'/static/ttsout/{id}.mp3'
	return mp3url_rel


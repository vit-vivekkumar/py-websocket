from django.http import HttpResponseBadRequest
from django.shortcuts import render, HttpResponse
from .models import Chat, Group
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
# Create your views here.
def index(request, group_name):
  print("Group Name...", group_name)
  group = Group.objects.filter(name = group_name).first()
  chats = []
  if group:
    chats = Chat.objects.filter(group = group)
  else:
    group = Group(name = group_name)
    group.save()
  return render(request, 'index.html', {'groupname': group_name, 'chats':chats})

import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def msgfromoutside(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)
        group_name = body_data.get('group_name', None)
        
        if group_name:
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                group_name,
                {
                    'type': 'chat.message',
                    'message': body_data.get('msg', '')
                }
            )
            return HttpResponse("Message sent to group {}".format(group_name))
    
    return HttpResponseBadRequest()

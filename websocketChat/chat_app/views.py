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

def msgfromoutside(request):
  channel_layer = get_channel_layer()
  print('channel_layer',channel_layer)
  async_to_sync(channel_layer.group_send)(
    'india',
    {
      'type':'chat.message',
      'message':'Message from outside consumer'
    }
  )
  return HttpResponse("Message Sent from View to Consumer")
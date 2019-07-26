import json
from django.shortcuts import render
from django.utils.safestring import mark_safe


def index(request):
    return render(request, 'chat_app/index.html', {})


def room(request, room_name):
    room_name_json = mark_safe(json.dumps(room_name))

    context = {
        'room_name_json': room_name_json
    }
    return render(request, 'chat_app/room.html', context)
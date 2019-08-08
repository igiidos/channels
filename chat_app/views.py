import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe

from chat_app.models import OpenRoom, OneToOneRoom


@login_required
def index(request):
    return render(request, 'chat_app/index.html', {})


@login_required
def one_index(request):
    return render(request, 'chat_app/one_index.html', {})


@login_required
def room(request, room_name):
    if not OpenRoom.objects.filter(title=room_name).exists():
        create = OpenRoom.objects.create(title=room_name)
        create.users.add(request.user)
        create.save()
    else:
        join = OpenRoom.objects.get(title=room_name)
        join.users.add(request.user)
        join.save()

    room_name_json = mark_safe(json.dumps(room_name))

    context = {
        'room_name': room_name,
        'room_name_json': room_name_json
    }
    return render(request, 'chat_app/room.html', context)



@login_required
def one_room(request, room_name):
    if not OneToOneRoom.objects.filter(title=room_name).exists():
        create = OneToOneRoom.objects.create(title=room_name)
        create.users.add(request.user)
        create.limitation += 1
        create.save()
    elif OneToOneRoom.objects.filter(title=room_name, limitation=1).exists():
        join = OneToOneRoom.objects.get(title=room_name)
        join.users.add(request.user)
        join.limitation += 1
        join.save()
    else:
        print("안됌")
        return redirect('index')

    room_name_json = mark_safe(json.dumps(room_name))

    context = {
        'room_name': room_name,
        'room_name_json': room_name_json
    }
    return render(request, 'chat_app/one_room.html', context)


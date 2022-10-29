from django.shortcuts import render

# Create your views here.

rooms = [
    {'id':1, 'name':'中文假文產生器'},
    {'id':2, 'name':'這是什麼鬼東西？'},
    {'id':3, 'name':'這能幹嘛？'},
]


def home(request):
    context = {'rooms':rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room': room}
    return render(request, 'base/room.html', context)
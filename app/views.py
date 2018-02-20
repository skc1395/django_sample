from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Room, RoomType, RoomAgree, RoomOption, University


def room_list(request):
    rooms = Room.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'app/room_list.html', {'rooms':rooms})

def room_detail(request, pk):
    room = get_object_or_404(Room, pk=pk)
    return render(request, 'app/room_detail.html', {'room':room})

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Room, RoomType, RoomAgree, RoomOption, University
from .forms import RoomForm
from .get_geocode import Get_geocode
from . import constant

def room_list(request):
    rooms = Room.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'app/room_list.html', {'rooms':rooms})

def room_detail(request, pk):
    room = get_object_or_404(Room, pk=pk)
    return render(request, 'app/room_detail.html', {'room':room})

def room_new(request):
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.address_lng = Get_geocode(request.POST['address'],constant.API_KEY)[0]
            room.address_lat = Get_geocode(request.POST['address'],constant.API_KEY)[1]
            room.published_date = timezone.now()
            room.save()
            return redirect('room_detail', pk=room.pk)
    else:
        form = RoomForm()
    return render(request, 'app/room_edit.html', {'form': form})

def room_edit(request, pk):
    room = get_object_or_404(Room, pk=pk)
    if request.method == "POST":
        form = RoomForm(instance=room)
        if form.is_valid():
            room = form.save(commit=False)
            address_lng = Get_geocode(room.address_lng, API_KEY)
            address_lat = Get_geocode(room.address_lat, API_KEY)
            room.published_date = timezone.now()
            room.save()
            return redirect('room_detail', pk=room.pk)
    else:
        form = RoomForm(instance=room)
    return render(request, 'app/room_edit.html', {'form': form})

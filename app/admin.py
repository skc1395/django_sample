from django.contrib import admin
from .models import Room, RoomType, RoomAgree, RoomOption, University, Door

# Register your models here.
admin.site.register(Room)
admin.site.register(RoomType)
admin.site.register(RoomAgree)
admin.site.register(RoomOption)
admin.site.register(University)
admin.site.register(Door)

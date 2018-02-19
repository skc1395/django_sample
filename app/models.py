from django.db import models
from django.utils import timezone

class RoomType(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class RoomAgree(models.Model):
    agree = models.CharField(max_length=50)

    def __str__(self):
        return self.agree

class RoomOption(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Door(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class University(models.Model):
    name = models.CharField(max_length=30)
    door = models.ManyToManyField(Door)

    def __str__(self):
        return self.name


class Room(models.Model):
    title = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    deposit_ori = models.IntegerField()
    rentfee_ori = models.IntegerField()
    deposit_new = models.IntegerField()
    rentfee_new = models.IntegerField()
    manage_fee = models.CharField(max_length=30)
    date_start = models.DateField()
    date_end = models.DateField()
    room_type = models.ForeignKey(RoomType)
    room_agree = models.ForeignKey(RoomAgree)
    contact = models.CharField(max_length=50)
    room_option = models.ManyToManyField(RoomOption)
    text = models.TextField()
    university = models.ForeignKey(University)

    #뭐하는 기능인지
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

from django.contrib import admin
from .models import Member, Document, Photo, Video
# Register your models here.
admin.site.register(Member)
admin.site.register(Document)
admin.site.register(Photo)
admin.site.register(Video)
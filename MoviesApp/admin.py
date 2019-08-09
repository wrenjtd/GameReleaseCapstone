from django.contrib import admin
from . models import Game, GamePlatform, Member

admin.site.register(Game)
admin.site.register(GamePlatform)
admin.site.register(Member)

# Register your models here.

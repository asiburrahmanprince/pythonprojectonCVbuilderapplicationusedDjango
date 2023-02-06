from django.contrib import admin
from .models import Skill,User,Cv,Academic,Profile

model_list = [User, Skill,Cv,Academic,Profile]
admin.site.register(model_list)

# Register your models here.

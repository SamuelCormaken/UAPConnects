from django.contrib import admin
from .models import User,Post,Comment,Resources,Club,ClubMember
# Register your models here.
admin.site.register([User,Post,Comment,Resources,Club,ClubMember])
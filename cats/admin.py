from django.contrib import admin

from cats.models import Cats, Breed
# Register your models here.
admin.site.register(Cats)
admin.site.register(Breed)

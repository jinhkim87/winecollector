from django.contrib import admin
# import your models here
from .models import Wine, Year, Food, Photo

# Register your models here
admin.site.register(Wine)
admin.site.register(Year)
admin.site.register(Food)
admin.site.register(Photo)
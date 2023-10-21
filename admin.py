from django.contrib import admin
from django.contrib.admin.sites import site
from news.models import News
class newsadmin(admin.ModelAdmin):
    list_display=('news_title','news_desc')


admin.site.register(News,newsadmin)    


# Register your models here.

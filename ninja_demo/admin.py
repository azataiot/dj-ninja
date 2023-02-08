from django.contrib import admin
from ninja_demo import models


# Register your models here.


class OneAdmin(admin.ModelAdmin):
    pass


class TwoAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.One, OneAdmin)
admin.site.register(models.Two, TwoAdmin)

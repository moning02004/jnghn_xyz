from django.contrib import admin

from .models import HeartPlan, Plan, Detail


admin.site.register(HeartPlan)
admin.site.register(Plan)
admin.site.register(Detail)

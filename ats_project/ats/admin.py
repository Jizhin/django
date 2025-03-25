from django.contrib import admin

from .models import Candidate


class CandidateAdmin(admin.ModelAdmin):
    list_display = ("name", "age", "gender", "email", "phone_number")
    search_fields = ("name", "email")


admin.site.register(Candidate)
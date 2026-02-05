from django.contrib import admin

from django import forms

from .models import Category, ContactMessage, EmploymentMessage, Project, ProjectImage

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline]

# Register your models here.
admin.site.register(Project)
admin.site.register(ProjectImage)
admin.site.register(Category)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email', 'message')

@admin.register(EmploymentMessage)
class EmploymentMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'job_applied_for', 'cv')
    search_fields = ('name', 'job_applied_for', 'cv')

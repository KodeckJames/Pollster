from django.contrib import admin

# Register your models here.
from .models import Questions, Choices

admin.site.site_header = 'Pollster Admin'
admin.site.site_title = 'Pollster Admin Area'
admin.site.index_title = 'Welcome to the Pollster admin ares'

class ChoicesInline(admin.TabularInline):
    model = Choices
    extra = 3

# @admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('question_text',)}),
        ('Date Information', {'fields': ('pub_date',), 'classes': ('collapse',)}),
    )
    inlines = [ChoicesInline]

# admin.site.register(Questions)
# admin.site.register(Choices)
admin.site.register(Questions, QuestionsAdmin)
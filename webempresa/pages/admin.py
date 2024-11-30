from django.contrib import admin
class PageAdmin(admin.ModelAdmin):
 readonly_fields = ('created', 'updated')
 list_display = ('title', 'order')
